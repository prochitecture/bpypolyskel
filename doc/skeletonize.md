# skeletonize

`skeletonize()` computes the straight skeleton of a polygon. It accepts a simple description of the contour of a footprint polygon, including those of evetual holes, and returns the nodes and edges of its straight skeleton.

The polygon is expected as a list of contours, where every contour is a list of edges of type `Edge2` (imported from `bpyeuclid`). The outer contour of the polyigon is the first list of in the list of contours and is expected in counterclockwise order. In the right-handed coordinate system, seen from top, the polygon is on the left of its contour.

If the footprint has holes, their contours are expected as lists of their edges, following the outer contour of the polygon. Their edges are in clockwise order, seen from top, the polygon is on the left of the hole's contour.

```
skeletonize(edgeContours, mergeRange=0.15)
```
## Arguments
<table width=100% border="0">
  <tr>
    <th align="left" width=17%>Argument</th>
    <th align="left">Description</th>
  </tr>
  <tr>
    <td valign="top"><i>edgeContours</td>
    <td>
        A list of contours of the polygon and eventually its holes, where every contour is a list of edges of type `Edge2` (imported from `bpyeuclid`). It is expected to as:<br><br>
        <code>edgeContours = [ polygon_edge,&#60;hole1_edges&#62;, &#60;hole2_edges&#62;, ...]</code><br><br>
        <code>polygon_egdes</code> is a list of the edges of the outer polygon contour in counterclockwise order. <code>&#60;hole_edges&#62;</code> is an optional list of the edges of a hole contour in clockwise order.
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
    <td valign="top"><i>return</td>
    <td>
        A list of subtrees (of type <code>Subtree</code>) of the straight skeleton. A <code>Subtree</code> contains the attributes <code>(source, height, sinks)</code>, where <code>source</code> is the node vertex, <code>height</code> is its distance to the nearest polygon edge, and <code>sinks</code> is a list of vertices connected to the node. All vertices are of type <code>mathutils.Vertex</code> with two dimension x and y.
    </td>
  </tr>
</table> 
