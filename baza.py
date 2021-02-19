# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import os
import mysql.connector
#import pymysql


import pymysql

conn = pymysql.connect(host = 'localhost', user ='root', password ='Savakiran03', database = 'kontakty', charset='utf8') # 1234 HASLO
c = conn.cursor()
print('połączenie ustanowione!')

