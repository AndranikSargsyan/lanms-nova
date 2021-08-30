import numpy as np

from .lanmslib import merge_quadrangle_n9 as nms_impl


def merge_quadrangle_n9(polys: np.ndarray, nms_thresh: float = 0.3, precision: int = 10000) -> np.ndarray:
    if len(polys) == 0:
        return np.array([], dtype='float32')

    p = polys.copy()
    p[:, :8] *= precision
    ret = np.array(nms_impl(p, nms_thresh), dtype='float32')
    ret[:, :8] /= precision

    return ret
