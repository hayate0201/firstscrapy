# -*- coding: utf-8 -*-  
#---------------------------------------  
#   ���򣺰ٶ���������  
#   �汾��0.1  
#   ���ߣ�why  
#   ���ڣ�2013-05-14  
#   ���ԣ�Python 2.7  
#   �������������ҳ�ĵ�ַ��ȥ�����������֣�����һ����ʼҳ�����յ�ҳ����  
#   ���ܣ����ض�Ӧҳ���ڵ�����ҳ�沢�洢Ϊhtml�ļ���  
#---------------------------------------  
   
import string, urllib2  
   
#����ٶȺ���  
def baidu_tieba(url,begin_page,end_page):     
    for i in range(begin_page, end_page+1):  
        sName = string.zfill(i,5) + '.html'#�Զ�������λ���ļ���  
        print '�������ص�' + str(i) + '����ҳ��������洢Ϊ' + sName + '......'  
        f = open(sName,'w+')  
        m = urllib2.urlopen(url + str(i)).read()  
        f.write(m)  
        f.close()  
   
   
#-------- ������������� ------------------  
  
# �����ɽ����ѧ�İٶ�������ĳһ�����ӵĵ�ַ  
bdurl = 'http://tieba.baidu.com/p/4441409629?pn='  
#iPostBegin = 1  
#iPostEnd = 10  
  
#bdurl = str(raw_input(u'���������ɵĵ�ַ��ȥ��pn=��������֣�\n'))  
#begin_page = int(raw_input(u'�����뿪ʼ��ҳ����\n'))  
#end_page = int(raw_input(u'�������յ��ҳ����\n'))  
#-------- ������������� ------------------  
begin_page = 1
end_page = 10
#����  
baidu_tieba(bdurl,begin_page,end_page)  