import unittest
from selenium import webdriver
import time
from BeautifulReport import BeautifulReport as bf
import HTMLTestRunner

mainpage = "http://sahitest.com/demo/index.htm"
linktable = ["Link Test","Select Test", "Table Test"]

class testclick(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        print(cls.driver.title)
        cls.driver.get(mainpage)

    def test_click(self):
        for link in linktable:
            with self.subTest(link=link):
                # 当我点击了之后self.driver就跳转到了另外一个页面了
                link_ele = self.driver.find_element_by_link_text(link)
                link_ele.click()
                # time.sleep(1)
                self.assertEqual(1,1)
                self.driver.back()

    # 这里采用了子测试，使得循环中的每一个条件或者参数都能被测试到
    def test_Names(self):
        links = self.driver.find_elements_by_css_selector('a')
        for link in links:
            with self.subTest(link=link):
                flag = self.check_name(link.text)
                self.assertTrue(flag)

    def check_name(self, str):
        return str.istitle() 
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    smoke_test = unittest.TestSuite()
    testsuit1 = unittest.TestLoader().loadTestsFromTestCase(testclick)
    smoke_test.addTest(testsuit1)
    unittest.TextTestRunner(verbosity=2).run(smoke_test)

    # beautifulrunner和HTMLTestRunner都不支持subtest，在subtest中抛出异常之后无法捕获异常信息而且runner程序无法正常终止
    '''
    run = bf(testsuit1)
    run.report(filename="unitest_selenium_report",description="the first beautuful report!")
    '''
    '''
    reportpath = "./report.html"
    fp = open(reportpath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",verbosity=2,description=u"第一个报告")
    runner.run(smoke_test)
    fp.close()
    '''
