#!/bin/bash
streamlit run ${COCO_EXPLORER} -- \
--coco_train /home/gregork/dataset/coco_parts_ts4/annotations/val_wholes.json \
--images_path /home/gregork/dataset/coco_parts_ts4/val/