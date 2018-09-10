stat 系统调用时用来返回相关文件的系统状态信息的。

首先我们看一下stat中有哪些属性:

>>> import os
>>> print os.stat("/root/python/zip.py")
(33188, 2033080, 26626L, 1, 0, 0, 864, 1297653596, 1275528102, 1292892895)
>>> print os.stat("/root/python/zip.py").st_mode   #权限模式
33188
>>> print os.stat("/root/python/zip.py").st_ino   #inode number
2033080
>>> print os.stat("/root/python/zip.py").st_dev    #device
26626
>>> print os.stat("/root/python/zip.py").st_nlink  #number of hard links
1
>>> print os.stat("/root/python/zip.py").st_uid    #所有用户的user id
0
>>> print os.stat("/root/python/zip.py").st_gid    #所有用户的group id
0
>>> print os.stat("/root/python/zip.py").st_size  #文件的大小，以位为单位
864
>>> print os.stat("/root/python/zip.py").st_atime  #文件最后访问时间
1297653596
>>> print os.stat("/root/python/zip.py").st_mtime  #文件最后修改时间
1275528102
>>> print os.stat("/root/python/zip.py").st_ctime  #文件创建时间
1292892895



'''
        os.stat_result(
        st_mode=33206, 
        st_ino=4785074604179011, 
        st_dev=10461841, 
        st_nlink=1, 
        st_uid=0, 
        st_gid=0, 
        st_size=208, 
        st_atime=1530777169, 
        st_mtime=1530777169, 
        st_ctime=1530685403)
        '''
        
        
                '''
        time.struct_time(
        tm_year=2018, 
        tm_mon=7, tm_mday=5, tm_hour=15, tm_min=52, 
        tm_sec=49, tm_wday=3, tm_yday=186, tm_isdst=0)
        '''