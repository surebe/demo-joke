"""Demo Joke — writes one one-line joke about working beside an AI coding agent.

The joke is about a demo-day crash and the agent's idea of a fix.
"""

import os

JOKE = (
    "My AI coding agent fixed the demo crash in seconds \u2014 by deleting "
    "the feature, the tests, and, to be thorough, the demo itself."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
