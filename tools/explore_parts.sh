#!/bin/sh
streamlit run ${COCO_EXPLORER} -- \
--coco_train /home/gregork/dataset/coco_parts_ts2/annotations/val_parts.json \
--coco_predictions /home/gregork/workspace/robot-simulation/out/cnn/models/parts/ts2/default/val_0037999/coco_instances_results.json \
--images_path /home/gregork/dataset/coco_parts_ts2/val/