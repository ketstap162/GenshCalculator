# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from cgitb import text
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setAutoFillBackground(False)
        self.MainWidget.setStyleSheet("image: url(:/images/images/background1.png);")
        self.MainWidget.setObjectName("MainWidget")
        self.ATK = QtWidgets.QLabel(self.MainWidget)
        self.ATK.setGeometry(QtCore.QRect(40, 30, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.ATK.setFont(font)
        self.ATK.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.ATK.setObjectName("ATK")
        self.DEF = QtWidgets.QLabel(self.MainWidget)
        self.DEF.setGeometry(QtCore.QRect(40, 110, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.DEF.setFont(font)
        self.DEF.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.DEF.setObjectName("DEF")
        self.HP = QtWidgets.QLabel(self.MainWidget)
        self.HP.setGeometry(QtCore.QRect(40, 190, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.HP.setFont(font)
        self.HP.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.HP.setObjectName("HP")
        self.Percent = QtWidgets.QLabel(self.MainWidget)
        self.Percent.setGeometry(QtCore.QRect(170, 30, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.Percent.setFont(font)
        self.Percent.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.Percent.setObjectName("Percent")
        self.Percent_2 = QtWidgets.QLabel(self.MainWidget)
        self.Percent_2.setGeometry(QtCore.QRect(170, 110, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.Percent_2.setFont(font)
        self.Percent_2.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.Percent_2.setObjectName("Percent_2")
        self.Percent_3 = QtWidgets.QLabel(self.MainWidget)
        self.Percent_3.setGeometry(QtCore.QRect(170, 190, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.Percent_3.setFont(font)
        self.Percent_3.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.Percent_3.setObjectName("Percent_3")
        self.Yunka_df = QtWidgets.QLabel(self.MainWidget)
        self.Yunka_df.setGeometry(QtCore.QRect(40, 290, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.Yunka_df.setFont(font)
        self.Yunka_df.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.Yunka_df.setObjectName("Yunka_df")
        self.Percent_4 = QtWidgets.QLabel(self.MainWidget)
        self.Percent_4.setGeometry(QtCore.QRect(170, 290, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.Percent_4.setFont(font)
        self.Percent_4.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.Percent_4.setObjectName("Percent_4")
        self.Shenka_atk = QtWidgets.QLabel(self.MainWidget)
        self.Shenka_atk.setGeometry(QtCore.QRect(40, 370, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.Shenka_atk.setFont(font)
        self.Shenka_atk.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.Shenka_atk.setObjectName("Shenka_atk")
        self.Percent_5 = QtWidgets.QLabel(self.MainWidget)
        self.Percent_5.setGeometry(QtCore.QRect(170, 370, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.Percent_5.setFont(font)
        self.Percent_5.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.Percent_5.setObjectName("Percent_5")
        self.add_sk = QtWidgets.QLabel(self.MainWidget)
        self.add_sk.setGeometry(QtCore.QRect(40, 450, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.add_sk.setFont(font)
        self.add_sk.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.add_sk.setObjectName("add_sk")
        self.Percent_6 = QtWidgets.QLabel(self.MainWidget)
        self.Percent_6.setGeometry(QtCore.QRect(170, 450, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.Percent_6.setFont(font)
        self.Percent_6.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.Percent_6.setObjectName("Percent_6")
        self.Crit_ch = QtWidgets.QLabel(self.MainWidget)
        self.Crit_ch.setGeometry(QtCore.QRect(330, 30, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.Crit_ch.setFont(font)
        self.Crit_ch.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.Crit_ch.setObjectName("Crit_ch")
        self.Crit_dmg = QtWidgets.QLabel(self.MainWidget)
        self.Crit_dmg.setGeometry(QtCore.QRect(460, 30, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.Crit_dmg.setFont(font)
        self.Crit_dmg.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.Crit_dmg.setObjectName("Crit_dmg")
        self.r_full = QtWidgets.QRadioButton(self.MainWidget)
        self.r_full.setGeometry(QtCore.QRect(330, 130, 111, 30))
        self.r_full.setAccessibleDescription("")
        self.r_full.setAutoFillBackground(False)
        self.r_full.setStyleSheet("font: 10pt \"Arial\";\nimage: clear")
        self.r_full.setObjectName("r_full")
        self.React = QtWidgets.QLabel(self.MainWidget)
        self.React.setGeometry(QtCore.QRect(330, 110, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.React.setFont(font)
        self.React.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.React.setObjectName("React")
        self.r_half = QtWidgets.QRadioButton(self.MainWidget)
        self.r_half.setGeometry(QtCore.QRect(330, 160, 200, 30))
        self.r_half.setAccessibleDescription("")
        self.r_half.setAutoFillBackground(False)
        self.r_half.setStyleSheet("font: 10pt \"Arial\";\nimage: clear")
        self.r_half.setObjectName("r_half")
        self.r_none = QtWidgets.QRadioButton(self.MainWidget)
        self.r_none.setEnabled(True)
        self.r_none.setChecked(True)
        self.r_none.setGeometry(QtCore.QRect(330, 190, 200, 30))
        self.r_none.setAccessibleDescription("")
        self.r_none.setAutoFillBackground(False)
        self.r_none.setStyleSheet("font: 10pt \"Arial\";\nimage: clear")
        self.r_none.setObjectName("r_none")
        self.Witch_check = QtWidgets.QCheckBox(self.MainWidget)
        self.Witch_check.setGeometry(QtCore.QRect(330, 220, 70, 50))
        self.Witch_check.setStyleSheet("image: clear")
        self.Witch_check.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/CrimsonWitch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Witch_check.setIcon(icon1)
        self.Witch_check.setIconSize(QtCore.QSize(50, 50))
        self.Witch_check.setObjectName("Witch_check")
        self.rBonus1 = QtWidgets.QLabel(self.MainWidget)
        self.rBonus1.setGeometry(QtCore.QRect(330, 280, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.rBonus1.setFont(font)
        self.rBonus1.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.rBonus1.setObjectName("rBonus1")
        self.dmgB1 = QtWidgets.QLabel(self.MainWidget)
        self.dmgB1.setGeometry(QtCore.QRect(330, 370, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.dmgB1.setFont(font)
        self.dmgB1.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.dmgB1.setObjectName("dmgB1")
        self.line32 = QtWidgets.QFrame(self.MainWidget)
        self.line32.setGeometry(QtCore.QRect(330, 335, 250, 35))
        self.line32.setStyleSheet("image: clear")
        self.line32.setFrameShape(QtWidgets.QFrame.HLine)
        self.line32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line32.setObjectName("line32")
        self.line31 = QtWidgets.QFrame(self.MainWidget)
        self.line31.setGeometry(QtCore.QRect(330, 85, 250, 25))
        self.line31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line31.setObjectName("line31")
        self.dmgB2 = QtWidgets.QLabel(self.MainWidget)
        self.dmgB2.setGeometry(QtCore.QRect(330, 440, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.dmgB2.setFont(font)
        self.dmgB2.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.dmgB2.setObjectName("dmgB2")
        self.line2 = QtWidgets.QFrame(self.MainWidget)
        self.line2.setGeometry(QtCore.QRect(300, 30, 30, 535))
        self.line2.setStyleSheet("color: rgb(0, 0, 0);")
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.dmgB3 = QtWidgets.QLabel(self.MainWidget)
        self.dmgB3.setGeometry(QtCore.QRect(330, 510, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.dmgB3.setFont(font)
        self.dmgB3.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.dmgB3.setObjectName("dmgB3")
        self.line22 = QtWidgets.QFrame(self.MainWidget)
        self.line22.setGeometry(QtCore.QRect(580, 30, 30, 535))
        self.line22.setStyleSheet("image: clear")
        self.line22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line22.setObjectName("line22")
        self.line30 = QtWidgets.QFrame(self.MainWidget)
        self.line30.setGeometry(QtCore.QRect(20, 245, 271, 45))
        self.line30.setStyleSheet("image: clear")
        self.line30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line30.setObjectName("line30")
        self.resist_label = QtWidgets.QLabel(self.MainWidget)
        self.resist_label.setGeometry(QtCore.QRect(610, 30, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.resist_label.setFont(font)
        self.resist_label.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.resist_label.setObjectName("resist_label")
        self.resist_labelR = QtWidgets.QLabel(self.MainWidget)
        self.resist_labelR.setGeometry(QtCore.QRect(740, 30, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.resist_labelR.setFont(font)
        self.resist_labelR.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.resist_labelR.setObjectName("resist_labelR")
        self.lvl1_lab = QtWidgets.QLabel(self.MainWidget)
        self.lvl1_lab.setGeometry(QtCore.QRect(610, 100, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.lvl1_lab.setFont(font)
        self.lvl1_lab.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.lvl1_lab.setObjectName("lvl1_lab")
        self.lvl1_lab_2 = QtWidgets.QLabel(self.MainWidget)
        self.lvl1_lab_2.setGeometry(QtCore.QRect(740, 100, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.lvl1_lab_2.setFont(font)
        self.lvl1_lab_2.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.lvl1_lab_2.setObjectName("lvl1_lab_2")
        self.def_trim_lab = QtWidgets.QLabel(self.MainWidget)
        self.def_trim_lab.setGeometry(QtCore.QRect(610, 200, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.def_trim_lab.setFont(font)
        self.def_trim_lab.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.def_trim_lab.setObjectName("def_trim_lab")
        self.lvl1tip_lab = QtWidgets.QLabel(self.MainWidget)
        self.lvl1tip_lab.setGeometry(QtCore.QRect(610, 155, 120, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lvl1tip_lab.setFont(font)
        self.lvl1tip_lab.setStyleSheet("font: 8pt \"Arial\";\nimage: clear")
        self.lvl1tip_lab.setObjectName("lvl1tip_lab")
        self.lvl2tip_lab = QtWidgets.QLabel(self.MainWidget)
        self.lvl2tip_lab.setGeometry(QtCore.QRect(740, 155, 120, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lvl2tip_lab.setFont(font)
        self.lvl2tip_lab.setStyleSheet("font: 8pt \"Arial\";\nimage: clear")
        self.lvl2tip_lab.setObjectName("lvl2tip_lab")
        self.calc_btn = QtWidgets.QPushButton(self.MainWidget)
        self.calc_btn.setGeometry(QtCore.QRect(610, 515, 180, 50))
        self.calc_btn.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;\nbackground-color: rgb(207, 232, 255);")
        self.calc_btn.setObjectName("calc_btn")
        self.calc_crit = QtWidgets.QLabel(self.MainWidget)
        self.calc_crit.setGeometry(QtCore.QRect(610, 290, 240, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.calc_crit.setFont(font)
        self.calc_crit.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.calc_crit.setObjectName("calc_crit")
        self.calc_line_crit = QtWidgets.QLineEdit(self.MainWidget)
        self.calc_line_crit.setGeometry(QtCore.QRect(610, 310, 240, 35))
        self.calc_line_crit.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.calc_line_crit.setReadOnly(True)
        self.calc_line_crit.setObjectName("calc_line_crit")
        self.calc_dmg = QtWidgets.QLabel(self.MainWidget)
        self.calc_dmg.setGeometry(QtCore.QRect(610, 430, 240, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.calc_dmg.setFont(font)
        self.calc_dmg.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.calc_dmg.setObjectName("calc_dmg")
        self.calc_line_dmg = QtWidgets.QLineEdit(self.MainWidget)
        self.calc_line_dmg.setGeometry(QtCore.QRect(610, 450, 240, 35))
        self.calc_line_dmg.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.calc_line_dmg.setText("")
        self.calc_line_dmg.setReadOnly(True)
        self.calc_line_dmg.setObjectName("calc_line_dmg")
        self.st1_atk = QtWidgets.QLineEdit(self.MainWidget)
        self.st1_atk.setGeometry(QtCore.QRect(40, 50, 120, 35))
        self.st1_atk.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st1_atk.setMaxLength(40)
        self.st1_atk.setReadOnly(False)
        self.st1_atk.setObjectName("st1_atk")
        self.st1_atk_per = QtWidgets.QLineEdit(self.MainWidget)
        self.st1_atk_per.setGeometry(QtCore.QRect(170, 50, 120, 35))
        self.st1_atk_per.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st1_atk_per.setMaxLength(40)
        self.st1_atk_per.setReadOnly(False)
        self.st1_atk_per.setObjectName("st1_atk_per")
        self.st2_df_per = QtWidgets.QLineEdit(self.MainWidget)
        self.st2_df_per.setGeometry(QtCore.QRect(170, 130, 120, 35))
        self.st2_df_per.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st2_df_per.setMaxLength(40)
        self.st2_df_per.setReadOnly(False)
        self.st2_df_per.setObjectName("st2_df_per")
        self.st3_hp_per = QtWidgets.QLineEdit(self.MainWidget)
        self.st3_hp_per.setGeometry(QtCore.QRect(170, 210, 120, 35))
        self.st3_hp_per.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st3_hp_per.setMaxLength(40)
        self.st3_hp_per.setReadOnly(False)
        self.st3_hp_per.setObjectName("st3_hp_per")
        self.st4_Ydf_per = QtWidgets.QLineEdit(self.MainWidget)
        self.st4_Ydf_per.setGeometry(QtCore.QRect(170, 310, 120, 35))
        self.st4_Ydf_per.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st4_Ydf_per.setMaxLength(40)
        self.st4_Ydf_per.setReadOnly(False)
        self.st4_Ydf_per.setObjectName("st4_Ydf_per")
        self.st5_Satk_per = QtWidgets.QLineEdit(self.MainWidget)
        self.st5_Satk_per.setGeometry(QtCore.QRect(170, 390, 120, 35))
        self.st5_Satk_per.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st5_Satk_per.setMaxLength(40)
        self.st5_Satk_per.setReadOnly(False)
        self.st5_Satk_per.setObjectName("st5_Satk_per")
        self.st6_add_per = QtWidgets.QLineEdit(self.MainWidget)
        self.st6_add_per.setGeometry(QtCore.QRect(170, 470, 120, 35))
        self.st6_add_per.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st6_add_per.setMaxLength(40)
        self.st6_add_per.setReadOnly(False)
        self.st6_add_per.setObjectName("st6_add_per")
        self.st2_df = QtWidgets.QLineEdit(self.MainWidget)
        self.st2_df.setGeometry(QtCore.QRect(40, 130, 120, 35))
        self.st2_df.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st2_df.setMaxLength(40)
        self.st2_df.setReadOnly(False)
        self.st2_df.setObjectName("st2_df")
        self.st3_hp = QtWidgets.QLineEdit(self.MainWidget)
        self.st3_hp.setGeometry(QtCore.QRect(40, 210, 120, 35))
        self.st3_hp.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st3_hp.setMaxLength(40)
        self.st3_hp.setReadOnly(False)
        self.st3_hp.setObjectName("st3_hp")
        self.st4_Ydf = QtWidgets.QLineEdit(self.MainWidget)
        self.st4_Ydf.setGeometry(QtCore.QRect(40, 310, 120, 35))
        self.st4_Ydf.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st4_Ydf.setMaxLength(40)
        self.st4_Ydf.setReadOnly(False)
        self.st4_Ydf.setObjectName("st4_Ydf")
        self.st5_Satk = QtWidgets.QLineEdit(self.MainWidget)
        self.st5_Satk.setGeometry(QtCore.QRect(40, 390, 120, 35))
        self.st5_Satk.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st5_Satk.setMaxLength(40)
        self.st5_Satk.setReadOnly(False)
        self.st5_Satk.setObjectName("st5_Satk")
        self.st6_add = QtWidgets.QLineEdit(self.MainWidget)
        self.st6_add.setGeometry(QtCore.QRect(40, 470, 120, 35))
        self.st6_add.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.st6_add.setMaxLength(40)
        self.st6_add.setReadOnly(False)
        self.st6_add.setObjectName("st6_add")
        self.crit_chance = QtWidgets.QLineEdit(self.MainWidget)
        self.crit_chance.setGeometry(QtCore.QRect(330, 50, 120, 35))
        self.crit_chance.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.crit_chance.setMaxLength(40)
        self.crit_chance.setReadOnly(False)
        self.crit_chance.setObjectName("crit_chance")
        self.crit_dmg = QtWidgets.QLineEdit(self.MainWidget)
        self.crit_dmg.setGeometry(QtCore.QRect(460, 50, 120, 35))
        self.crit_dmg.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.crit_dmg.setMaxLength(40)
        self.crit_dmg.setReadOnly(False)
        self.crit_dmg.setObjectName("crit_dmg")
        self.em_bonus = QtWidgets.QLineEdit(self.MainWidget)
        self.em_bonus.setGeometry(QtCore.QRect(330, 300, 120, 35))
        self.em_bonus.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.em_bonus.setMaxLength(40)
        self.em_bonus.setReadOnly(False)
        self.em_bonus.setObjectName("em_bonus")
        self.dmg1 = QtWidgets.QLineEdit(self.MainWidget)
        self.dmg1.setGeometry(QtCore.QRect(330, 390, 120, 35))
        self.dmg1.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.dmg1.setMaxLength(40)
        self.dmg1.setReadOnly(False)
        self.dmg1.setObjectName("dmg1")
        self.dmg2 = QtWidgets.QLineEdit(self.MainWidget)
        self.dmg2.setGeometry(QtCore.QRect(330, 460, 120, 35))
        self.dmg2.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.dmg2.setMaxLength(40)
        self.dmg2.setReadOnly(False)
        self.dmg2.setObjectName("dmg2")
        self.dmg3 = QtWidgets.QLineEdit(self.MainWidget)
        self.dmg3.setGeometry(QtCore.QRect(330, 530, 120, 35))
        self.dmg3.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.dmg3.setMaxLength(40)
        self.dmg3.setReadOnly(False)
        self.dmg3.setObjectName("dmg3")
        self.resist = QtWidgets.QLineEdit(self.MainWidget)
        self.resist.setGeometry(QtCore.QRect(610, 50, 80, 35))
        self.resist.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.resist.setMaxLength(40)
        self.resist.setReadOnly(False)
        self.resist.setObjectName("resist")
        self.resist_red = QtWidgets.QLineEdit(self.MainWidget)
        self.resist_red.setGeometry(QtCore.QRect(740, 50, 80, 35))
        self.resist_red.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.resist_red.setMaxLength(40)
        self.resist_red.setReadOnly(False)
        self.resist_red.setObjectName("resist_red")
        self.enemy_lvl = QtWidgets.QLineEdit(self.MainWidget)
        self.enemy_lvl.setGeometry(QtCore.QRect(610, 120, 80, 35))
        self.enemy_lvl.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.enemy_lvl.setMaxLength(3)
        self.enemy_lvl.setReadOnly(False)
        self.enemy_lvl.setObjectName("enemy_lvl")
        self.char_lvl = QtWidgets.QLineEdit(self.MainWidget)
        self.char_lvl.setGeometry(QtCore.QRect(740, 120, 80, 35))
        self.char_lvl.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.char_lvl.setMaxLength(3)
        self.char_lvl.setReadOnly(False)
        self.char_lvl.setObjectName("char_lvl")
        self.df_red = QtWidgets.QLineEdit(self.MainWidget)
        self.df_red.setGeometry(QtCore.QRect(610, 220, 80, 35))
        self.df_red.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.df_red.setMaxLength(40)
        self.df_red.setReadOnly(False)
        self.df_red.setObjectName("df_red")
        self.line33 = QtWidgets.QFrame(self.MainWidget)
        self.line33.setGeometry(QtCore.QRect(610, 255, 270, 35))
        self.line33.setStyleSheet("image: clear")
        self.line33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line33.setObjectName("line33")
        self.calc_ncrit = QtWidgets.QLabel(self.MainWidget)
        self.calc_ncrit.setGeometry(QtCore.QRect(610, 360, 240, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(False)
        self.calc_ncrit.setFont(font)
        self.calc_ncrit.setStyleSheet("font: 12pt \"Arial\";\nimage: clear")
        self.calc_ncrit.setObjectName("calc_ncrit")
        self.calc_line_ncrit = QtWidgets.QLineEdit(self.MainWidget)
        self.calc_line_ncrit.setGeometry(QtCore.QRect(610, 380, 240, 35))
        self.calc_line_ncrit.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;")
        self.calc_line_ncrit.setReadOnly(True)
        self.calc_line_ncrit.setObjectName("calc_line_ncrit")
        self.clear_btn = QtWidgets.QPushButton(self.MainWidget)
        self.clear_btn.setGeometry(QtCore.QRect(800, 515, 50, 50))
        self.clear_btn.setStyleSheet("font: 12pt \"Arial\";\nimage: clear;\nbackground-color: rgb(255, 199, 199);")
        self.clear_btn.setObjectName("clear_btn")
        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.go_calc()
        self.go_clear()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "zGensh Calculator"))
        self.ATK.setText(_translate("MainWindow", "ATK"))
        self.DEF.setText(_translate("MainWindow", "DEF"))
        self.HP.setText(_translate("MainWindow", "HP"))
        self.Percent.setText(_translate("MainWindow", "%"))
        self.Percent_2.setText(_translate("MainWindow", "%"))
        self.Percent_3.setText(_translate("MainWindow", "%"))
        self.Yunka_df.setText(_translate("MainWindow", "Yunka: DEF"))
        self.Percent_4.setText(_translate("MainWindow", "%"))
        self.Shenka_atk.setText(_translate("MainWindow", "Shenhe: ATK"))
        self.Percent_5.setText(_translate("MainWindow", "%"))
        self.add_sk.setText(_translate("MainWindow", "Additional"))
        self.Percent_6.setText(_translate("MainWindow", "%"))
        self.Crit_ch.setText(_translate("MainWindow", "Crit Chance"))
        self.Crit_dmg.setText(_translate("MainWindow", "Crit DMG"))
        self.r_full.setText(_translate("MainWindow", "Melt/Vape"))
        self.React.setText(_translate("MainWindow", "Reactions:"))
        self.r_half.setText(_translate("MainWindow", "Reverse Melt/Vape"))
        self.r_none.setText(_translate("MainWindow", "None/Other"))
        self.rBonus1.setText(_translate("MainWindow", "Bonus from EM"))
        self.dmgB1.setText(_translate("MainWindow", "DMG bonus"))
        self.dmgB2.setText(_translate("MainWindow", "AA, Hold, E or Q bonus"))
        self.dmgB3.setText(_translate("MainWindow", "Elemental/Phys bonus"))
        self.resist_label.setText(_translate("MainWindow", "Resist"))
        self.resist_labelR.setText(_translate("MainWindow", "R. Reduce"))
        self.lvl1_lab.setText(_translate("MainWindow", "Enemy\'s lvl"))
        self.lvl1_lab_2.setText(_translate("MainWindow", "Character lvl"))
        self.def_trim_lab.setText(_translate("MainWindow", "DEF Reduce"))
        self.lvl1tip_lab.setText(_translate("MainWindow", "(Default: 97)"))
        self.lvl2tip_lab.setText(_translate("MainWindow", "(Default: 90)"))
        self.calc_btn.setText(_translate("MainWindow", "Calculate!"))
        self.calc_crit.setText(_translate("MainWindow", "Damage from CRIT HIT:"))
        self.calc_dmg.setText(_translate("MainWindow", "Average Damage:"))
        self.calc_ncrit.setText(_translate("MainWindow", "Damage from NON CRIT"))
        self.clear_btn.setText(_translate("MainWindow", "C"))

    def go_calc(self):
        self.calc_btn.clicked.connect(lambda: self.dmg_calc(
        [
            self.st1_atk.text(),
            self.st1_atk_per.text(),
            self.st2_df.text(),
            self.st2_df_per.text(),
            self.st3_hp.text(),
            self.st3_hp_per.text(),
            self.st4_Ydf.text(),
            self.st4_Ydf_per.text(),
            self.st5_Satk.text(),
            self.st5_Satk_per.text(),
            self.st6_add.text(),
            self.st6_add_per.text(),
        ],

        [
            self.crit_chance.text(),
            self.crit_dmg.text(),
        ],

        [
            self.r_full.isChecked(),
            self.r_half.isChecked(),
            self.r_none.isChecked(),
            self.Witch_check.isChecked(),
            self.em_bonus.text()
        ],

        [
            self.dmg1.text(),
            self.dmg2.text(),
            self.dmg3.text()
        ],

        [
            self.resist.text(),
            self.resist_red.text(),
        ],

        [
            self.enemy_lvl.text(),
            self.char_lvl.text(),
            self.df_red.text()
        ]
        ))
    def dmg_calc(self, l1, l2, l3, l4, l5, l6):
        #print(f'Go! Go! Go!\n{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{l6}')

        self.calc_line_crit.setText('')
        self.calc_line_ncrit.setText('')
        self.calc_line_dmg.setText('')


        a=0
        k31=1
        k32=1
        k4=1
        k5=1
        k6=1
        k7=0.49

        #a
        if l1[0]!='' and l1[1]!='':
            atk=(l1[0]).replace(',', '.')
            atk_per=(l1[1]).replace(',', '.')
            atk_per=atk_per.replace('%', '')

            try:
                a+=(eval(atk))*(eval(atk_per))/100
            except:
                self.calc_line_crit.setText('Error in ATK')
                self.calc_line_ncrit.setText('Error in ATK')
                self.calc_line_dmg.setText('Error in ATK')

        if l1[2]!='' and l1[3]!='':
            df=(l1[2]).replace(',', '.')
            df_per=(l1[3]).replace(',', '.')
            df_per=df_per.replace('%', '')

            try:
                a+=(eval(df))*(eval(df_per))/100
            except:
                self.calc_line_crit.setText('Error in DEF')
                self.calc_line_ncrit.setText('Error in DEF')
                self.calc_line_dmg.setText('Error in DEF')

        if l1[4]!='' and l1[5]!='':
            hp=(l1[4]).replace(',', '.')
            hp_per=(l1[5]).replace(',', '.')
            hp_per=hp_per.replace('%', '')

            try:
                a+=(eval(hp))*(eval(hp_per))/100
            except:
                self.calc_line_crit.setText('Error in HP')
                self.calc_line_ncrit.setText('Error in HP')
                self.calc_line_dmg.setText('Error in HP')

        if l1[6]!='' and l1[7]!='':
            Yunka_df=(l1[6]).replace(',', '.')
            Yunka_per=(l1[7]).replace(',', '.')
            Yunka_per=Yunka_per.replace('%', '')

            try:
                a+=(eval(Yunka_df))*(eval(Yunka_per))/100
            except:
                self.calc_line_crit.setText('Error in YUNKA')
                self.calc_line_ncrit.setText('Error in YUNKA')
                self.calc_line_dmg.setText('Error in YUNKA')
        
        if l1[8]!='' and l1[9]!='':
            Shenhe_atk=(l1[8]).replace(',', '.')
            Shenhe_per=(l1[9]).replace(',', '.')
            Shenhe_per=Shenhe_per.replace('%', '')

            try:
                a+=(eval(Shenhe_atk))*(eval(Shenhe_per))/100
            except:
                self.calc_line_crit.setText('Error in SHENHE')
                self.calc_line_ncrit.setText('Error in SHENHE')
                self.calc_line_dmg.setText('Error in SHENHE')
        
        if l1[10]!='' and l1[11]!='':
            add_st=(l1[10]).replace(',', '.')
            add_per=(l1[11]).replace(',', '.')
            add_per=add_per.replace('%', '')

            try:
                a+=(eval(add_st))*(eval(add_per))/100
            except:
                self.calc_line_crit.setText('Error in ADD')
                self.calc_line_ncrit.setText('Error in ADD')
                self.calc_line_dmg.setText('Error in ADD')
        #k31 k32
        if l2[1]!='':
            crit_chance=(l2[0]).replace(',', '.')
            crit_chance=crit_chance.replace('%', '')
            if crit_chance=='':
                crit_chance='0'
            
            crit_dmg=(l2[1]).replace(',', '.')
            crit_dmg=crit_dmg.replace('%', '')

            try:
                crit_chance=eval(crit_chance)
                crit_dmg=eval(crit_dmg)
                if crit_chance>100:
                    crit_chance=100
                elif crit_chance<0:
                    crit_chance=0
                k31=1+(crit_dmg/100)
                k32=1+((crit_dmg*crit_chance/100)/100)
            except:
                self.calc_line_crit.setText('Error in CRIT')
                self.calc_line_ncrit.setText('Error in CRIT')
                self.calc_line_dmg.setText('Error in CRIT')
            
        #k4
        if l3[0]==True:
            em_bonus=0
            if l3[3]==True:
                em_bonus+=15
            if l3[4]!='':
                try:
                    em=l3[4].replace(',', '.')
                    em=em.replace('%', '')
                    em_bonus=eval(em)
                except:
                    self.calc_line_crit.setText('Error in REACT')
                    self.calc_line_ncrit.setText('Error in REACT')
                    self.calc_line_dmg.setText('Error in REACT')
            k4=2*(100+em_bonus)/100 
      
        elif l3[1]==True:
            em_bonus=0
            if l3[3]==True:
                em_bonus+=15
            if l3[4]!='':
                try:
                    em=l3[4].replace(',', '.')
                    em=em.replace('%', '')
                    em_bonus=eval(em)
                except:
                    self.calc_line_crit.setText('Error in REACT')
                    self.calc_line_ncrit.setText('Error in REACT')
                    self.calc_line_dmg.setText('Error in REACT') 
            k4=1.5*(100+em_bonus)/100
        #k5
        if l4[0]!='':
            dmg_bonus1=l4[0].replace(',', '.')
            dmg_bonus1=dmg_bonus1.replace('%', '')
            try:
                k5+=eval(dmg_bonus1)/100
            except:
                self.calc_line_crit.setText('Error in DMG BONUS')
                self.calc_line_ncrit.setText('Error in DMG BONUS')
                self.calc_line_dmg.setText('Error in DMG BONUS') 
        if l4[1]!='':
            dmg_bonus2=l4[1].replace(',', '.')
            dmg_bonus2=dmg_bonus2.replace('%', '')
            try:
                k5+=eval(dmg_bonus2)/100
            except:
                self.calc_line_crit.setText('Error in SKILL BONUS')
                self.calc_line_ncrit.setText('Error in SKILL BONUS')
                self.calc_line_dmg.setText('Error in SKILL BONUS') 
        if l4[2]!='':
            dmg_bonus3=l4[2].replace(',', '.')
            dmg_bonus3=dmg_bonus3.replace('%', '')
            try:
                k5+=eval(dmg_bonus3)/100
            except:
                self.calc_line_crit.setText('Error in E/Ph BONUS')
                self.calc_line_ncrit.setText('Error in E/Ph BONUS')
                self.calc_line_dmg.setText('Error in E/Ph BONUS') 
        #k6
        if l5[0]!='':
            resist=l5[0].replace(',','.')
            resist=resist.replace('%','')
            try:
                k6-=eval(resist)/100
            except:
                self.calc_line_crit.setText('Error in RESISTs')
                self.calc_line_ncrit.setText('Error in RESISTs')
                self.calc_line_dmg.setText('Error in RESISTs') 
        if l5[1]!='':
            resist_red=l5[1].replace(',','.')
            resist_red=resist_red.replace('%','')
            try:
                k6+=eval(resist_red)/100
            except:
                self.calc_line_crit.setText('Error in R.REDUCE')
                self.calc_line_ncrit.setText('Error in R.REDUCE')
                self.calc_line_dmg.setText('Error in R.REDUCE') 
        if k6>1:
            k6=1+(k6-1)/2
        

        #k7
        enemy_lvl=97
        if l6[0]!='':
            try:
                enemy_lvl=int(l6[0])
            except:
                self.calc_line_crit.setText('Error in EnemyLVL')
                self.calc_line_ncrit.setText('Error in EnemyLVL')
                self.calc_line_dmg.setText('Error in EnemyLVL')
            
        char_lvl=90
        if l6[1]!='':
            try:
                char_lvl=int(l6[1])
            except:
                self.calc_line_crit.setText('Error in CharLVL')
                self.calc_line_ncrit.setText('Error in CharLVL')
                self.calc_line_dmg.setText('Error in CharLVL')

        if l6[2]!='':
            try:
                df_red=l6[2].replace(',', '.')
                df_red=df_red.replace('%', '')
                df_red=eval(df_red)
            except:
                self.calc_line_crit.setText('Error in DefRED')
                self.calc_line_ncrit.setText('Error in DefRED')
                self.calc_line_dmg.setText('Error in DefRED')
        else:
            df_red=0
        if type(char_lvl)!=str and type(enemy_lvl)==int and type(df_red)!=str:
            k7=(char_lvl+100)/((enemy_lvl+100)*((100-df_red)/100)+(char_lvl+100))

        dmg_crit=round(a*k31*k4*k5*k6*k7)
        dmg_ncrit=round(a*k4*k5*k6*k7)
        dmg_avarage=round(a*k32*k4*k5*k6*k7)

        print(f'''
            {a}
            {k31}
            {k32}
            {k4}
            {k5}
            {k6}
            {k7}
            ''')


        if 'Error' not in self.calc_line_crit.text():
            self.calc_line_crit.setText(f'{dmg_crit}')
            self.calc_line_ncrit.setText(f'{dmg_ncrit}')
            self.calc_line_dmg.setText(f'{dmg_avarage}')

    def go_clear(self):
        self.clear_btn.clicked.connect(lambda: self.clearing())
    def clearing(self):
        self.st1_atk.setText('')
        self.st1_atk_per.setText('')
        self.st2_df.setText('')
        self.st2_df_per.setText('')
        self.st3_hp.setText('')
        self.st3_hp_per.setText('')
        self.st4_Ydf.setText('')
        self.st4_Ydf_per.setText('')
        self.st5_Satk.setText('')
        self.st5_Satk_per.setText('')
        self.st6_add.setText('')
        self.st6_add_per.setText('')
      
        self.crit_chance.setText('')
        self.crit_dmg.setText('')

        self.r_none.setChecked(True)
        self.Witch_check.setChecked(False)
        self.em_bonus.setText('')

        self.dmg1.setText('')
        self.dmg2.setText('')
        self.dmg3.setText('')
 
        self.resist.setText('')
        self.resist_red.setText('')

        self.enemy_lvl.setText('')
        self.char_lvl.setText('')
        self.df_red.setText('')

        self.calc_line_crit.setText(f'')
        self.calc_line_ncrit.setText(f'')
        self.calc_line_dmg.setText(f'')


        #print(f'a={a}\nk31={k31}\nk32={k32}\nk4={k4}\nk5={k5}\nk6={k6}\nk7={k7}\n')

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())