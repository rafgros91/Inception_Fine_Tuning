# Inception_Fine_Tuning
A script to fine-tune (retrain last layers) the pre-trained inception model of your choice (Inceptionv3, Inceptionv4 or InceptionResNetv2) with the desired number of iterations (Adapted from Google's  script in "Tensorflow for Poets" example).

## Usage
Train the Inception model with your own images to be able to do image classification.

## Instructions
- Add your images organized by directories that will be their classes in "workspace/images"
- From the root directory, run "./scripts/run_retraining.sh"
- Choose the inception model and enter the number of iterations you want to run
- Wait for the training
- Once done, you can run "python ./scritps/return_labels.py --image [PATH TO YOUR TEST IMAGE]" to evaluate the model obtained"
