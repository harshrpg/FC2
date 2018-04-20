#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `FC2` package."""
import sys
sys.path.append('.')

import pytest

from click.testing import CliRunner
from FC2 import cli
from FC2 import linkList

def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main,['./data/testroutes.csv'])
    # assert result.exit_code == 0
    assert "./data/testroutes.csv" in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

def test_linkList():
    _linkList = linkList.LinkList()
    _linkList.addNode([0,45])
    _linkList.addNode([1,45])
    _linkList.addNode([2,45])
    result1 = _linkList.getHead()
    result2 = _linkList.getNode(1)
    _linkList.removeNode([1,45])
    result3 = _linkList.getList()
    assert [0,45] == result1
    assert [1,45] == result2
    assert [[0,45],[2,45]] == result3
    _linkList.removeNode([1, 45])
    result4 = _linkList.getList()
    assert [[0,45],[2,45]] == result3
