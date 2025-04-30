import string
from typing import Generator, Tuple
import xml.etree.ElementTree as ET
import re
from typing import Optional, Tuple


def getAdjWordPair(text: str) -> Generator[tuple[str, str], None, None]:
    """
    处理输入的文本，清洗后迭代输出相邻的单词对。

    清洗规则：
    - 将换行符 (\\n) 和回车符 (\\r) 视为空格。
    - 将任何标点符号 (string.punctuation) 视为空格。
    - 忽略非字母 (A-Z 和 a-z 之外) 字符：除了字母和空格，其他字符都替换为空格
    - 忽略大小写，只保留小写字母。
    - 连续的空格被视为一个分隔符。

    Args:
        text: 输入的原始文本字符串。

    Yields:
        处理后的文本中的相邻单词对，格式为 (word1, word2) 的元组，
        其中 word1 和 word2 都是小写字符串。
    """
    if not isinstance(text, str):
        # 可以在函数开始处进行类型检查，或者依赖后续字符串方法的错误处理
        # 为了明确性，这里可以添加一个检查
        # raise TypeError("Input must be a string.")
        # 或者简单处理非字符串输入，例如视为空文本
        text = str(text)  # 尝试转换为字符串

    # 1. 将换行/回车符替换为 空格
    cleaned_text = text.replace("\n", " ").replace("\r", " ")

    # 2. 转换为小写
    cleaned_text = cleaned_text.lower()

    # 3. 将非字母字符替换为 空格 (保留字母和已有的空格)
    #    string.punctuation 包含常用的标点，但直接检查字母范围更全面，且能处理数字等非字母字符
    processed_text = ""
    previous = ""
    for char in cleaned_text:
        if "a" <= char <= "z":
            processed_text += char
            continue

        if processed_text:
            if previous:
                yield (previous, processed_text)
            previous = processed_text
            processed_text = ""

    if processed_text:
        if previous:
            yield (previous, processed_text)

    # # 4. 按 空格 分割成单词列表，split() 会自动处理多个连续 空格 并忽略开头/结尾的 空格
    # words = processed_text.split()

    # # 5. 迭代输出相邻的单词对
    # # 需要至少有两个单词才能形成一对 (word1, word2)
    # # 迭代范围是 len(words) - 1，确保 words[i+1] 不越界
    # if len(words) < 2:
    #     return  # 单词少于两个，无法形成相邻对，生成器结束

    # for i in range(len(words) - 1):
    #     yield (words[i], words[i + 1])


# Helper function to parse SVG dimension string (e.g., "100px", "50", "2in")
def _parse_svg_dimension(dimension_str: Optional[str]) -> Optional[float]:
    """
    解析 SVG 尺寸字符串 (如 "100px", "50", "2em")。
    目前支持无单位 (视为 px) 和 'px' 单位。
    返回像素值，如果解析失败、单位不受支持或为相对单位，则返回 None。
    """
    if dimension_str is None:
        return None

    # 移除前导/后导空白符
    dimension_str = dimension_str.strip()

    # 正则表达式用于捕获数值和可选的单位
    match = re.match(r"(\d+\.?\d*)([a-zA-Z%]*)$", dimension_str)

    if not match:
        # 格式不匹配
        return None

    value_str, unit = match.groups()
    try:
        value = float(value_str)
    except ValueError:
        # 数值无效
        return None

    # 处理单位
    unit = unit.lower()
    if unit in ("px", ""):  # 无单位通常视为 px
        return value
    elif (
        unit == "pt"
    ):  # 1pt = 1/72 inch, 标准网页 DPI 96 --> 1pt = 96/72 px = 4/3 px
        return value * (4 / 3)
    elif unit == "in":  # 1 inch = 96px (标准网页 DPI)
        return value * 96
    elif (
        unit == "cm"
    ):  # 1 cm = 0.3937 inches --> 1cm = 0.3937 * 96 px ≈ 37.795 px
        return value * 37.795

    # 对于不支持的单位或相对单位（如 %），我们无法确定实际像素值，返回 None
    print(
        f"Warning: Unsupported or relative unit '{unit}' found in dimension '{dimension_str}'. Cannot determine pixel value reliably."
    )
    return None


