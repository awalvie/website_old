#!/bin/python3

import datetime
x = datetime.date.today()
time = datetime.datetime.now()
time = str(time)
time = time[0:16]
file_title = input("file-title: ")
title = input("Main Title: ")
category = input("Category: ")
filename = str(x) + "-" + file_title + '.md'
description = input("Description: ")
text_to_write = '''---
layout: post
title: {0}
description: {2}
categories: {1}
---
'''.format(title, category, description)

print(text_to_write)

with open(filename, 'w') as file:
    file.write(text_to_write)
