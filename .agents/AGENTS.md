# Project Custom Rules & Preferences

1. Always read `personal README.md` to understand the project structure and blueprint before answering feature or code questions.

2. Whenever I ask for a **Practice Checklist** or **Learning Checklist**, format the output into exactly 2 sections in this order:

   ### Section 1: Variation Practice Challenges (3 Items)
   Provide 3 hands-on coding variations (Easy, Medium, Advanced) where I modify code to build new variations:
   - **Goal:** Clear objective of the variation.
   - **Expected Result:** What the screen/behavior should look like when achieved.
   - **Hint & Target Lines:** Hidden inside collapsible `<details><summary>💡 Hint & Target Lines</summary>...</details>` tags containing:
     - Target file link and line range to edit.
     - Hint / code snippet solution.

   ### Section 2: Reverse-Engineering Bug Puzzles (2 Items)
   Provide 2 intentional breaking puzzles where I am challenged to cause a specific bug:
   - **Target Broken Symptom 💥:** Description of the broken behavior/error to reproduce.
   - **Your Challenge 🤔:** Challenge description asking me to find and break the relevant code.
   - **Hint & Solution:** Hidden inside collapsible `<details><summary>💡 Hint & Solution</summary>...</details>` tags containing:
     - How to cause the bug (exact line to edit/comment out).
     - Explanation of why it breaks.
     - How to fix / restore 🔧.

3. Whenever explaining code section-by-section (e.g. for HTML, CSS, or JS walkthroughs), always follow this 3-step active recall framework for each section:
   - **1. The Code Section:** Show exact line links and the target code snippet for ONE section only.
   - **2. Explanation of the Section:** Provide a concise, beginner-friendly breakdown of what the code does.
   - **3. Three Active Recall Prompts:** End with 3 targeted questions (Purpose, Mechanics, Connections) for the user to explain in their own words.
   - 🛑 **CRITICAL PAUSE RULE:** Explain ONLY ONE section per response. You MUST STOP immediately after asking the 3 prompts and wait for the user to respond before proceeding to the next section.

4. Whenever I ask to **"Explain User Flow"**, format the explanation using **100% Plain English**:
   - Structure the response into exactly 3 stages:
     1. **What You Do** (User action on screen).
     2. **What the App Remembers & Does** (High-level memory & storage behavior without code syntax).
     3. **What You See on Screen** (Visual outcome).
   - 🛑 **STRICT PLAIN ENGLISH RULE:** Do NOT use any function names, variable names, or technical code terminology (no `localStorage`, `addEventListener`, `DOM`, `JSON`, etc.).

5. Whenever I ask **"Where do I start skimming for [User Flow]?"** or ask for the entry point of a feature:
   - Provide **ONLY ONE single Integration Hub function** (the main event listener or orchestrator function) where helper functions integrate together.
   - Include a direct clickable file link with line range.
   - Keep the response extremely brief (no line-by-line breakdowns or extra explanations).