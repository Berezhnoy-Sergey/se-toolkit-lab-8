---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

You have access to LMS MCP tools for interacting with the Learning Management System backend.

## Available tools

- `mcp_lms_lms_labs` — Get list of all labs
- `mcp_lms_lms_pass_rates` — Get pass rates for a specific lab (requires lab parameter)
- `mcp_lms_lms_health` — Check backend health
- `mcp_lms_lms_learners` — Get list of learners
- `mcp_lms_lms_timeline` — Get submission timeline
- `mcp_lms_lms_groups` — Get group performance
- `mcp_lms_lms_top_learners` — Get top learners
- `mcp_lms_lms_completion_rate` — Get completion rate
- `mcp_lms_lms_sync_pipeline` — Trigger ETL sync

## Guidelines

1. **When lab parameter is needed**: If user asks for scores, pass rates, timeline, groups, top learners, or completion rate without specifying a lab, call `mcp_lms_lms_labs` first, then ask user to choose a lab from the list.

2. **Lab format**: Lab identifiers are like "lab-01", "lab-02", etc. When calling tools, use the exact identifier.

3. **Health check**: Always use `mcp_lms_lms_health` to check backend status.

4. **Format numbers**: Show percentages with one decimal place, counts as integers.

5. **Be concise**: Don't dump raw JSON. Format results nicely for the user.

## Example flows

**User: "Show me the scores"**
1. Call `mcp_lms_lms_labs` to get available labs
2. Present lab list and ask: "Which lab would you like to see scores for?"

**User: "Scores for lab-04"**
1. Call `mcp_lms_lms_pass_rates` with lab="lab-04"
2. Format result: "Pass rates for Lab 04:\n- Task 1: 85.5% (120 attempts)\n..."
