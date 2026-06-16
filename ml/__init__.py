"""YatraAI Machine Learning Module.

This module contains all ML training, evaluation, and data processing components:
- Data cleaning and preprocessing
- Model training for Budget Allocator and Accommodation Recommender
- Model evaluation on test datasets
- Complete training pipeline orchestration
"""

from .train_pipeline import train_pipeline

__all__ = [
    "train_pipeline",
]
