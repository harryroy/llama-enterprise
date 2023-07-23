# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

# Importing required modules and functions
import os
from logging import getLogger
from typing import List
from sentencepiece import SentencePieceProcessor

# Initialize logger
logger = getLogger()

# Create a Tokenizer class
class Tokenizer:
    def __init__(self, model_path: str):
        # Check if the model file exists
        assert os.path.isfile(model_path), model_path
        
        # Load SentencePiece model from the provided path
        self.sp_model = SentencePieceProcessor(model_file=model_path)
        logger.info(f"Reloaded SentencePiece model from {model_path}")

        # Initialize BOS (beginning of sentence), EOS (end of sentence), PAD (padding), and total words
        # in the vocabulary from the loaded SentencePiece model
        self.n_words: int = self.sp_model.vocab_size()
        self.bos_id: int = self.sp_model.bos_id()
        self.eos_id: int = self.sp_model.eos_id()
        self.pad_id: int = self.sp_model.pad_id()
        logger.info(
            f"#words: {self.n_words} - BOS ID: {self.bos_id} - EOS ID: {self.eos_id}"
        )
        
        # Assert that the vocab size is equal to the number of pieces in the SentencePiece model
        assert self.sp_model.vocab_size() == self.sp_model.get_piece_size()

    def encode(self, s: str, bos: bool, eos: bool) -> List[int]:
        # Assert input is a string
        assert type(s) is str

        # Tokenize the input string using SentencePiece model
        t = self.sp_model.encode(s)

        # If bos is True, prepend the BOS token to the token list
        if bos:
            t = [self.bos_id] + t

        # If eos is True, append the EOS token to the token list
        if eos:
            t = t + [self.eos_id]
        
        # Return the token list
        return t

    def decode(self, t: List[int]) -> str:
        # Convert the token list back to the string using SentencePiece model
        return self.sp_model.decode(t)
