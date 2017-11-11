import webbrowser

def open_file(fileName):
    """用浏览器打开指定文件
    :param fileName: 文件名
    """
    webbrowser.open('file:' + fileName)
