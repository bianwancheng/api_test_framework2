import logging

from selenium import webdriver


class Logging:
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] - %(name)s - [Line:%(lineno)d] - [%(levelname)s] - %(message)s')
    logger = logging.getLogger(__name__)

    @staticmethod
    def info(msg):
        Logging.logger.info(msg)

    @staticmethod
    def error(msg):
        Logging.error(msg)

    @staticmethod
    def debug(msg):
        Logging.debug(msg)

    @staticmethod
    def warning(msg):
        Logging.warning(msg)


if __name__ == '__main__':
    # Logging.info('af')
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    # driver.find_element_by_xpath('')