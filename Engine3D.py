from gl import Render, color

from obj import Obj

r = Render(1200,3000)

r.loadModel('./models/bears.obj', (400,200), (40,40) )

r.glFinish('output.bmp')