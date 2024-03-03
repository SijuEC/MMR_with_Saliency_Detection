# IN THE PURSUIT OF A NEW STATE-OF-THE-ART MODEL FOR ANOMALY LOCALIZATION WITH DOMAIN SHIFT

This is an official PyTorch implementation of the Master's Dissertation "IN THE PURSUIT OF A NEW STATE-OF-THE-ART MODEL FOR ANOMALY LOCALIZATION WITH DOMAIN SHIFT".
<br>
This code was implemented on a linux machine. It has to be edited to run on operating systems.
<br>
Save this repository in your home folder under the name "notebooks". This ensures that all the file paths in the config file of this program function properly.


### Dataset

The dataset used for this Thesis is a real-world Aero-engine Blade Anomaly Detection (AeBAD) dataset, consisting of two sub-datasets: the single-blade dataset (AeBAD-S) and the video anomaly detection dataset of blades (AeBAD-V).

* AeBAD-S

<p align="center">
  <img src=assets/image/dataset_s.jpg width="80%">
</p>

* AeBAD-V

<p align="center">
  <img src=assets/image/dataset_v.jpg width="60%">
</p>

**Download the dataset at [here](https://drive.google.com/file/d/14wkZAFFeudlg0NMFLsiGwS0E593b-lNo/view?usp=share_link) (Google Drive) or at [here](https://drive.google.com/file/d/1A5Qj6n2kcJv8gcUsoCQaxtrFb9wjMfGA/view?usp=sharing) (Google Drive).**

The dataset is a zip file. If you run the code inside the jupyter notebook **01_Preparing_AeBAD_dataset.ipynb**, the dataset will be unzipped and the MACOSX version will be deleted.


### Pre-trained models

Download the pre-trained model of MAE (ViT-base) at [here](https://dl.fbaipublicfiles.com/mae/visualize/mae_visualize_vit_base.pth) and save this pth file inside the MMR folder.


### Train and Test for AeBAD

Run the code in **02_MMR_with_saliency_guided_random_masking_AeBAD_S.ipynb** for training and testing the model on the AeBAD_S dataset.<br>
Run the code in **03_MMR_with_saliency_guided_random_masking_AeBAD_V.ipynb** for training and testing the model on the AeBAD_V dataset.

**MMR/method_config/** folder contains the config files for the training and testing runs of this model. <br>
**MMR/method_config/AeBAD_S/MMR.yaml** is relevant for training and testing this model on the AeBAD_S dataset. <br>
**MMR/method_config/AeBAD_V/MMR.yaml** is relevant for training and testing this model on the AeBAD_V dataset. <br>
Inside these yaml files **TRAIN.MMR.model_chkpt** in **MMR.yaml** is the path of above downloaded MAE model. **TRAIN.dataset_path** (TEST.dataset_path) is the path of data.<br>
Set **Test.save_segmentation_images** as True or False to save processed image.<br>
**Note that for AeBAD-V, we only evaluate the sample-level metric. The pixel-level metric is 0.**


## Acknowledgement
I would like to acknowledge the excellent implementation from [MMR](https://github.com/zhangzilongc/MMR)
```
@article{zhang2023industrial,
  title={Industrial Anomaly Detection with Domain Shift: A Real-world Dataset and Masked Multi-scale Reconstruction},
  author={Zhang, Zilong and Zhao, Zhibin and Zhang, Xingwu and Sun, Chuang and Chen, Xuefeng},
  journal={arXiv preprint arXiv:2304.02216},
  year={2023}
}
```


