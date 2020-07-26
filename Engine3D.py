from gl import Render, color

r = Render(600,600)

r.glViewport(100,100, 400, 400)

r.glClearColor(0,0,0)
r.glColor(0.45,0.5,0)
r.glClear()

r.glLine(-1,0, 0,1)
r.glLine(0,1, 1,0)
r.glLine(1,0, 0,-1)
r.glLine(0,-1, -1,0)
r.glLine(-1,0, 1,0)
r.glLine(0,-1, 0,1)
r.glLine(-1,-1, -1,1)
r.glLine(-1,1, 1,1)
r.glLine(1,1, 1,-1)
r.glLine(1,-1, -1,-1)
r.glLine(-1,-1, 1,1)
r.glLine(1,-1, -1,1)


r.glFinish('output.bmp')