from PySide2 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication()
my_widget = QtWidgets.QWidget()
my_widget.show()
my_widget.setWindowTitle("Shipping Payment")
my_widget.resize(370,310)

my_label_1 = QtWidgets.QLabel("Full Name")
my_label_1.setParent(my_widget)
my_label_1.show()
my_label_1.setGeometry(25,1,100,50)
my_input_field_1 = QtWidgets.QLineEdit()
my_input_field_1.setParent(my_widget)
my_input_field_1.setGeometry(5,40,100,20)
my_input_field_1.show()
my_input_field_1.setPlaceholderText("同護照姓名")

my_label_2 = QtWidgets.QLabel("Email")
my_label_2.setParent(my_widget)
my_label_2.show()
my_label_2.setGeometry(160,1,100,50)
my_input_field_2 = QtWidgets.QLineEdit()
my_input_field_2.setParent(my_widget)
my_input_field_2.setGeometry(115,40,125,20)
my_input_field_2.show()

my_label_3 = QtWidgets.QLabel("Phone")
my_label_3.setParent(my_widget)
my_label_3.show()
my_label_3.setGeometry(280,1,100,50)
my_input_field_3 = QtWidgets.QLineEdit()
my_input_field_3.setParent(my_widget)
my_input_field_3.setGeometry(250,40,100,20)
my_input_field_3.show()
my_input_field_3.setPlaceholderText("09xxxxxxxx")

my_label_4 = QtWidgets.QLabel("Address")
my_label_4.setParent(my_widget)
my_label_4.show()
my_label_4.setGeometry(100,50,100,50)
my_input_field_4 = QtWidgets.QLineEdit()
my_input_field_4.setParent(my_widget)
my_input_field_4.setGeometry(5,85,230,20)
my_input_field_4.show()

my_label_5 = QtWidgets.QLabel("Zip Code")
my_label_5.setParent(my_widget)
my_label_5.show()
my_label_5.setGeometry(275,50,100,50)
my_input_field_5 = QtWidgets.QLineEdit()
my_input_field_5.setParent(my_widget)
my_input_field_5.setGeometry(250,85,100,20)
my_input_field_5.show()

my_label_6 = QtWidgets.QLabel("City")
my_label_6.setParent(my_widget)
my_label_6.show()
my_label_6.setGeometry(88,95,100,50)
combobox = QtWidgets.QComboBox()
combobox.setParent(my_widget)
combobox.setGeometry(38,130,120,20)
combobox.show()
combobox.addItem("台北市")
combobox.addItem("桃園市")
combobox.addItem("台中市")

my_label_7 = QtWidgets.QLabel("Country")
my_label_7.setParent(my_widget)
my_label_7.show()
my_label_7.setGeometry(218,95,100,50)
combobox2 = QtWidgets.QComboBox()
combobox2.setParent(my_widget)
combobox2.setGeometry(180,130,120,20)
combobox2.show()
combobox2.addItem("台灣")
combobox2.addItem("香港")
combobox2.addItem("日本")

my_label_8 = QtWidgets.QLabel("Card Number")
my_label_8.setParent(my_widget)
my_label_8.show()
my_label_8.setGeometry(35,155,100,50)
my_input_field_8 = QtWidgets.QLineEdit()
my_input_field_8.setParent(my_widget)
my_input_field_8.setGeometry(5,190,135,20)
my_input_field_8.show()
my_input_field_8.setPlaceholderText("0123-xxxx-xxxx-xxxx")

my_label_9 = QtWidgets.QLabel("Expiry(mm/YY)")
my_label_9.setParent(my_widget)
my_label_9.show()
my_label_9.setGeometry(160,155,150,50)
my_input_field_9 = QtWidgets.QLineEdit()
my_input_field_9.setParent(my_widget)
my_input_field_9.setGeometry(165,190,80,20)
my_input_field_9.show()
my_input_field_9.setPlaceholderText("12/20")

my_label_10 = QtWidgets.QLabel("cvv")
my_label_10.setParent(my_widget)
my_label_10.show()
my_label_10.setGeometry(302,155,150,50)
my_input_field_10 = QtWidgets.QLineEdit()
my_input_field_10.setParent(my_widget)
my_input_field_10.setGeometry(280,190,65,20)
my_input_field_10.show()
my_input_field_10.setPlaceholderText("***")
my_input_field_10.setEchoMode(QtWidgets.QLineEdit.Password)


def get_value():
    print(my_input_field_1.text())
    print(my_input_field_2.text())
    print(my_input_field_3.text())
    print(my_input_field_4.text())
    print(my_input_field_5.text())
    print(combobox.currentText())
    print(combobox2.currentText())
    print(my_input_field_9.text())
    print(my_input_field_10.text())


my_button = QtWidgets.QPushButton("SUBMIT")
my_button.setParent(my_widget)
my_button.setGeometry(135,240,105,50)
my_button.show()
my_button.clicked.connect(get_value)


sys.exit(app.exec_())