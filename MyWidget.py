import random
import sys
import time
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QFileDialog,
    QMessageBox,
    QTableWidgetItem,
    QTableWidget,
)
from PySide6.QtCore import (
    QMutex,
    QRunnable,
    QThreadPool,
    QMutexLocker,
    Signal,
)
from panel_ui import Ui_Form
from ImageDialog import ImageDialog
from Graph import Graph
import Utils


class MyWidget(QWidget, Ui_Form):

    # 定义用于与 GUI 线程通信的信号
    # 信号参数是要传递的数据类型
    update_text_signal = Signal(str, bool)  # 用于更新文本框
    walk_finished_signal = Signal()  # 信号，表示随机漫步完成

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self.initSlots()

        self.graph = Graph()  # 图对象
        self.graphInitialized = False
        self.path = None  # 传递最短路径
        self.stopWalk = False  # 停止随机游走标志
        self.mutex = QMutex()  # 互斥锁

    def initUi(self):
        # Initialize your UI components here
        self.tabWidget.setCurrentIndex(0)
        self.setWindowTitle("SE Lab1")
        self.tableWidget_outputPageRank.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )  # 禁止编辑表格

    def initSlots(self):
        # Connect signals and slots here

        # tab 1
        self.pushButton_getFilePath.clicked.connect(self.getFilePath)
        self.pushButton_generateFromFile.clicked.connect(
            self.generateDirectedGraphFromFile
        )
        self.pushButton_generateFromPlainText.clicked.connect(
            self.generateDirectedGraphFromText
        )

        # tab 2
        self.pushButton_showGraphInText.clicked.connect(
            self.showDirectedGraphInText
        )
        self.pushButton_showGraphInImage.clicked.connect(
            self.showDirectedGraphInImage
        )
        self.pushButton_saveGraphAsImage.clicked.connect(self.saveGraphAsImage)

        # tab 3
        self.comboBox_bridgeStart.currentTextChanged.connect(
            self.comboBox_bridgeStart_currentTextChanged
        )
        self.comboBox_bridgeEnd.currentTextChanged.connect(
            self.comboBox_bridgeEnd_currentTextChanged
        )
        self.pushButton_calcBridgeWord.clicked.connect(self.queryBridgeWords)

        # tab 4
        self.pushButton_generateNewText.clicked.connect(self.generateNewText)

        # tab 5
        self.comboBox_shortestPathStart.currentTextChanged.connect(
            self.comboBox_shortestPathStart_currentTextChanged
        )
        self.comboBox_shortestPathEnd.currentTextChanged.connect(
            self.comboBox_shortestPathEnd_currentTextChanged
        )
        self.checkBox_calcStartToAll.stateChanged.connect(
            self.checkBox_calcStartToAll_stateChanged
        )
        self.pushButton_calcShortestPath.clicked.connect(self.calShortestPath)
        self.comboBox_shortestPath.currentIndexChanged.connect(
            self.comboBox_shortestPath_currentIndexChanged
        )
        self.pushButton_showPathInImage.clicked.connect(
            self.showShortestPathInImage
        )

        # tab 6
        self.pushButton_startPageRank.clicked.connect(self.calPageRank)

        # tab 7
        self.pushButton_startRandomWalk.clicked.connect(self.randomWalk)
        self.pushButton_stopRandomWalk.clicked.connect(self.stopRandomWalk)

        # 连接自定义信号到处理 GUI 更新的槽函数
        self.update_text_signal.connect(self.appendRandomWalkText)
        # 连接完成信号到处理结束的槽函数
        self.walk_finished_signal.connect(self.handleRandomWalkFinished)

    def getFilePath(self):
        # Implement the logic to get the file path
        filePath, _ = QFileDialog.getOpenFileName(
            self,
            "选择文件",
            "",
            "文本文件 (*.txt)",
        )

        if filePath:
            self.lineEdit_filePath.setText(filePath)
            self.pushButton_generateFromFile.setEnabled(True)
        else:
            self.lineEdit_filePath.clear()
            self.pushButton_generateFromFile.setEnabled(False)

    def _generateDirectedGraphFromString(self, content: str):
        self.graph.clear()
        for pair in Utils.getAdjWordPair(content):
            word1, word2 = pair
            if self.graph.hasEdge(word1, word2):
                self.graph.increaseEdgeWeight(word1, word2, 1)
            else:
                self.graph.addEdge(word1, word2, 1)
        self.graphInitialized = True

        keys = sorted(self.graph._str_to_int.keys())
        self.comboBox_bridgeStart.clear()
        self.comboBox_bridgeEnd.clear()
        self.comboBox_shortestPathStart.clear()
        self.comboBox_shortestPathEnd.clear()
        self.comboBox_bridgeStart.addItems(keys)
        self.comboBox_bridgeEnd.addItems(keys)
        self.comboBox_shortestPathStart.addItems(keys)
        self.comboBox_shortestPathEnd.addItems(keys)

        self.path = None

        self.plainTextEdit_showGraph.clear()
        self.plainTextEdit_outputBridge.clear()
        self.plainTextEdit_outputNewText.clear()
        self.comboBox_shortestPath.clear()
        self.label_shortestPathCount.setText("路径数：")
        self.plainTextEdit_outputShortestPath.clear()
        self.tableWidget_outputPageRank.clearContents()
        self.tableWidget_outputPageRank.setRowCount(0)
        self.tableWidget_outputPageRank.setColumnCount(0)
        self.tableWidget_outputPageRank.setSortingEnabled(False)
        self.plainTextEdit_outputRandomWalk.clear()

        QMessageBox.information(self, "提示", "图生成成功！")

    def generateDirectedGraphFromFile(self):
        filePath = self.lineEdit_filePath.text()
        file = open(filePath, encoding="utf-8", mode="r")
        if file:
            content = file.read()
            self._generateDirectedGraphFromString(content)

    def generateDirectedGraphFromText(self):
        content = self.plainTextEdit_rawInput.toPlainText()
        if content:
            self._generateDirectedGraphFromString(content)
        else:
            QMessageBox.warning(self, "警告", "请输入文本内容！")

    def showDirectedGraphInImage(
        self,
        highlightedNodes: list[str] = None,
        highlightedPath: list[str] = None,
    ):
        if not self.graphInitialized:
            QMessageBox.warning(self, "警告", "请先生成图！")
            return

        try:
            dot = self.graph.toDigraph(highlightedNodes, highlightedPath)
            dot.render("./temp/temp", format="svg", cleanup=True)
        except Exception as e:
            QMessageBox.critical(self, "错误", f"生成图片失败：{str(e)}")
            return

        dialog = ImageDialog(self, "./temp/temp.svg")
        dialog.exec()

    def showDirectedGraphInText(self):
        if not self.graphInitialized:
            QMessageBox.warning(self, "警告", "请先生成图！")
            return

        # Convert the graph to a string representation
        graph_str = str(self.graph)

        self.plainTextEdit_showGraph.setPlainText(graph_str)

    def saveGraphAsImage(self):
        if not self.graphInitialized:
            QMessageBox.warning(self, "警告", "请先生成图！")
            return

        filePath, _ = QFileDialog.getSaveFileName(
            self,
            "保存图像",
            "",
            "图像文件 (*.png)",
        )

        if filePath:
            try:
                dot = self.graph.toDigraph()
                dot.graph_attr["dpi"] = "400"
                dot.render(filePath.split(".")[0], format="png", cleanup=True)
                QMessageBox.information(self, "提示", "图像保存成功！")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存图像失败：{str(e)}")

    def queryBridgeWords(self):
        if not self.graphInitialized:
            QMessageBox.warning(self, "警告", "请先生成图！")
            return

        start = self.lineEdit_bridgeStart.text()
        end = self.lineEdit_bridgeEnd.text()

        if not start or not end:
            QMessageBox.warning(self, "警告", "请输入起始节点和结束节点！")
            return

        if not (start.isalpha() and end.isalpha()):
            QMessageBox.warning(
                self, "警告", "请输入有效的节点名称！应为纯英文字母"
            )
            return

        exist_start = self.graph.hasNode(start.lower())
        exist_end = self.graph.hasNode(end.lower())

        if not exist_start or not exist_end:
            self.plainTextEdit_outputBridge.setPlainText(
                f'No "{start}" or "{end}" in the graph!'
            )
        else:
            bridges = self.graph.getBridge(start.lower(), end.lower())
            if bridges:
                # The bridge words from "word1" to "word2" are: "xxx", "xxx", and "xxx"
                if len(bridges) == 1:
                    self.plainTextEdit_outputBridge.setPlainText(
                        f'The bridge word from "{start}" to "{end}" is: "{bridges[0]}"!'
                    )
                else:
                    self.plainTextEdit_outputBridge.clear()
                    self.plainTextEdit_outputBridge.insertPlainText(
                        f'The bridge words from "{start}" to "{end}" are: '
                    )
                    for i, word in enumerate(bridges):
                        if i == 0:
                            self.plainTextEdit_outputBridge.insertPlainText(
                                f'"{word}"'
                            )
                        elif i == len(bridges) - 1:
                            self.plainTextEdit_outputBridge.insertPlainText(
                                f' and "{word}"'
                            )
                        else:
                            self.plainTextEdit_outputBridge.insertPlainText(
                                f', "{word}"'
                            )
            else:
                self.plainTextEdit_outputBridge.setPlainText(
                    f'No bridge words from "{start}" to "{end}"!'
                )

    def comboBox_bridgeStart_currentTextChanged(self, text):
        self.lineEdit_bridgeStart.setText(text)

    def comboBox_bridgeEnd_currentTextChanged(self, text):
        self.lineEdit_bridgeEnd.setText(text)

    def comboBox_shortestPathStart_currentTextChanged(self, text):
        self.lineEdit_shortestPathStart.setText(text)

    def comboBox_shortestPathEnd_currentTextChanged(self, text):
        self.lineEdit_shortestPathEnd.setText(text)

    def generateNewText(self):
        """
        根据输入的文本生成新文本
        根据桥接词生成新文本
        """
        input_text = self.plainTextEdit_rawNewInput.toPlainText()

        input_text.replace("\n", " ").replace("\r", " ")
        processed_text = ""
        for char in input_text:
            if char.isalpha() or char == " ":
                processed_text += char
            else:
                processed_text += " "

        words = processed_text.split()

        final_str = ""

        if len(words) == 0:
            QMessageBox.warning(self, "警告", "请输入文本内容！")
            return
        elif len(words) == 1:
            final_str = words[0]
        else:
            for i in range(len(words) - 1):
                final_str += words[i]
                final_str += " "
                res = self.graph.getBridge(
                    words[i].lower(), words[i + 1].lower()
                )
                if res:
                    final_str += random.choice(res)
                    final_str += " "
            final_str += words[-1]

        self.plainTextEdit_outputNewText.setPlainText(final_str)

    def calShortestPath(self):
        if not self.graphInitialized:
            QMessageBox.warning(self, "警告", "请先生成图！")
            return

        start = self.lineEdit_shortestPathStart.text()
        end = self.lineEdit_shortestPathEnd.text()

        to_all = self.checkBox_calcStartToAll.isChecked()

        if not (start and (to_all or end)):
            QMessageBox.warning(self, "警告", "请输入起始节点和结束节点！")
            return

        if not (start.isalpha() and (to_all or end.isalpha())):
            QMessageBox.warning(
                self, "警告", "请输入有效的节点名称！应为纯英文字母"
            )
            return

        if not (
            self.graph.hasNode(start.lower())
            and (to_all or self.graph.hasNode(end.lower()))
        ):
            QMessageBox.warning(
                self, "警告", f'节点 "{start}" 或 "{end}" 不存在！'
            )
            return

        self.path = self.graph.getShortestPath(
            start.lower(),
            None if to_all else end.lower(),
            showMultiPath=self.checkBox_showMultiPath.isChecked(),
        )

        if not self.path:
            QMessageBox.information(
                self,
                "未找到路径",
                (
                    f'没有找到从 "{start}" 到其他节点的路径！'
                    if to_all
                    else f'没有找到从 "{start}" 到 "{end}" 的路径！'
                ),
            )
            return

        self.label_shortestPathCount.setText(f"路径数：{len(self.path)}")
        self.comboBox_shortestPath.clear()
        self.comboBox_shortestPath.addItems(
            [
                f"{i+1}: {self.path[i][1][0]}->{self.path[i][1][-1]}"
                for i in range(len(self.path))
            ]
        )

        QMessageBox.information(
            self,
            "路径计算成功",
            (
                f'从 "{start}" 到所有节点的路径计算成功！'
                if to_all
                else f'从 "{start}" 到 "{end}" 的路径计算成功！'
            ),
        )

    def showShortestPathInImage(self):
        if not self.graphInitialized:
            QMessageBox.warning(self, "警告", "请先生成图！")
            return

        if not self.path:
            QMessageBox.warning(self, "警告", "请先计算路径！")
            return

        index = self.comboBox_shortestPath.currentIndex()
        path = self.path[index][1]
        self.showDirectedGraphInImage(path, path)

    def checkBox_calcStartToAll_stateChanged(self, state):
        if state == 2:
            self.lineEdit_shortestPathEnd.setEnabled(False)
            self.lineEdit_shortestPathEnd.clear()
            self.comboBox_shortestPathEnd.setEnabled(False)
        else:
            self.lineEdit_shortestPathEnd.setEnabled(True)
            self.comboBox_shortestPathEnd.setEnabled(True)

    def comboBox_shortestPath_currentIndexChanged(self, index: int):
        if self.path:
            path = self.path[index]
            self.plainTextEdit_outputShortestPath.setPlainText(
                f"最短路径长度为 {path[0]}: {' -> '.join(path[1])}"
            )
        else:
            self.plainTextEdit_outputShortestPath.clear()

    def calPageRank(self):
        if not self.graphInitialized:
            QMessageBox.warning(self, "警告", "请先生成图！")
            return

        d = self.doubleSpinBox_dampingFactor.value()
        times = self.spinBox_iterationTimes.value()

        if self.radioButton_uniformPageRankStrategy.isChecked():
            strategy = "uniform"
        elif self.radioButton_inDegreePageRankStrategy.isChecked():
            strategy = "in_degree"
        elif self.radioButton_sumIncomingWeightsPageRankStrategy.isChecked():
            strategy = "sum_incoming_weights"

        pageRank = self.graph.getPageRank(d, times, strategy)

        self.tableWidget_outputPageRank.clearContents()
        self.tableWidget_outputPageRank.setSortingEnabled(False)  # 禁用排序
        self.tableWidget_outputPageRank.setRowCount(len(pageRank))
        self.tableWidget_outputPageRank.setColumnCount(2)
        self.tableWidget_outputPageRank.setHorizontalHeaderLabels(
            ["节点", "PR值"]
        )

        for i, (node, pr) in enumerate(pageRank.items()):
            self.tableWidget_outputPageRank.setItem(
                i, 0, QTableWidgetItem(node)
            )
            self.tableWidget_outputPageRank.setItem(
                i, 1, QTableWidgetItem(f"{pr:.15f}")
            )

        self.tableWidget_outputPageRank.setSortingEnabled(True)  # 启用排序

        QMessageBox.information(self, "PageRank计算成功", f"PageRank计算成功！")

    def randomWalk(self):
        # 此函数在主 GUI 线程中运行
        if not self.graphInitialized:
            # 在 GUI 线程中显示消息框
            QMessageBox.warning(
                None, "警告", "请先生成图！"
            )  # 如果在类中，可以传递 self 作为父控件
            return

        # 在开始工作线程之前，在 GUI 线程中更新状态
        self.plainTextEdit_outputRandomWalk.clear()
        self.tab_1.setEnabled(False)
        self.tab_2.setEnabled(False)
        self.tab_3.setEnabled(False)
        self.tab_4.setEnabled(False)
        self.tab_5.setEnabled(False)
        self.tab_6.setEnabled(False)
        self.pushButton_startRandomWalk.setEnabled(False)
        self.pushButton_stopRandomWalk.setEnabled(True)
        self.spinBox_randomWalkSpeed.setEnabled(False)

        speed = self.spinBox_randomWalkSpeed.value()

        # 创建并启动 QRunnable
        walking = QRunnable.create(lambda: self._doRandomWalk(speed))
        walking.setAutoDelete(True)
        pool = QThreadPool.globalInstance()
        pool.start(walking)

    def _doRandomWalk(self, speed: int):

        # 此方法在工作线程中运行！
        # 切勿在此直接访问 GUI 元素。

        with QMutexLocker(self.mutex):
            self.stopWalk = False  # 初始化停止标志

        try:  # 使用 try 块确保即使发生错误，完成信号也能被发射
            current = random.choice(list(self.graph._str_to_int.keys()))
            walked_edges = set()

            # 发射信号来追加初始节点文本 (通知 GUI 线程)
            self.update_text_signal.emit(current, True)

            while True:
                # 检查停止标志，使用互斥锁确保线程安全
                with QMutexLocker(self.mutex):
                    if self.stopWalk:
                        # 停止标志被设置，退出循环
                        break

                next_nodes = self.graph.getSuccessor(current)
                if not next_nodes:
                    # 没有后续节点，漫步结束
                    break

                next_node = random.choice(next_nodes)
                # 发射信号来追加下一个节点文本 (通知 GUI 线程)
                self.update_text_signal.emit(next_node, False)

                # 检查是否形成循环
                if (current, next_node) in walked_edges:
                    break
                else:
                    walked_edges.add((current, next_node))
                    current = next_node

                # 在工作线程中使用 time.sleep 实现延迟
                time.sleep(1.0 / speed)  # 休眠 200 毫秒

        finally:
            # 无论循环是正常结束还是因 break 退出，此 finally 块都会执行
            # 发射信号通知漫步完成 (通知 GUI 线程更新按钮状态)
            self.walk_finished_signal.emit()
            # 在这里重置 stopWalk 标志，因为漫步确实结束了
            with QMutexLocker(self.mutex):
                self.stopWalk = False

    def stopRandomWalk(self):
        # 此方法在主 GUI 线程中运行
        # 使用互斥锁安全地修改共享标志
        with QMutexLocker(self.mutex):
            self.stopWalk = True  # 设置停止标志，工作线程会检测到并退出循环

    def appendRandomWalkText(self, text: str, is_first: bool):
        self.plainTextEdit_outputRandomWalk.insertPlainText(
            text if is_first else f" {text}"
        )

    def handleRandomWalkFinished(self):
        # 在 GUI 线程中更新状态
        self.tab_1.setEnabled(True)
        self.tab_2.setEnabled(True)
        self.tab_3.setEnabled(True)
        self.tab_4.setEnabled(True)
        self.tab_5.setEnabled(True)
        self.tab_6.setEnabled(True)
        self.pushButton_startRandomWalk.setEnabled(True)
        self.pushButton_stopRandomWalk.setEnabled(False)
        self.spinBox_randomWalkSpeed.setEnabled(True)
        # stopWalk 标志已在 _doRandomWalk 的 finally 块中重置

        QMessageBox.information(self, "提示", "随机游走完成！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
