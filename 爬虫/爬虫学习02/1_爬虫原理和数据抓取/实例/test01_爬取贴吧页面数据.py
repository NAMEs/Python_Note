from urllib import request, parse
import os

def url_splice(url, keyword):
    """
    作用：拼接url
    :param url: 贴吧的url
    :param keyword: 想要搜索的关键字
    :return: 返回拼接后的url
    """
    kw = {"kw": keyword}
    kw = parse.urlencode(kw)

    url = url + kw

    return url


def tieba_spider(url, start_page, end_page, foldername):
    """
    作用：处理url，将每个url分别发送请求
    :param url:
    :param start_page: 开始页面
    :param end_page: 结束页面
    :return:none
    """

    for page in range(start_page, end_page + 1):
        pn = (page-1)*50

        filename = "第"+str(page)+"页"+".html"
        file_path = "../html/"+foldername+"/"+filename
        folder = "../html/"+foldername+"/"

        # 如果文件夹不存在，则创建该文件夹
        if os.path.exists(folder) is False:
            os.mkdir(folder)

        full_url = url + "&pn=" + str(pn)

        html = load_page(full_url, file_path)

        write_file(html, file_path)


def load_page(url, file_path):
    """
    作用：加载页面
    :param url: 页面的url
    :param file_path: 文件路径
    :return: 返回html页面
    """
    req = request.Request(url)
    print("正在加载:{0}".format(file_path))
    html = request.urlopen(req).read().decode()

    return html


def write_file(html, file_path):
    """
    作用：将html文件写到本地
    :param html: html文件
    :param file_path: 要写入的文件路径
    :return: none
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("下载完成:{}".format(file_path))


if __name__ == "__main__":
    url = "http://tieba.baidu.com/f?"
    name = input("请输入贴吧名：")
    start_page = input("请输入开始页数:")
    end_page = input("请输入结束页数:")

    url = url_splice(url, name)

    tieba_spider(url, int(start_page), int(end_page), name)
