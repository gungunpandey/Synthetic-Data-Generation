# Synthetic Data Generation Using Variational Autoencoders (VAE)

## Overview
This repository contains code, experiments, and results for generating synthetic tabular data using Variational Autoencoders (VAE) and Beta-VAE models. The primary dataset consists of environmental sensor readings with 9 features. The goal is to create high-quality synthetic data that preserves the statistical properties and variability of the original data, making it suitable for robust data science and machine learning applications.

**Note:** This is an ongoing project/experiment. The models, scripts, and results are subject to continuous improvement as new insights are gained.

---

## Project Structure
- **standard_vae/**: Standard VAE implementations and results
- **beta_vae/**: Beta-VAE experiments, enhancements, and synthetic data outputs
- **outputs/**: Plots and summary statistics for real and synthetic data
- **results/**: EDA reports and analysis

---

## Key Approaches & Models
- **Standard VAE**: Baseline model for synthetic data generation
- **Beta-VAE**: Enhanced models with adjustable regularization (beta parameter)
- **Annealed Beta-VAE**: Breakthrough model using gradual beta increase for optimal performance

---

## Parameter Tuning & Improvements
Parameter tuning has been central to improving synthetic data quality. Key areas of experimentation include:

### 1. **Beta Parameter (β) Tuning**
- **Fixed High Beta (4.0, 2.0):** Led to KL loss collapse and poor variance preservation
- **Annealed Beta (0→1):** Gradually increased β during training, preventing KL loss collapse and enabling meaningful latent learning

### 2. **Loss Function Selection**
- **MSE Loss:** Initial experiments
- **MAE Loss:** Provided more stable training and better variance preservation

### 3. **Architecture Adjustments**
- **Latent Dimensions:** Tested 2, 8, and 16; found 8 to be optimal for this dataset
- **Network Depth:** Simpler architectures outperformed deeper, more complex ones

### 4. **Training Dynamics**
- **Early Stopping:** Prevented overfitting and ensured optimal convergence
- **Learning Rate Scheduling:** Improved training stability
- **KL Monitoring:** Separate tracking of KL and reconstruction losses

### 5. **Other Enhancements**
- **Smoother Annealing Schedules:** Tested but found to sometimes worsen results
- **Recommendations:** Future work includes dropout, batch normalization, cyclical annealing, and alternative generative models (CTGAN, TVAE)

---

## Results Summary
- **Standard VAE:** 15-25% variance preservation (limited synthetic data quality)
- **Beta-VAE (Fixed):** 1-2% variance preservation (KL loss collapse)
- **Annealed Beta-VAE:** 53.44% variance preservation, KL loss 0.3220, minimal mode collapse (breakthrough result)
- **Smoother Annealing:** 28% variance preservation, excessive KL loss (over-regularization)

---

## Ongoing Work
This project is actively evolving. Current and future directions include:
- Further tuning of beta schedules and model architectures
- Adding regularization (dropout, batch normalization)
- Exploring alternative generative models (CTGAN, TVAE)
- Testing on additional datasets
- Deploying the best models for production use

---

## How to Use
1. Clone the repository
2. Install dependencies (see requirements.txt)
3. Run the notebooks in `standard_vae/` and `beta_vae/` for experiments
4. Review outputs and results in the `outputs/` and `results/` folders

---

## Contact
For questions, suggestions, or collaboration, please open an issue or contact the project maintainer.
