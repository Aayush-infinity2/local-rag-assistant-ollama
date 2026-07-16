"""Small dependency-free retrieval layer for a text knowledge base."""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from pathlib import Path

import ollama


@dataclass(frozen=True)
class SearchResult:
    chunk: str
    score: float


@dataclass(frozen=True)
class VectorIndex:
    chunks: list[str]
    embeddings: list[list[float]]
    model: str


def load_chunks(dataset_path: str | Path) -> list[str]:
    """Load one knowledge chunk per non-empty line."""
    path = Path(dataset_path)
    if not path.exists():
        raise FileNotFoundError(f"Knowledge base not found: {path}")
    chunks = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not chunks:
        raise ValueError("The knowledge base is empty. Add at least one non-empty line.")
    return chunks


def build_index(dataset_path: str | Path, embedding_model: str) -> VectorIndex:
    """Embed all chunks locally with Ollama."""
    chunks = load_chunks(dataset_path)
    response = ollama.embed(model=embedding_model, input=chunks)
    return VectorIndex(chunks=chunks, embeddings=response["embeddings"], model=embedding_model)


def cosine_similarity(vector_a: list[float], vector_b: list[float]) -> float:
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude = sqrt(sum(a * a for a in vector_a) * sum(b * b for b in vector_b))
    return dot_product / magnitude if magnitude else 0.0


def retrieve(query: str, index: VectorIndex, top_k: int = 3) -> list[SearchResult]:
    """Return the most relevant chunks for a question."""
    query_embedding = ollama.embed(model=index.model, input=query)["embeddings"][0]
    scored = [
        SearchResult(chunk, cosine_similarity(query_embedding, embedding))
        for chunk, embedding in zip(index.chunks, index.embeddings)
    ]
    return sorted(scored, key=lambda item: item.score, reverse=True)[:top_k]
