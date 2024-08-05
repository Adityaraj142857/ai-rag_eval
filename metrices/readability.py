from __future__ import annotations

import logging
import typing as t # type: ignore
from dataclasses import dataclass # type: ignore
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import textstat

if t.TYPE_CHECKING:
    from langchain_core.callbacks.base import Callbacks

import os
from getpass import getpass

logger = logging.getLogger(__name__)


class readability_score():
    def standard_aggregations(self,scores):
        return {
            "mean": np.mean(scores),
            "variance": np.var(scores),
            "p90": np.percentile(scores, 90),
        }


    def _flesch_kincaid_eval_fn(self,predictions, targets=None, metrics=None):
        try:
            import textstat
        except ImportError:
            logger.warning(
                "Failed to import textstat for flesch kincaid metric, skipping metric logging. "
                "Please install textstat using 'pip install textstat'."
            )
            return
        # print(textstat.flesch_kincaid_grade(predictions))
        scores = textstat.flesch_kincaid_grade(predictions)
        return self.standard_aggregations(scores)
    
Readibility = readability_score()