def get_svg_pixel_dimensions(file_path: str) -> Optional[tuple[float, float]]:
    """
    根据 SVG 文件的 'width' 和 'height' 属性获取其像素尺寸。

    Args:
        file_path: SVG 文件的路径。

    Returns:
        如果成功从 'width' 和 'height' 属性中解析出像素宽度和高度，则返回一个元组 (width, height)，
        否则返回 None。注意 SVG 是矢量图，其像素尺寸取决于渲染或显式属性。
        此函数依赖于根 <svg> 元素的 width 和 height 属性来获取像素值或无单位值。
    """
    try:
        # 解析 XML 文件
        tree = ET.parse(file_path)
        root = tree.getroot()

        # 检查根元素是否是 SVG 元素 (需要考虑命名空间)
        svg_namespace = "http://www.w3.org/2000/svg"
        # ET.Element.tag 包含命名空间信息，格式为 '{namespace}tagname'
        if not root.tag == f"{{{svg_namespace}}}svg":
            print(f"Warning: Root element is not <svg> in {file_path}")
            return None

        # 获取 width 和 height 属性的值
        width_attr = root.get("width")
        height_attr = root.get("height")

        # 使用辅助函数解析尺寸
        width_px = _parse_svg_dimension(width_attr)
        height_px = _parse_svg_dimension(height_attr)

        # 如果宽度和高度都成功解析为像素值
        if width_px is not None and height_px is not None:
            return width_px, height_px
        else:
            # 如果 width 或 height 属性缺失、无效（非像素/无单位）或使用了不支持的单位，
            # 则无法从属性中可靠地确定像素尺寸。虽然可以尝试使用 viewBox，
            # 但没有明确的渲染上下文或 DPI，像素尺寸是模糊的。
            # 这里我们选择在无法从 width/height 属性直接确定时返回 None。
            print(
                f"Warning: Could not determine reliable pixel dimensions from 'width' and 'height' attributes in {file_path}."
            )
            print(
                f"Attributes found: width='{width_attr}', height='{height_attr}'."
            )
            # 可以选择在这里尝试从 viewBox 推断，但这通常需要更多上下文
            # 如果 viewBox="0 0 vw vh" 且无 width/height，则宽高可以视为 vw x vh 用户单位
            # 如果用户单位默认是 px，那就可以用 viewBox 的宽高，但这不总是可靠的。
            # 稳妥起见，只依赖 width/height 属性。
            return None

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except ET.ParseError:
        print(f"Error: Could not parse SVG file {file_path} as valid XML.")
        return None
    except Exception as e:
        # 捕获其他意外错误
        print(f"An unexpected error occurred: {e}")
        return None


# 示例用法：
if __name__ == "__main__":
    sample_text = """
To explore strange new worlds,
To seek out new life and new civilizations.
"""

    print("从示例文本中提取的相邻单词对：")
    for pair in getAdjWordPair(sample_text):
        print(pair)

    print("\n另一个简单示例：")
    sample_text_simple = "  Hello, World! This is a test...  "
    for pair in getAdjWordPair(sample_text_simple):
        print(pair)

    print("\n单空格文本示例：")
    sample_text_single = "Single"
    for pair in getAdjWordPair(sample_text_single):
        print(pair)  # 应该没有任何输出

    print("\n空文本示例：")
    sample_text_empty = ""
    for pair in getAdjWordPair(sample_text_empty):
        print(pair)  # 应该没有任何输出

    print("\n只有空格和符号的文本示例：")
    sample_text_symbols = " !@#$%^&*() "
    for pair in getAdjWordPair(sample_text_symbols):
        print(pair)  # 应该没有任何输出
