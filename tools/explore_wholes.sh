#!/bin/sh
streamlit run ${COCO_EXPLORER} -- \
--coco_train /home/gregork/dataset/coco_parts_ts4/annotations/val_wholes.json \
--coco_predictions /home/gregork/workspace/robot-simulation/out/cnn/models/wholes/ts4/default/val_0001999/coco_instances_results.json \
--images_path /home/gregork/dataset/coco_parts_ts4/val/