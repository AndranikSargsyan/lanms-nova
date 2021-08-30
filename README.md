# Locality-Aware Non-Maximum Suppression (LANMS)

This is a python binding for LANMS as described by Zhout et al.
in their paper "EAST: An Efficient and Accurate Scene Text Detector", CVPR 2017. The C++ code is  taken from the
implementation available on: https://github.com/argman/EAST

### Installation

`pip install lanms-nova`

### Usage example
```python
import numpy as np
import lanms

boxes = np.array([
     [137.0, 113.6, 162.3, 113.3, 162.4, 122.2, 137.2, 122.6, 0.75],
     [137.2, 113.8, 163.2, 114.6, 163.0, 122.6, 137.0, 121.9, 0.97],
     [136.8, 113.4, 163.2, 114.5, 162.9, 122.7, 136.5, 121.6, 0.15],
     [136.6, 112.9, 163.3, 114.5, 162.8, 122.9, 136.1, 121.3, 0.95],
     [136.4, 112.6, 163.4, 114.5, 162.8, 123.0, 135.8, 121.2, 0.96],
     [131.4, 89.2,  137.8, 89.0,  138.2, 98.5,  131.8,  98.7, 0.98],
     [131.6, 89.2,  137.8, 89.1,  138.1, 98.6,  131.8,  98.8, 0.32],
     [131.5, 89.2,  137.9, 89.1,  138.0, 98.6,  131.6,  98.7, 0.99],
     [131.5, 89.2,  138.0, 89.1,  138.1, 98.5,  131.6,  98.5, 0.87],
     [131.5, 89.3,  137.8, 89.0,  138.2, 98.4,  132.0,  98.7, 0.97]
], dtype=np.float32)

boxes = lanms.merge_quadrangle_n9(boxes, nms_thresh=0.5)
print(boxes)
```
