# 将远程仓库里面的项目拉下来
`git pull origin master`
# 删除target文件夹
`git rm -r --cached target`
# 提交,添加操作说明
`git commit -m '删除了target`'
# 添加远程仓库
`git remote add origin git@github.com:hll5752249/py.git`
# 将本次更改更新到github项目上去
`git push -u origin master`
# 完成操作
