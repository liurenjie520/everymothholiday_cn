import logging

# 获取logger对象,取名mylog
logger = logging.getLogger("mylog")
    # 输出DEBUG及以上级别的信息，针对所有输出的第一层过滤
logger.setLevel(level=logging.DEBUG)

    # 获取文件日志句柄并设置日志级别，第二层过滤
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)

    # 生成并设置文件日志格式，其中name为上面设置的mylog
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

    # 获取流句柄并设置日志级别，第二层过滤
console = logging.StreamHandler()
console.setLevel(logging.WARNING)

    # 为logger对象添加句柄
logger.addHandler(handler)
logger.addHandler(console)

def info(info):
    info=info


    # 记录info日志
    logger.info(info)
    return '记录warning日志ok'


def debug(debug):
    debug=debug


    # 记录debug日志
    logger.debug(debug)
    return '记录warning日志ok'

def warning(warning):
    warning = warning

    # 记录warning日志
    logger.warning(warning)
    return '记录warning日志ok'




