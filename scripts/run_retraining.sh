#!/bin/bash
#
# Usage:
# ./scripts/Run_Pretreatment_and_Training.sh
set -e

echo ''
echo ''
echo '--------------------------------------------'
echo 'WELCOME TO THE RETRAINING INCEPTION PROGRAM'
echo '--------------------------------------------'
echo ''
echo ''
echo 'This script let you retrain the last layers of the inception model of your choice'
echo ''
echo 'Available models:' 
echo 'inception_v3 | inception_v4 | inception_resnet_v2'
echo ''
echo 'Please enter the model you want to use:'
read ARCHITECTURE
echo ''
echo 'Please enter the number of iterations you want to run:'
read ITERATIONS
echo ''
echo 'Starting the retraining process...'
echo ''

# Fine-tune only the new layers for choosen number of steps.
python -m scripts.retrain \
--architecture="${ARCHITECTURE}" \
--bottleneck_dir=workspace/bottlenecks \
--how_many_training_steps=$ITERATIONS \
--model_dir=workspace/models/ \
--summaries_dir=workspace/training_summaries/"${ARCHITECTURE}" \
--output_graph=workspace/retrained_graph.pb \
--output_labels=workspace/retrained_labels.txt \
--image_dir=workspace/images
  
echo ''
echo ''
echo '-----------------'
echo 'Training done!!!'
echo '-----------------'
echo ''
echo ''
echo 'Use return_labels.py to test your model'
echo ''
