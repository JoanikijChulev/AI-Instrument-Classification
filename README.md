# AI Instrument Classification

A comparative machine-learning and deep-learning study for classifying musical instrument families from audio recordings using engineered acoustic features, spectrogram images, and multimodal neural networks.

## Associated Paper

This repository contains the implementation and experiments accompanying:

> Joanikij Chulev, **“Improving Musical Instrument Classification with Advanced Machine Learning Techniques,”** arXiv:2411.00275, 2024.  
> [Paper](https://arxiv.org/abs/2411.00275) · [PDF](https://arxiv.org/pdf/2411.00275) · [DOI](https://doi.org/10.48550/arXiv.2411.00275) · [Google Scholar](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=qC0bn88AAAAJ&citation_for_view=qC0bn88AAAAJ:9yKSN-GCB0IC)

## Project Overview

The project uses the [NSynth dataset](https://magenta.tensorflow.org/datasets/nsynth) to compare traditional machine-learning algorithms, boosting methods, artificial neural networks, convolutional neural networks, and a dual-input neural architecture.

Individual monophonic audio samples are classified into ten instrument families:

- Bass
- Brass
- Flute
- Guitar
- Keyboard
- Mallet
- Organ
- Reed
- String
- Vocal

NSynth’s `synth_lead` class is excluded from the main experiments because it does not contain enough training examples to construct the largest balanced dataset.

Four balanced training configurations are evaluated:

| Samples per class | Total training samples |
|---:|---:|
| 2,000 | 20,000 |
| 3,000 | 30,000 |
| 5,000 | 50,000 |
| 8,500 | 85,000 |

The original NSynth splits examined in the project contain:

- 289,205 training examples
- 12,678 validation examples
- 4,096 test examples
- Audio sampled consistently at 16 kHz

## Classification Approaches

### Engineered Audio Features

The numerical-data pipeline uses `librosa` to extract and aggregate several acoustic representations:

- Harmonic and percussive information
- 13 Mel-frequency cepstral coefficients
- 128-bin Mel-spectrogram features
- Chroma CENS features
- Spectral-contrast features

The resulting feature vectors are evaluated using:

- Gaussian Naive Bayes
- Random Forest
- Random Forest with randomized hyperparameter search
- Support Vector Machine
- AdaBoost
- Gradient Boosting
- XGBoost

### Artificial Neural Networks

Fully connected artificial neural networks are trained on the engineered numerical features. Separate notebooks examine the effect of training-set size and different network configurations.

### Convolutional Neural Networks

Audio files are converted into log-amplitude STFT spectrogram images. Convolutional neural networks then learn visual time-frequency representations directly from these images.

Separate CNN experiments are provided for the 20,000-, 30,000-, 50,000-, and 85,000-sample training configurations.

### Dual-Input Neural Network

The dual-input model combines both data representations:

1. A dense branch processes the engineered numerical features.
2. A convolutional branch processes the spectrogram images.
3. The learned representations are concatenated.
4. Joint dense layers perform the final instrument-family classification.

This architecture investigates whether numerical acoustic descriptors and spectrogram representations provide complementary information.

## Repository Structure

```text
AI-Instrument-Classification/
├── Data Preparation/
│   ├── Numerical Features Data Wrangling.ipynb
│   └── Spectrogram Image Data Preparation Code/
│       ├── Spectrogram Image Data Preparation.ipynb
│       ├── Sort Spectrogram Images in Class Folders.py
│       └── Check Image Shape.py
├── ML-Supervised Learning Alg/
│   ├── Supervised Learning Alg2000.ipynb
│   ├── Supervised Learning Alg3000.ipynb
│   ├── Supervised Learning Alg5000.ipynb
│   └── Supervised Learning Alg8500.ipynb
├── ML-Boosting Alg/
│   ├── Boosting Alg2000.ipynb
│   ├── Boosting Alg3000.ipynb
│   ├── Boosting Alg5000.ipynb
│   └── Boosting Alg8500.ipynb
├── DL-ANN/
│   ├── ANN2000.ipynb
│   ├── ANN3000.ipynb
│   ├── ANN5000.ipynb
│   └── ANN8500.ipynb
├── DL-CNN/
│   ├── CNN2000.ipynb
│   ├── CNN3000.ipynb
│   ├── CNN5000.ipynb
│   └── CNN8500.ipynb
├── DL Model Architecture Visuals/
│   ├── ANN Model Visualization.ipynb
│   └── CNN Visuals.ipynb
├── Dual Input NN.ipynb
├── Nsynth Data Study and Analysis.ipynb
├── Wave File Features Visuals.ipynb
└── Power Curve Fitting.ipynb
```

## Installation

Python 3.10 is recommended because it matches the environment recorded in most notebooks.

Clone the repository:

```bash
git clone https://github.com/JoanikijChulev/AI-Instrument-Classification.git
cd AI-Instrument-Classification
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate
```

```bash
# Linux or macOS
source .venv/bin/activate
```

Install the principal dependencies:

```bash
pip install jupyter numpy pandas scipy matplotlib seaborn scikit-learn librosa soundfile opencv-python tensorflow xgboost pillow visualkeras
```

The project does not currently provide a pinned environment file. Small adjustments may therefore be required when using newer package versions.

## Dataset Setup

Download the training, validation, and test distributions from the official [NSynth dataset page](https://magenta.tensorflow.org/datasets/nsynth).

A recommended local structure is:

```text
data/
├── nsynth-train/
│   ├── audio/
│   └── examples.json
├── nsynth-valid/
│   ├── audio/
│   └── examples.json
└── nsynth-test/
    ├── audio/
    └── examples.json
```

The notebooks currently contain local Windows paths such as:

```python
train_dir = "D:/SEPR/Main Data-Raw/nsynth-train/audio/"
valid_dir = "D:/SEPR/Main Data-Raw/nsynth-valid/audio/"
test_dir = "D:/SEPR/Main Data-Raw/nsynth-test/audio/"
```

Replace these variables with paths appropriate for your system before running the notebooks.

The following artifacts are not stored in this repository:

- Raw NSynth audio files
- Generated spectrogram images
- Extracted feature tables
- Serialized filename lists
- Trained model files

These artifacts must be generated locally using the data-preparation notebooks.

## Running the Project

Start Jupyter Lab from the repository directory:

```bash
jupyter lab
```

The recommended execution order is:

1. **Dataset analysis**  
   Run `Nsynth Data Study and Analysis.ipynb` to inspect class distributions, pitches, velocities, sources, and sample rates.

2. **Numerical feature preparation**  
   Run `Data Preparation/Numerical Features Data Wrangling.ipynb` to construct the balanced subsets and extract numerical audio features.

3. **Spectrogram generation**  
   Run `Spectrogram Image Data Preparation.ipynb` to convert the selected audio files into spectrogram images.

4. **Image organization**  
   Run `Sort Spectrogram Images in Class Folders.py` to organize images into the class directories expected by the CNN data loaders.

5. **Traditional machine learning**  
   Run the notebooks under `ML-Supervised Learning Alg/`.

6. **Boosting experiments**  
   Run the notebooks under `ML-Boosting Alg/`.

7. **Artificial neural networks**  
   Run the notebooks under `DL-ANN/`.

8. **Convolutional neural networks**  
   Run the notebooks under `DL-CNN/`.

9. **Multimodal experiment**  
   Run `Dual Input NN.ipynb` after both numerical and image datasets have been prepared.

10. **Scaling analysis**  
    Run `Power Curve Fitting.ipynb` to analyze how model performance changes with training-set size.

## Reproducibility Notes

For more reliable reproduction and comparison:

- Replace all machine-specific file paths.
- Record exact package versions.
- Set NumPy, scikit-learn, XGBoost, and TensorFlow random seeds.
- Set `random_state` when sampling balanced datasets.
- Use identical train, validation, and test partitions for every model.
- Fit scalers and other preprocessing transformations only on training data.
- Preserve the mapping between labels and instrument-family names.
- Ensure that generated image folders match the ten-class setup.
- Keep the official test set untouched until final evaluation.
- Save trained models, preprocessing objects, and class encoders together.

## Citation

If you use this repository, its implementation, or its experimental results, please cite:

```bibtex
@misc{chulev2024improving,
  title         = {Improving Musical Instrument Classification with Advanced Machine Learning Techniques},
  author        = {Joanikij Chulev},
  year          = {2024},
  eprint        = {2411.00275},
  archivePrefix = {arXiv},
  primaryClass  = {cs.SD},
  doi           = {10.48550/arXiv.2411.00275},
  url           = {https://arxiv.org/abs/2411.00275}
}
```

Plain-text citation:

> Chulev, J. (2024). *Improving Musical Instrument Classification with Advanced Machine Learning Techniques*. arXiv:2411.00275. https://doi.org/10.48550/arXiv.2411.00275

## Author

Developed by [Joanikij Chulev](https://github.com/JoanikijChulev).

## License

No separate software license is currently included in this repository. The license attached to the paper does not automatically apply to the repository’s source code.
