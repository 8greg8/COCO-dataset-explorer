"""
 Copyright (C) 2020 GORENJE d. o. o. - All Rights Reserved
 
 Unauthorized copying of this file, via any medium is strictly prohibited.
 Proprietary and confidential.
 
 Written by Gregor Koporec
"""

import subprocess
from argparse import ArgumentParser
from config import get_cfg_defaults, setup_cfg
from pathlib import Path


def get_cfg(args):
    cfg = get_cfg_defaults()
    cfg.merge_from_file(args.cfg)
    setup_cfg(cfg)
    cfg.freeze()

    print("#" * 80)
    print("Configuration:")
    print("-" * 80)
    print(cfg)
    print("#" * 80)

    return cfg


def get_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--cfg", type=str, metavar="<cfg>", help="Config file",
    )

    return parser


def main(args, cfg):
    gt_file = str(Path(cfg.DATASET.PATH) / "annotations" / cfg.GT)
    dt_file = cfg.DT
    img_path = str(Path(cfg.DATASET.PATH) / cfg.DATASET.IMG_FOLDER) + "/"
    cocoexplorer = "streamlit run ${COCO_EXPLORER} --"
    command = [
        cocoexplorer,
        "--coco_train",
        gt_file,
        "--coco_predictions",
        dt_file,
        "--images_path",
        img_path,
    ]
    print(f"Running command: {' '.join(command)}")
    subprocess.run(
        command, shell=True,
    )


if __name__ == "__main__":
    args = get_parser().parse_args()
    cfg = get_cfg(args)
    main(args, cfg)
