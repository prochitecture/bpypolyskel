"""
This module demontrates the funcion polygonize() of bpypolyskel.

It cannot be used in Blender and is thought to be used by an interpreter
where the library mathutils is installed as standalone library.

Use 'pip install mathutils'
"""
import math
import mathutils
import matplotlib.pyplot as plt
import sys
import time

from bpypolyskel import bpypolyskel
from matplotlib.widgets import Slider


# Define the outer loop of the floor plan (CCW order).
_OUTER_LOOP = [
    [1482.83, 495.548, 0],
    [1623.76, 593.700, 0],
    [1734.48, 724.983, 0],
    [1807.45, 880.449, 0],
    [1837.70, 1049.50, 0],
    [1823.16, 1220.63, 0],
    [1764.82, 1382.16, 0],
    [1666.67, 1523.08, 0],
    [1535.39, 1633.81, 0],
    [1379.92, 1706.78, 0],
    [1210.87, 1737.02, 0],
    [1039.75, 1722.49, 0],
    [878.216, 1664.15, 0],
    [737.288, 1566.00, 0],
    [626.566, 1434.72, 0],
    [553.596, 1279.25, 0],
    [523.349, 1110.20, 0],
    [537.887, 939.072, 0],
    [596.221, 777.543, 0],
    [694.373, 636.616, 0],
    [825.656, 525.894, 0],
    [981.122, 452.923, 0],
    [1150.18, 422.676, 0],
    [1321.30, 437.215, 0],
]

# Define the inner loop of the floor plan (CW order).
_INNER_LOOP = [
    [1351.82, 1444.80, 0],
    [1440.44, 1388.03, 0],
    [1511.34, 1310.26, 0],
    [1559.70, 1216.78, 0],
    [1582.23, 1113.98, 0],
    [1577.37, 1008.85, 0],
    [1545.47, 908.555, 0],
    [1488.70, 819.936, 0],
    [1410.93, 749.030, 0],
    [1317.46, 700.668, 0],
    [1214.65, 678.148, 0],
    [1109.52, 683.002, 0],
    [1009.23, 714.901, 0],
    [920.609, 771.671, 0],
    [849.702, 849.442, 0],
    [801.341, 942.916, 0],
    [778.820, 1045.72, 0],
    [783.675, 1150.85, 0],
    [815.574, 1251.14, 0],
    [872.344, 1339.76, 0],
    [950.115, 1410.67, 0],
    [1043.59, 1459.03, 0],
    [1146.39, 1481.55, 0],
    [1251.53, 1476.70, 0],
]

_COORDS = _OUTER_LOOP + _INNER_LOOP

# Convert the coordinates to 'mathutils.Vector' objects.
VERTS = [mathutils.Vector(coords) for coords in _COORDS]

# Define indices and lengths of polygon and hole.
FIRST_VERTEX_INDEX = 0
NUM_VERTS = len(_OUTER_LOOP)
HOLES_INFO = [(NUM_VERTS, len(_INNER_LOOP))]

# We let polygonize() compute the unit vectors and have no faces yet.
FACES, UNIT_VECTORS = None, None

# Pitch values.
MIN_PITCH = 0.0
MAX_PITCH = 80.0
DEFAULT_PITCH = 30.0


def get_roof_faces(pitch):
    return bpypolyskel.polygonize(
        VERTS,
        FIRST_VERTEX_INDEX,
        NUM_VERTS,
        HOLES_INFO,
        0.0,
        math.tan(pitch * math.pi / 180),
        FACES,
        UNIT_VECTORS,
    )

def create_roof(pitch, ax):
    ax.clear()

    # Create the roof faces.
    faces = get_roof_faces(pitch)

    # Plot the hipped roof in 3D.
    for face in faces:
        for edge in zip(face, face[1:] + face[:1]):
            p1, p2 = VERTS[edge[0]], VERTS[edge[1]]
            ax.plot([p1.x, p2.x], [p1.y, p2.y], [p1.z, p2.z], 'k')

    ax.axis('equal')
    ax.set_zlim(0, 1200)


def run_demo():
    fig = plt.figure('Roof Demo')
    ax = fig.add_subplot(projection='3d')

    # Display the roof using the default pitch.
    create_roof(DEFAULT_PITCH, ax)

    # Add a vertical slider to control the pitch.
    pitch_slider = Slider(
        ax=fig.add_axes([0.9, 0.2, 0.02, 0.6]),
        label='Roof pitch\n(degrees)',
        valmin=MIN_PITCH,
        valmax=MAX_PITCH,
        valinit=DEFAULT_PITCH,
        valstep=1.0,
        orientation='vertical'
    )
    pitch_slider.on_changed(lambda pitch: create_roof(pitch, ax))

    plt.show()


def run_benchmark():
    start = time.perf_counter()
    pitch = 0

    while pitch < 90:
        _ = get_roof_faces(pitch)
        pitch += 0.1

    duration = time.perf_counter() - start
    print(f'Execution time: {round(duration, 4)} seconds.')


if __name__ == '__main__':
    # Execute only if run as a script.
    if len(sys.argv) == 2 and sys.argv[1] == '--benchmark':
        run_benchmark()
    else:
        run_demo()
