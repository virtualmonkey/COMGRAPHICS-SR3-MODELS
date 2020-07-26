from gl import Render, color

from obj import Obj

r = Render(1000,1500)

r.loadModel('./models/sonic.obj', (400,200), (40,40) )

r.glFinish('output.bmp')