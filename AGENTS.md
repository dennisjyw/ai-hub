# AGENTS.md
> [!IMPORTANT]
> **READ SHARED CONFIGURATION FIRST**
> Please read [AGENTS_DOCS.md](file:///Users/denniswang/ai-hub/AGENTS_DOCS.md) for the core rules and configuration.
> Please read [skills/README.md](file:///Users/denniswang/ai-hub/skills/README.md) for available skills.

## Memory System

Persistent memory is stored at `/Users/denniswang/.claude/projects/-Users-denniswang-ai-hub/memory/`.

- Read `MEMORY.md` in that directory at the start of each conversation for context.
- Save new memories (user profile, feedback, project context, references) as individual `.md` files with the required frontmatter (`name`, `description`, `metadata.type`), then add a pointer line to `MEMORY.md`.
- Memory types: `user`, `feedback`, `project`, `reference`. See the auto memory rules in the system prompt for full spec.
