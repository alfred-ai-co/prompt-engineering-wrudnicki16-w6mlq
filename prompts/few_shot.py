FEW_SHOT_PROMPT = """
Given the following topic {input}, generate a quiz with 3 questions increasing from beginner to expert in difficulty level.

- a) <choice_1>
- b) <choice_2>
- c) <choice_3>
- d) <choice_4>
- Answer: <single_character_key>

The output should be a JSON Quiz object with the following structure:
{{
  "questions": [
    {{
      "question": "<question_text>",
      "choices": [
        {{"key": "a", "value": "<choice_1>"}},
        {{"key": "b", "value": "<choice_2>"}},
        {{"key": "c", "value": "<choice_3>"}},
        {{"key": "d", "value": "<choice_4>"}}
      ],
      "answer": "<single_character_key>"
    }}
  ]
}}

Examples of a set of questions for Sleep:

1. What is the recommended amount of sleep for adults?
- a) 4-6 hours
- b) 6-8 hours
- c) 7-9 hours
- d) 8-10 hours
- Answer: c

2. What is the term for the inability to fall asleep?
- a) Insomnia
- b) Narcolepsy
- c) Sleep apnea
- d) Sleep paralysis
- Answer: a

3. What part of the brain is responsible for circadian rhythms in the brain?
- a) Thalamus
- b) Amygdala
- c) Hippocampus
- d) Hypothalamus
- Answer: d
"""