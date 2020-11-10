import os
import signal
import subprocess

import pytest


@pytest.fixture(scope='module', autouse=True)
def record_video():
    print("----- 开始录屏 -----")
    # command = "scrcpy --record file.mp4"
    # subprocess 可以执行cmd 命令
    ex = subprocess.Popen(['scrcpy', '--record', 'file.mp4'], shell=True)
    #  shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(ex)
    yield
    os.kill(ex.pid, signal.CTRL_C_EVENT)
    print("---- 结束录屏 ----")
