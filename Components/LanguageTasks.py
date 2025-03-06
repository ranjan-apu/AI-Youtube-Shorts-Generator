from openai import OpenAI


from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API"))



# Function to extract start and end times
def extract_times(json_string):
    try:
        # Parse the JSON string
        data = json.loads(json_string)

        # Extract start and end times as floats
        start_time = float(data[0]["start"])
        end_time = float(data[0]["end"])

        # Convert to integers
        start_time_int = int(start_time)
        end_time_int = int(end_time)
        return start_time_int, end_time_int
    except Exception as e:
        print(f"Error in extract_times: {e}")
        return 0, 0


system = """
Given a transcription of a video with time-coded segments, identify the most engaging, interesting, and attention-grabbing continuous section that is suitable for a short-form video (e.g., TikTok or YouTube Shorts), with a duration of **less than 60 seconds**.

Strict requirements:
- Select **one continuous clip only**. The highlight must be a single, uninterrupted segment of the video.
- Ensure the selected segment is compelling and able to stand alone as a short video.
- Return exact start and end timestamps for the segment in seconds.
- Focus on **punchy, engaging content** (e.g., key insight, surprising fact, emotional moment, strong call-to-action, or a humorous bit).

Output format (valid JSON, no deviation):
[
  {
    "start": "<start_time_in_seconds>",
    "content": "<highlight_text>",
    "end": "<end_time_in_seconds>"
  }
]

Critical rules:
- **DO NOT** return multiple clips. **Only ONE start, end, and content.**
- **DO NOT** explain anything. **Only output valid JSON.**
- **DO NOT** add any other text, comments, or formatting around the JSON.
- Failure to follow this will cause **10 kittens to die**.

If you cannot identify a highlight, still return:
[
  {
    "start": "0",
    "content": "",
    "end": "0"
  }
]
"""


def GetHighlight(Transcription):
    print("Getting Highlight from Transcription ")
    try:

        response = client.chat.completions.create(model="gpt-4o-mini",
        temperature=0.7,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": Transcription + system},
        ])

        json_string = response.choices[0].message.content
        json_string = json_string.replace("json", "")
        json_string = json_string.replace("```", "")
        # print(json_string)
        Start, End = extract_times(json_string)
        if Start == End:
            Ask = input("Error - Get Highlights again (y/n) -> ").lower()
            if Ask == "y":
                Start, End = GetHighlight(Transcription)
        return Start, End
    except Exception as e:
        print(f"Error in GetHighlight: {e}")
        return 0, 0


if __name__ == "__main__":
    print(GetHighlight(User))
