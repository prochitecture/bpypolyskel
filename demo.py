"""
This module demontrates the funcion polygonize() of bpypolyskel.

It cannot be used in Blender and is thought to be used by an interpreter
where the library mathutils is installed as standalone library.

Use 'pip install mathutils'
"""
import math
import mathutils
import matplotlib.pyplot as plt

from bpypolyskel import bpypolyskel
from matplotlib.widgets import Slider


# Define vertices of a polygon and a hole.
_COORDS = [
    # Polygon contour in counterclockwise order, seen from top.
    # The polygon is on the left of this contour.
    [0, 0, 0],
    [10, 0, 0],
    [10, 5, 0],
    [45, 5, 0],
    [45, 20, 0],
    [10, 20, 0],
    [10, 25, 0],
    [0, 25, 0],
    # Hole contour in clockwise order, seen from top.
    # The polygon is on the left of this contour.
    [5, 16, 0],
    [35, 16, 0],
    [35, 9, 0],
    [5, 9, 0],
]

# Convert the coordinates to 'mathutils.Vector' objects.
VERTS = [mathutils.Vector(coords) for coords in _COORDS]

# Define indices and lengths of polygon and hole.
FIRST_VERTEX_INDEX = 0
NUM_VERTS = 8
HOLES_INFO = [(8, 4)]

# We let polygonize() compute the unit vectors and have no faces yet.
FACES, UNIT_VECTORS = None, None

# Pitch values.
MIN_PITCH = 0.0
MAX_PITCH = 80.0
DEFAULT_PITCH = 30.0


def create_roof(pitch, ax):
    ax.clear()

    faces = bpypolyskel.polygonize(
        VERTS,
        FIRST_VERTEX_INDEX,
        NUM_VERTS,
        HOLES_INFO,
        0.0,
        math.tan(pitch * math.pi / 180),
        FACES,
        UNIT_VECTORS,
    )

    # Plot the hipped roof in 3D.
    for face in faces:
        for edge in zip(face, face[1:] + face[:1]):
            p1, p2 = VERTS[edge[0]], VERTS[edge[1]]
            ax.plot([p1.x, p2.x], [p1.y, p2.y], [p1.z, p2.z], 'k')

    ax.axis('equal')
    ax.set_zlim(0, 30)


def run_demo():
    fig = plt.figure('Roof Demo')
    ax = fig.add_subplot(projection='3d')

    # Display the roof using the default pitch.
    create_roof(DEFAULT_PITCH, ax)

    # Add a vertical slider to control the pitch.
    pitch_slider = Slider(
        ax=fig.add_axes([0.9, 0.2, 0.02, 0.6]),
        label="Roof pitch\n(degrees)",
        valmin=MIN_PITCH,
        valmax=MAX_PITCH,
        valinit=DEFAULT_PITCH,
        valstep=1.0,
        orientation="vertical"
    )
    pitch_slider.on_changed(lambda pitch: create_roof(pitch, ax))

    plt.show()


if __name__ == "__main__":
    # Execute only if run as a script.
    run_demo()
