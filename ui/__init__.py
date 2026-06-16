"""YatraAI UI package.

Presentation layer for the YatraAI Travel Planner. Pure rendering + light
input handling; it imports from graph/state/utils but nothing here imports back
into the UI package from the backend (one-way dependency, same rule as the rest
of the codebase).

Modules:
  theme        - global design-system CSS (gradients, glassmorphism, typography)
  destinations - curated destination metadata, coordinates, attractions
  nlu          - natural-language trip-request parsing (Gemini + regex fallback)
  hero         - hero / banner section
  chat         - chat-first AI travel assistant
"""
