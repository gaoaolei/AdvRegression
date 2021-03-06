import unittest
import paramunittest
from OperateExcel import ReadExcel
# from GetMysqlData import *
from GetAPIData import *
# from tools import *
# import GetPath
# import time
import warnings

xls = ReadExcel().get_xls('user_data.xlsx', 'Regression')
area_config_id = 51
url = "https://api-ks.wtzw.com/api/v1/reader-adv"


@paramunittest.parametrized(*xls)
class TestAdvVideoList(unittest.TestCase):
    def setParameters(self, order, platform, app_version, channel, device_id, net_env, sys_ver):
        """excel见了整数，小数就是float，其他大致都是str"""
        self.order = int(order)
        self.platform = int(platform)
        self.app_version = int(app_version)
        self.channel = channel
        self.device_id = device_id
        self.net_env = int(net_env)
        self.sys_ver = sys_ver

    def setUp(self):
        """忽略ResourceWarning"""
        warnings.simplefilter('ignore', ResourceWarning)

        """获取接口数据"""
        response = get_api_data(url, self.net_env, self.channel, self.sys_ver, self.device_id, self.platform,
                                self.app_version)
        self.api_data = response['data']['video_list']

    def test_null_duration(self):
        self.assertNotEqual(self.api_data['duration'], [])

    def test_null_feedback(self):
        self.assertNotEqual(self.api_data['feedback'], [])

    @unittest.skip
    def test_null_reader_getcoin(self):
        pass

    @unittest.skip
    def test_null_reader_inchapter(self):
        pass

    @unittest.skip
    def test_null_reader_scroll(self):
        pass

    def tearDown(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()
