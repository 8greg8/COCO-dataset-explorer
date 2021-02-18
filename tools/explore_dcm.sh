#!/bin/bash
streamlit run ${COCO_EXPLORER} -- \
--coco_train /home/gregork/dataset/coco_parts_ts2/annotations/val_wholes.json \
--coco_predictions /home/gregork/workspace/robot-simulation/out/dcm/models/gmm/ts2/std_dmap/result-coco_det-gt_val-param_0.75nms_1e-17prop.json \
--images_path /home/gregork/dataset/coco_parts_ts2/val/