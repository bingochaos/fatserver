#!/bin/bash

SERVER_ROOT=$(pwd)

export FAT_SERVER_PATH=$SERVER_ROOT/fatserver
export PYTHONPATH=$FAT_SERVER_PATH/Lib:$FAT_SERVER_PATH:$SERVER_ROOT/examples/pingpong

python2.7 $SERVER_ROOT/examples/pingpong/main.py

