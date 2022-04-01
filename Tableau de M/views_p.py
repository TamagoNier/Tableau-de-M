from flask import Flask, render_template, request
import sqlite3 


conn = sqlite3.connect('tableau_mendeleiev.db', check_same_thread=False)
cur = conn.cursor()

app = Flask(__name__)

