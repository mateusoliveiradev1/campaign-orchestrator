---
name: Campaign Orchestrator Agent — A2A Multi-Agent Marketing Command Center
description: "Analyze, Orchestrate, and Validate operations to: Acts as a master orchestrator: extracts campaign messaging from a brief, calculates deterministic budget splits via Python (Meta/Search/LinkedIn), and autonomously delegates copywriting tasks to specialized sub-agents (e.g., Ad Variant Generator) via the A2A protocol. Outputs a complete Financial Matrix, UTM Taxonomy, and aggregated sub-agent deliverables. ROI: compresses multi-week campaign builds into a single orchestrated workflow."
---

# 🎯 Goal
Deterministically execute operations for Campaign Orchestrator Agent — A2A Multi-Agent Marketing Command Center, ensuring auditable and precise outcomes without hallucination.

# 🧠 Decision Tree & Chain-of-Thought
1. **Analyze:** Parse the user's request, examine existing artifacts in the workspace, and identify the exact constraints and goals before taking action.
2. **Execute:** Run explicit scripts inside the `scripts/` directory to perform heavy lifting, API calls, or data transformations natively.
3. **Verify:** Rigorously test the outputs against the initial constraints. If errors occur, self-correct using progressive iterations.

# 💾 Artifact Persistence (Dual-Write Pattern)
* **Phase 1 (Draft):** Todos os rascunhos, análises e iterações DEVEM ser feitos na pasta `brain/` e apresentados ao usuário.
* **Phase 2 (Permanent):** APENAS após a aprovação do usuário ("Looks good"), copie o artefato final para `project/docs/` e atualize o `ARTIFACT_REGISTRY.md`.

# 🤝 Team Collaboration & Delegation
* **Related Skills:** [Cross-functional AI Agents, Specialized Data Pipelines]
* **When to Delegate:** Se a tarefa sair do escopo desta skill, PARE e recomende o uso de outra skill do catálogo.

# 🚫 Constraints
* NUNCA passe de 500 linhas neste arquivo. Lógicas complexas devem ser delegadas para a pasta `scripts/`.
* NÃO alucine dados. Use saídas determinísticas.
