#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-19 19:03
# @Author  : lamber
# @Site    : dcgamer.top
# @File    : ser.py
# @Software: PyCharm
from rest_framework import serializers
from snippet.models import LEXERS, STYLE_CHOICES, LANGUAGE_CHOICES


class SnippetSerializer(serializers.Serializer):



