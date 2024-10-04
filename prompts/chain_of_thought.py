CHAIN_OF_THOUGHT_PROMPT = """
Let's think about this step by step:

Given the following topic {input}, generate a quiz with 5 questions increasing from beginner to expert in difficulty level.

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
"""