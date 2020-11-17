# polygonize

`polygonize()` computes the faces of a hipped roof from  a footprint polygon of a building, skeletonized by a straight skeleton. It accepts a simple description of the vertices of the footprint polygon, including those of evetual holes, and returns a list of polygon faces.

The polygon is expected as a list of vertices in counterclockwise order. In a right-handed coordinate system, seen from top, the polygon is on the left of its contour. Holes are expected as lists of vertices in clockwise order. Seen from top, the polygon is on the left of the hole's contour.

```
polygonize(verts, firstVertIndex, numVerts, holesInfo=None, height=0.0, tan=0.0, faces=None, unitVectors=None, mergeRange=0.15)
```
## Arguments
<table width=100% border="0">
  <tr>
    <th align="left" width=17%>Argument</th>
    <th align="left">Description</th>
  </tr>
  <tr>
    <td valign="top"><i>verts</td>
    <td>
        A list of vertices. Vertices that define the outer contour of the footprint polygon are located in a continuous block of the <code>verts</code> list, starting at the index <code>firstVertIndex</code>. Each vertex is an instance of <code>mathutils.Vector</code> with 3 coordinates x, y and z. The z-coordinate must be the same for all vertices of the polygon.<br><br>
        The outer contour of the footprint polygon contains <code>numVerts</code> vertices in counterclockwise order, in its block in <code>verts</code>.<br><br>
        Vertices that define eventual holes are also located in <code>verts</code>. Every hole takes its continuous block. The start index and the length of every hole block are described by the argument <code>holesInfo</code>. See there.<br><br>
        The list of vertices <code>verts</code> gets extended by <code>polygonize()</code>. The new nodes of the straight skeleton are appended at the end of the list.
    </td>
  </tr>
  
  <tr>
    <td valign="top"><i>firstVertIndex</td>
    <td>
        The first index of vertices of the polygon index in the <code>verts</code> list that defines the footprint polygon.
    </td>
  </tr>
  
  <tr>
    <td valign="top"><i>numVerts</td>
    <td>
        The first index of the vertices in the <code>verts</code> list of the polygon, that defines the outer contour of the footprint.
    </td>
  </tr>
  
  <tr>
    <td valign="top"><i>holesInfo</td>
    <td>
        If the footprint polygon contains holes, their position and length in the <code>verts</code> list are described by this argument. <code>holesInfo</code> is a list of tuples, one for every hole. The first element in every tuple is the start index of the hole's vertices in <code>verts</code> and the second element is the number of its vertices.<br><br>
        The default value of <code>holesInfo</code> is <code>None</code>, which means that there are no holes.
    </td>
  </tr>
  
  <tr>
    <td valign="top"><i>height</td>
    <td>
        The maximum height of the hipped roof to be generated. If both <code>height</code> and <code>tan</code> are equal to zero, flat faces are generated. <code>height</code> takes precedence over <code>tan</code> if both have a non-zero value. The default value of <code>height</code> is 0.0.
    </td>
  </tr>
  
  <tr>
    <td valign="top"><i>tan</td>
    <td>
        In many cases it's desirable to deal with the roof pitch angle instead of the maximum roof height. The tangent <code>tan</code> of the roof pitch angle can be supplied for that case. If both <code>height</code> and <code>tan</code> are equal to zero, flat faces are generated. <code>height</code> takes precedence over <code>tan</code> if both have a non-zero value. The default value of <code>tan</code> is 0.0.
    </td>
  </tr>
  
  <tr>
    <td valign="top"><i>faces</td>
    <td>
        An already existing Python list of faces. Everey face in this list is itself a list of indices of the face-vertices in the <code>verts</code> list. If this argument is <code>None</code> (its default value), a new list with the new faces created by the straight skeleton is created and returned by polygonize(), else <code>faces</code> is extended by the new list.
    </td>
  </tr>
  
  <tr>
    <td valign="top"><i>unitVectors</td>
    <td>
        A Python list of unit vectors along the polygon edges (including holes if they are present). These vectors are of type <code>mathutils.Vector</code> with three dimensions. The direction of the vectors corresponds to order of the vertices in the polygon and its holes. The order of the unit vectors in the <code>unitVectors</code> list corresponds to the order of vertices in the input Python list <code>verts</code>.<br><br>
        The list <code>unitVectors</code> (if given) gets used inside <code>polygonize()</code> function instead of calculating it once more. If this argument is <code>None</code> (its default value), the unit vectors get calculated inside <code>polygonize()</code>.
    </td>
  </tr>
  
  <tr>
    <td valign="top"><i>mergeRange</td>
    <td>
        <code>skeletonize()</code> sometimes produces clusters of vertices that are close together. These get merged into one vertice, for all pairs of vertices, that are within a square of width <code>mergeRange</code> and where the Manhattan distance between such pairs is less than <code>5*mergeRange</code>. The default value of <code>mergeRange</code> is 0.15.
    </td>
  </tr>
</table> 

## Output
<table width=100% border="0">
  <tr>
    <th align="left" width=17%>Value</th>
    <th align="left">Description</th>
  </tr>

  <tr>
    <td valign="top"><i>verts</td>
    <td>
        The list of the vertices <code>verts</code> gets extended at its end by the vertices of the straight skeleton.
    </td>
  </tr>
  
  <tr>
    <td valign="top"><i>return</td>
    <td>
        A list of the faces created by the straight skeleton. Everey face in this list is a list of indices of the face-vertices in the <code>verts</code> list. The order of vertices of the faces is counterclockwise, as the order of vertices in the input Python list <code>verts</code>. The first edge of a face is always an edge of the polygon or its holes.<br><br>
        If a list of faces has been given in the argument <code>faces</code>, it gets extended at 
        its end by the new list.
    </td>
  </tr>
</table> 
