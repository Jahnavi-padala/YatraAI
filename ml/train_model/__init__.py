"""Model Training Module for YatraAI.

This module contains model training functions:
- Budget Allocator model training (Regressor)
- Accommodation Recommender model training (Classifier)
"""

from .train_budget_allocator import train_budget_allocator
from .train_accommodation_recommender import train_accommodation_recommender

__all__ = [
    "train_budget_allocator",
    "train_accommodation_recommender",
]
