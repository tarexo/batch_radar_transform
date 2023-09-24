import numpy as np
from pathlib import Path

def write_pointcloud(pc: np.array, path: Path, file_name: str, type: str = np.float32):
    """Write a point cloud to a given file name.

    Args:
        pc (np.array): The point cloud to be written.
        path (Path): Path were the file should be written to.
        file_name (str): Name of the file containing the point cloud.
        type (str, optional): Type of the point cloud data. Defaults to "float32".
    """
    pc.astype(type).tofile(str(path / file_name))


def load_original_radar_pointcloud(
    file_path: Path,
    d_type: type = np.float32,
) -> np.ndarray:
    """Loads a point cloud given a file name.

    Args:
        file_path (str): Path to the file containing the point cloud.
        d_type (type): Optional, defaults to np.float32. Sets the data type.

    Returns:
        np.ndarray: The loaded point cloud.
    """
    return np.fromfile(file_path, dtype=d_type).reshape(-1, 7)


def load_transformed_radar_pointcloud(
    file_path: Path,
    d_type: type = np.float32,
) -> np.ndarray:
    """Loads a point cloud given a file name.

    Args:
        file_path (str): Path to the file containing the point cloud.
        d_type (type): Optional, defaults to np.float32. Sets the data type.

    Returns:
        np.ndarray: The loaded point cloud.
    """
    return np.fromfile(file_path, dtype=d_type).reshape(-1, 4)