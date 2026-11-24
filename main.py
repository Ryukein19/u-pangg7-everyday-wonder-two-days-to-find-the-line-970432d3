import os
# One-liner entry (200 chars max): the line below is the whole submission.
# Output goes to /output/entry.txt.
LINE = "At 6:47 a.m., the kettle clicks off by itself, and for one second the kitchen is so quiet you can hear the house remembering everyone who ever lived in it."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
