import execjs

node=execjs.get()
filePath='qixiang/testPyexec.js'
ctx=node.compile(open(filePath).read())

js='add("{0}", "{1}")'.format(1, 2)
result=ctx.eval(js)
print(result)

