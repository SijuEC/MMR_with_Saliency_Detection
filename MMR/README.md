## IN THE PURSUIT OF A NEW STATE-OF-THE-ART MODEL FOR ANOMALY LOCALIZATION WITH DOMAIN SHIFT

This is an official PyTorch implementation of the master's thesis "IN THE PURSUIT OF A NEW STATE-OF-THE-ART MODEL FOR ANOMALY LOCALIZATION WITH DOMAIN SHIFT"

### Datasets

The dataset used for this Thesis is a real-world Aero-engine Blade Anomaly Detection (AeBAD) dataset, consisting of two sub-datasets: the single-blade dataset (AeBAD-S) and the video anomaly detection dataset of blades (AeBAD-V).

**Download dataset at (Change this link to your link, just in case the link from the MMR authors expires) [here](https://drive.google.com/file/d/14wkZAFFeudlg0NMFLsiGwS0E593b-lNo/view?usp=share_link) (Google Drive).

### Get Started

#### Pre-trained models

Download the pre-trained model of MAE (ViT-base) at [here](https://dl.fbaipublicfiles.com/mae/visualize/mae_visualize_vit_base.pth).
Please save this pth file inside the MMR folder.

#### Dataset


**AeBAD:**

Download the AeBAD dataset from the above link. The AeBAD dataset directory should be as follows.

```
|-- AeBAD
    |-- AeBAD_S
        |-- train
            |-- good
                |-- background
        |-- test
                |-- ablation
                    |-- background
        |-- ground_truth
                |-- ablation
                    |-- view
    |-- AeBAD_V
        |-- test
            |-- video1
                |-- anomaly
        |-- train
            |-- good
                |-- video1_train
```

**Note that background, view and illumination in the train set is different from test. The background, view and illumination in test is unseen for the training set.**

#### Train and Test for AeBAD

Create a folder called "notebooks" in your home folder. Paste this repository into this "notebooks" folder. Next, paste the dataset zip file into this repository as well. This ensures that all the file paths in the config file of this program function properly.

MMR/method_config/ folder contains the config files for the training and testing runs of this model. 
MMR/method_config/AeBAD_S/MMR.yaml is relevant for training and testing this model on the AeBAD_S dataset. 
MMR/method_config/AeBAD_V/MMR.yaml is relevant for training and testing this model on the AeBAD_V dataset. 

Run the code in 01_Preparing_AeBAD_dataset.ipynb to prepare the dataset for the MMR model. (**Update**)
Run the code in 12_MMR_random_mask_with_sal_prior_0.6-mask-ratio_AeBAD_S.ipynb for training and testing the model on the AeBAD_S dataset. (**Update**)
Run the code in 15_MMR_random_mask_with_sal_prior_0.6-mask-ratio_AeBAD_V.ipynb for training and testing the model on the AeBAD_V dataset. (**Update**)

TRAIN.MMR.model_chkpt in MMR.yaml is the path of above download model. TRAIN.dataset_path (TEST.dataset_path) is the path of data.
Set Test.save_segmentation_images as True or False to save processed image.

**Note that for AeBAD-V, we only evaluate the sample-level metric. The pixel-level metric is 0.**

## Acknowledgement
I would like to acknowledge the excellent implementation from [MMR](https://github.com/zhangzilongc/MMR)

