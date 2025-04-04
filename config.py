# config.py
from questions import (
    verbal_analogies,
    arithmetic_reasoning,
    word_knowledge,
    math_knowledge,
    reading_comprehension,
    instrument,
    block_counting,
    table_reading,
    aviation_information,
    general_science,
    rotated_blocks,
    hidden_figures
)

SUBTESTS = [
    {
        "name": "Verbal Analogies",
        "gen_func": verbal_analogies.generate_verbal_analogies_questions,
        "time_minutes": 8
    },
    {
        "name": "Arithmetic Reasoning",
        "gen_func": arithmetic_reasoning.generate_arithmetic_reasoning_questions,
        "time_minutes": 29
    },
    {
        "name": "Word Knowledge",
        "gen_func": word_knowledge.generate_word_knowledge_questions,
        "time_minutes": 5
    },
    {
        "name": "Math Knowledge",
        "gen_func": math_knowledge.generate_math_knowledge_questions,
        "time_minutes": 22
    },
    {
        "name": "Reading Comprehension",
        "gen_func": reading_comprehension.generate_reading_comprehension_questions,
        "time_minutes": 38
    },
    {
        "name": "Instrument Comprehension",
        "gen_func": instrument.generate_instrument_comprehension_questions,
        "time_minutes": 5
    },
    {
        "name": "Block Counting",
        "gen_func": block_counting.generate_block_counting_questions,
        "time_minutes": 3
    },
    {
        "name": "Table Reading",
        "gen_func": table_reading.generate_table_reading_questions,
        "time_minutes": 7
    },
    {
        "name": "Aviation Information",
        "gen_func": aviation_information.generate_aviation_information_questions,
        "time_minutes": 8
    },
    {
        "name": "General Science",
        "gen_func": general_science.generate_general_science_questions,
        "time_minutes": 10
    },
    {
        "name": "Rotated Blocks",
        "gen_func": rotated_blocks.generate_rotated_blocks_questions,
        "time_minutes": 13
    },
    {
        "name": "Hidden Figures",
        "gen_func": hidden_figures.generate_hidden_figures_questions,
        "time_minutes": 8
    }
]