"""Model Evaluation Module for YatraAI.

This module contains model evaluation functions:
- Budget Allocator evaluation (Regression metrics)
- Accommodation Recommender evaluation (Classification metrics)
- Standalone evaluate_all_models() for calling from main.py
"""

from .evaluate_models import evaluate_models, evaluate_all_models

__all__ = [
    "evaluate_models",
    "evaluate_all_models",
]
