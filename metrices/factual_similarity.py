from __future__ import annotations

import logging
import typing as t # type: ignore
from dataclasses import dataclass # type: ignore
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

from langchain_google_genai import GoogleGenerativeAIEmbeddings


if t.TYPE_CHECKING:
    from langchain_core.callbacks.base import Callbacks

import os
from getpass import getpass

logger = logging.getLogger(__name__)

class factual_similarity():
    
    name: str = "factual_similarity"  # type: ignore
    # is_cross_encoder: bool = False
    threshold: t.Optional[float] = None

    def embeddings(self,text:str)->list:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key="AIzaSyBdOi80WvlmzgBYoGCUWoir3EAnJKri9pw")
        vector = embeddings.embed_query(text)
        query_result = np.array(vector).reshape(1, -1)
        return query_result

    def similarity_score(self,embd1:list,embd2:list)->float:
        # cosine_similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
        return cosine_similarity(embd1, embd2)[0][0]
    
    def score(self,text1:str,text2:str)->float:
        embed1 = self.embeddings(text1)
        embed2 = self.embeddings(text2)
        score = self.similarity_score(embed1,embed2)

        return score



FactualSimilarity = factual_similarity()