#!/bin/bash
streamlit run ${COCO_EXPLORER} -- \
--coco_train /home/gregork/dataset/coco_parts_ts4/annotations/test_wholes.json \
--coco_predictions /home/gregork/workspace/robot-simulation/out/dcm/models/ts4_train/gmm/std_dmap/model_d161b01a-78cd-3a78-944e-f7969bf8837b/result-model.lib_det-cnn_imbalanced_test_999.json \
--images_path /home/gregork/dataset/coco_parts_ts4/test/