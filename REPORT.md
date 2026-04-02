# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Q: What is the agentic loop?**
The agentic loop is the fundamental reasoning cycle that autonomous AI agents use to accomplish tasks. It consists of: Perceive → Reason → Act → Reflect, repeated until the task is complete. More sophisticated agents may also include memory, tool selection, and self-correction.

**Q: What labs are available in our LMS?**
I don't have specific information about your LMS in your workspace. To help you find available labs, I need more information about your LMS setup.

## Task 1B — Agent with LMS tools

**Q: What labs are available?**
Here are the available labs:
1. Lab 01 – Products, Architecture & Roles
2. Lab 02 — Run, Fix, and Deploy a Backend Service
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 — Testing, Front-end, and AI Agents
5. Lab 05 — Data Pipeline and Analytics Dashboard
6. Lab 06 — Build Your Own Agent
7. Lab 07 — Build a Client with an AI Coding Agent
8. lab-08

**Q: Is the LMS backend healthy?**
Yes, the LMS backend is healthy. It currently has 56 items in the system.

## Task 1C — Skill prompt

**Q: Show me the scores**
Agent: Here are the available labs: [list of labs]. Which lab would you like to see the scores for?

## Task 2A — Deployed agent

Startup log excerpt:
🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
✓ Channels enabled: webchat
MCP server 'lms': connected, 9 tools registered
Agent loop started

## Task 2B — Web client

**WebSocket test output:**
```json
{"type":"text","content":"Here are the available labs:\n\n1. **Lab 01** – Products, Architecture & Roles\n2. **Lab 02** — Run, Fix, and Deploy a Backend Service\n3. **Lab 03** — Backend API: Explore, Debug, Implement, Deploy\n4. **Lab 04** — Testing, Front-end, and AI Agents\n5. **Lab 05** — Data Pipeline and Analytics Dashboard\n6. **Lab 06** — Build Your Own Agent\n7. **Lab 07** — Build a Client with an AI Coding Agent\n8. **Lab 08** — lab-08\n\nWould you like to see details for any specific lab?","format":"markdown"}
React dashboard:
Opened http://10.93.25.240:42002/ with LMS_API_KEY=my-secret-api-key. Dashboard loads and shows analytics data.

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
