"""YatraAI Utilities Module.

This module contains utility functions for YatraAI:
- Gemini API client initialization
"""

from .gemini_client import build_gemini_client

__all__ = [
    "build_gemini_client",
]
