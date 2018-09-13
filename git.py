 # git 操作 #

## 远程库操作 ##
git remote      #常看所有连接的远程库名

# origin
# py
# py_new


git remote add [shortname] [url]    # 添加远程仓库
# git remote add origin git@server-name:path/repo-name.git


git remote -v       #查看所有远程库名称及地址
# origin  git@github.com:ShiningChan/ShiningChan.git (fetch)
# origin  git@github.com:ShiningChan/ShiningChan.git (push)
# py      git://github.com/ShiningChan/ieleven.git (fetch)
# py      git://github.com/ShiningChan/ieleven.git (push)
# py_new  git@github.com:ShiningChan/ieleven.git (fetch)
# py_new  git@github.com:ShiningChan/ieleven.git (push)


git remote rm [shortname]       #删除远程库

git remote rename [old_sn] [new_sn]     #重命名远程库

git push [shortname] master     #推送数据到远程仓库
# git push -u origin master   (第一次推送 使用-u增加关联)

## 本地库 ##

git status      #查看本地仓库状态

git diff readme.txt         #查看修改了什么

git log     #查看日志

## 提交

git add readme.txt      #提交更新、提交新文件

git commit -m "add distributed"      #提交

## 删除
rm text.txt     #本地删除

git rm test.txt     #从版本库删除文件

git commit -m "remove text.txt"     #提交到工作区

# 版本库的版本替换工作区的版本 无论是修改还是删除
git checkout -- readme.txt      #丢弃工作区修改


# 从远程库克隆
git clone [URL]
# git clone git@github.com:ShiningChan/ieleven.git


