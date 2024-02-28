# Masters Dissertation: IN THE PURSUIT OF A NEW STATE-OF-THE-ART MODEL FOR ANOMALY LOCALIZATION WITH DOMAIN SHIFT

This is an official PyTorch implementation of the Master's Dissertation "IN THE PURSUIT OF A NEW STATE-OF-THE-ART MODEL FOR ANOMALY LOCALIZATION WITH DOMAIN SHIFT".
This repository contains all the scripts required to recreate the proposed model in the dissertation.


### Get Started

This code in this repository assumes that you are working on a linux machine.

Create a folder called "notebooks" in your home folder. Add this repository into the "notebooks" folder. All the following files should be inside the notebooks folder. This ensures that all the file paths in the config file of this program function properly.

#### Dataset

The dataset used for this Thesis is a real-world Aero-engine Blade Anomaly Detection (AeBAD) dataset, consisting of two sub-datasets: the single-blade dataset (AeBAD-S) and the video anomaly detection dataset of blades (AeBAD-V).

**Download dataset at (Change this link to your link, just in case the link from the MMR authors expires) [here](https://drive.google.com/file/d/14wkZAFFeudlg0NMFLsiGwS0E593b-lNo/view?usp=share_link) (Google Drive).

The dataset is a zip file. If you run the commands inside the jupyter notebook 01_Preparing_AeBAD_dataset.ipynb, the dataset will be unzipped and the MACOSX version will be deleted.


#### Pre-trained models

Download the pre-trained model of MAE (ViT-base) at [here](https://dl.fbaipublicfiles.com/mae/visualize/mae_visualize_vit_base.pth).
Please save this pth file inside the MMR folder.

#### Train and Test for AeBAD

MMR/method_config/ folder contains the config files for the training and testing runs of this model. 
MMR/method_config/AeBAD_S/MMR.yaml is relevant for training and testing this model on the AeBAD_S dataset. 
MMR/method_config/AeBAD_V/MMR.yaml is relevant for training and testing this model on the AeBAD_V dataset. 
Inside these yaml files TRAIN.MMR.model_chkpt in MMR.yaml is the path of above downloaded MAE model. TRAIN.dataset_path (TEST.dataset_path) is the path of data.
Set Test.save_segmentation_images as True or False to save processed image.

Run the code in 02_MMR_with_saliency_guided_random_masking_AeBAD_S.ipynb for training and testing the model on the AeBAD_S dataset.
Run the code in 03_MMR_with_saliency_guided_random_masking_AeBAD_V.ipynb for training and testing the model on the AeBAD_V dataset.

**Note that for AeBAD-V, we only evaluate the sample-level metric. The pixel-level metric is 0.**

## Acknowledgement
I would like to acknowledge the excellent implementation from [MMR](https://github.com/zhangzilongc/MMR)


