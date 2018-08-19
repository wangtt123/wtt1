# -*- coding: utf-8 -*-
import allure
import pytest


class Test:
    @allure.step(title="第一个测试方法")
    @allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_all_001(self):
        allure.attach("test_001_1", "第一个测试方法的步骤描述")
        assert 1


@allure.step(title="第二个测试方法")
@allure.severity(pytest.allure.severity_level.CRITICAL)
def test_all_002(self):
    allure.attach("test_001_2", "第二个测试方法的步骤描述")
    assert 0


@allure.step(title="第三个测试方法")
@allure.severity(pytest.allure.severity_level.NORMAL)
def test_all_003(self):
    allure.attach("test_001_3", "第三个测试方法的步骤描述")
    assert 0


@allure.step(title="第四个测试方法")
@allure.severity(pytest.allure.severity_level.MINOR)
def test_all_004(self):
    allure.attach("test_001_4", "第四个测试方法的步骤描述")
    assert 1


@allure.step(title="第五个测试方法")
@allure.severity(pytest.allure.severity_level.TRIVIAL)
def test_all_005(self):
    allure.attach("test_001_5", "第五个测试方法的步骤描述")
    assert 0
