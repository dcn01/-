# -*- coding: utf-8 -*-

# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

# Connects to the current device, returning a MonkeyDevice object
#����һ���������������ó�ʱʱ��10s
device = mr.waitForConnection(10)
#device = mr.waitForConnection(30,'123123135002735')

# press menu
#device.press('KEYCODE_MENU', md.DOWN_AND_UP)


#��װapk��
#Ԥ����Դʱ��������װ
def installAPK(apkName):
	#device.installPackage('D:/Yahoo Mail.apk'.decode('utf-8'))
	device.installPackage('D:/SubwaySurf.apk'.decode('utf-8'))
	device.installPackage('D:/psiphon3.apk'.decode('utf-8'))
	print 'finish install'

'''
����ж��apk��Ҫ֪��apk����
com.psiphon3
'''
def removeAPK(packageName):
	device.removePackage('com.psiphon3')
	device.removePackage('com.kiloo.subwaysurf')	
	print 'finish uninstall'
	
#�϶��������ĸ�������ǰ�����ǳ�ʼ�㡢���������꣬0.5�ǳ���ʱ�䣬1�ǲ���
def drag(start,end,duration,step):
	device.drag((100,500),(550,500), 0.0, 1)

#����־������ⲿ�ļ�,��python��ʹ�����ģ���Ҫ���ļ���ͷ����������Ϊutf-8,��������
log = open('d:/monkenyLog.txt', 'w')
log.write('�ȴ��ֻ�')
log.close()

installAPK('')
#removeAPK('')

