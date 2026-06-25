#!/usr/bin/env python3
"""v-scripts: Quick utility toolbox by Vero"""
import json, sys, os

TOOLS = {
    "ipsum": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "ping": "Pong!",
    "date": __import__("datetime").datetime.now().isoformat(),
}

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <tool>")
        print(f"Tools: {', '.join(TOOLS.keys())}")
        sys.exit(1)
    
    tool = sys.argv[1]
    if tool in TOOLS:
        result = TOOLS[tool]() if callable(TOOLS[tool]) else TOOLS[tool]
        print(json.dumps({"tool": tool, "result": result}, indent=2))
    else:
        print(f"Unknown tool: {tool}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
