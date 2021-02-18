"""
 Copyright (C) 2020 GORENJE d. o. o. - All Rights Reserved
 
 Unauthorized copying of this file, via any medium is strictly prohibited.
 Proprietary and confidential.
 
 Written by Gregor Koporec
"""

from grcore.common.config import CN
from pathlib import Path

_C = CN()

# Name of coco json ground truth file
_C.GT = ""
# Name of coco json prediction file
_C.DT = ""


# Dataset parameters
_C.DATASET = CN()
# Label of the dataset
_C.DATASET.NAME = "coco"
# Path to a dataset
_C.DATASET.PATH = ""
# Name of dataset images folder
_C.DATASET.IMG_FOLDER = "test"


def get_cfg_defaults():
    """
    Get a yacs CfgNode object with default values for this project
    """
    return _C.clone()


def setup_cfg(cfg):
    # Defrost
    freezing = False
    if cfg.is_frozen():
        freezing = True
        cfg.defrost()

    # Configure paths
    cfg.DATASET.PATH = str(Path(cfg.DATASET.PATH).resolve())

    # Freeze
    if freezing:
        cfg.freeze()
