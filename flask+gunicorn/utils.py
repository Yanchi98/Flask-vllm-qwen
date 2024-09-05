import os


def get_root_path():
    # 获取当前脚本所在的目录
    current_path = os.path.dirname(os.path.abspath(__file__))

    # 获取当前脚本所在的项目根目录
    root_path = os.path.dirname(current_path)

    return root_path
