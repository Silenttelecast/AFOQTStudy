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
from image_generator import draw_block_count, draw_rotated_blocks, draw_table_reading, draw_hidden_figures

SUBTESTS = [
    {
        "name": "Verbal Analogies",
        "gen_func": verbal_analogies,
        "time_minutes": 8,
        "num_questions": 25
    },
    {
        "name": "Arithmetic Reasoning",
        "gen_func": arithmetic_reasoning,
        "time_minutes": 29,
        "num_questions": 25
    },
    {
        "name": "Word Knowledge",
        "gen_func": word_knowledge,
        "time_minutes": 5,
        "num_questions": 25
    },
    {
        "name": "Math Knowledge",
        "gen_func": math_knowledge,
        "time_minutes": 22,
        "num_questions": 25
    },
    {
        "name": "Reading Comprehension",
        "gen_func": reading_comprehension,
        "time_minutes": 38,
        "num_questions": 25
    },
    {
        "name": "Instrument Comprehension",
        "gen_func": instrument,
        "time_minutes": 6,
        "num_questions": 20
    },
    {
        "name": "Block Counting",
        "gen_func": block_counting,
        "time_minutes": 4.5,
        "num_questions": 30
    },
    {
        "name": "Table Reading",
        "gen_func": table_reading,
        "time_minutes": 7,
        "num_questions": 40
    },
    {
        "name": "Aviation Information",
        "gen_func": aviation_information,
        "time_minutes": 8,
        "num_questions": 20
    },
    {
        "name": "General Science",
        "gen_func": general_science,
        "time_minutes": 10,
        "num_questions": 20
    },
    {
        "name": "Rotated Blocks",
        "gen_func": rotated_blocks,
        "time_minutes": 13,
        "num_questions": 15
    },
    {
        "name": "Hidden Figures",
        "gen_func": hidden_figures,
        "time_minutes": 8,
        "num_questions": 15
    }
]