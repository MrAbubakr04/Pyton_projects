'''p=int(input('введи свое число'))
if p==5:
    print(13)
elif p==3:
    print('сработал')
#else: print('не сработал')'''
'''a=3.4
i=int(a)
d='123.35'
m=float(d)
a=i*d
print(a,i,d,m)
print('a='+a=input('cout<<'))
    '''
'''import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


phi = np.linspace(0, np.pi, 30)
theta = np.linspace(0, 2 * np.pi, 30)
phi, theta = np.meshgrid(phi, theta)
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(x, y, z, color='b', alpha=0.5)


ax.set_title('Sphera')


plt.show()
'''
'''import matplotlib as mpl
 import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation


 T = 100

 FFMpegWriter = manimation.writers['ffmpeg']

 writer = FFMpegWriter(fps=25)

 mpl.rcParams['legend.fontsize'] = 10


 fig = plt.figure()


 writer.setup(fig, "video.avi" , 200)
 x = np.arange(0, np.pi * 5, 0.1)

for t in range(0, T):
# Âûâîäèì íîìåð êàäðà íà ýêðàí äëÿ óäîáñòâà
print('Drawing frame %d...' % (t))

 y = np.sin(x - 2 * np.pi * t / T)


 plt.plot(x, y)
 plt.title("T = %f" % (t))


writer.grab_frame()

45 plt.clf()'''
'''import matplotlib as mpl
import matplotlib.animation as manimation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.cm as cm
import math
import matplotlib.pyplot as plt

fig = plt.figure()
T = 50
plt.rcParams['animation.ffmpeg_path']
writer = manimation.FFMpegWriter(fps=25)
sigma = 0.05

mpl.rcParams['legend.fontsize'] = 10
writer.setup(fig, "video.gif" , 200)
x = np.arange(-10, 10, 0.05)
y = np.arange(-10, 10, 0.05)

X, Y = np.meshgrid(x, y)

for t in range(0, T):
    print('Drawing frame %d...' % (t))
    Z = (X**2)/((t-10)**2) - (Y**2)/((t+10)**2)
    ax = fig.add_subplot(projection='3d')
    ax.set_zlim(-1, 1)
    ax.plot_surface(X, Y, Z)
    ax.set_title("T = %f" % (t))
    writer.grab_frame()
    plt.clf()'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Создание данных для куба
theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 100)
x_cube = np.outer(np.cos(theta), np.sin(phi))
y_cube = np.outer(np.sin(theta), np.sin(phi))
z_cube = np.outer(np.ones_like(theta), np.cos(phi))

# Создание данных для сферы
x_sphere = np.outer(np.cos(theta), np.sin(phi))
y_sphere = np.outer(np.sin(theta), np.sin(phi))
z_sphere = np.outer(np.cos(phi), np.ones_like(theta))

# Создание новой фигуры
fig = plt.figure()

# Создание трехмерной подложки
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Определение анимации
def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.plot_surface(x_cube, y_cube, z_cube, color='blue', alpha=0.6)  # Куб
    ax.plot_surface(x_sphere * frame + (1 - frame) * x_cube, 
                     y_sphere * frame + (1 - frame) * y_cube, 
                     z_sphere * frame + (1 - frame) * z_cube, color='red', alpha=0.6)  # Сфера

# Создание анимации
ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), interval=50)

# Сохранение анимации в видео-файле
ani.save('cube_to_sphere.gif', writer='pillow', fps=25)

plt.show()
