"""Ollama connectivity and streaming-answer helpers."""

from __future__ import annotations

from collections.abc import Iterator

import ollama

from src.rag import SearchResult


class OllamaUnavailableError(RuntimeError):
    """Raised when the local Ollama server cannot be reached."""


def check_ollama() -> tuple[bool, str]:
    try:
        ollama.list()
        return True, "Ollama is ready."
    except Exception as error:
        return False, str(error)


def stream_answer(
    question: str,
    sources: list[SearchResult],
    history: list[dict[str, str]],
    chat_model: str,
) -> Iterator[str]:
    """Stream a grounded answer from a local model."""
    context = "\n".join(f"- {source.chunk}" for source in sources)
    system_prompt = f"""You are a helpful, concise assistant.
Answer using only the supplied context. If the context does not contain the answer,
say that clearly. Do not invent facts.

Context:
{context}"""
    try:
        stream = ollama.chat(
            model=chat_model,
            messages=[{"role": "system", "content": system_prompt}, *history, {"role": "user", "content": question}],
            stream=True,
        )
        for part in stream:
            yield part["message"]["content"]
    except Exception as error:
        raise OllamaUnavailableError(
            "Could not contact Ollama or load the selected model. "
            "Check that Ollama is running and the model has been pulled."
        ) from error
