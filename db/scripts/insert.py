#!/usr/bin/env python

'''
The MIT License (MIT)

Copyright (c) 2016 Hirokazu Kiyomaru

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import csv
import sqlite3

conn = sqlite3.connect('cells.db')

csvReader = csv.reader(open('seeds/cells.csv', 'rb'))

sql = u"insert into cells values (?, ?, ?, ?, ?, ?, ?, ?)"
for row in csvReader:
    try:
        conn.execute(sql, (None, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    except:
        pass

conn.commit()

csvReader = csv.reader(open('seeds/links.csv', 'rb'))

sql = u"insert into links values (?, ?, ?, ?)"
for row in csvReader:
    try:
        conn.execute(sql, (None, row[0], row[1], row[2]))
    except:
        pass

conn.commit()

csvReader = csv.reader(open('seeds/contra-links.csv', 'rb'))

sql = u"insert into contra_links values (?, ?, ?, ?)"
for row in csvReader:
    try:
        conn.execute(sql, (None, row[0], row[1], row[2]))
    except:
        pass

conn.commit()

conn.close()
