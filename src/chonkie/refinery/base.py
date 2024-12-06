from abc import ABC, abstractmethod
from typing import List

from chonkie.types import Chunk


class BaseRefinery(ABC):
    """Base class for all Refinery classes.

    Refinery classes are used to refine the Chunks generated from the
    Chunkers. These classes take in chunks and return refined chunks.
    Most refinery classes would be used to add additional context to the
    chunks generated by the chunkers.
    """

    def __init__(self, context_size: int = 0) -> None:
        """Initialize the Refinery."""
        if context_size < 0:
            raise ValueError("context_size must be non-negative")
        self.context_size = context_size

    @abstractmethod
    def refine(self, chunks: List[Chunk]) -> List[Chunk]:
        """Refine the given list of chunks and return the refined list."""
        pass

    @classmethod
    @abstractmethod
    def is_available(cls) -> bool:
        """Check if the Refinery is available."""
        pass

    def __repr__(self) -> str:
        """Representation of the Refinery."""
        return f"{self.__class__.__name__}(context_size={self.context_size})"

    def __call__(self, chunks: List[Chunk]) -> List[Chunk]:
        """Call the Refinery."""
        return self.refine(chunks)
