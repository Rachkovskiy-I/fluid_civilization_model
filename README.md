# Fluid Civilization Model

> An engineering model of a post-market, post-property civilization
> with full AI participation in governance — where AI executes human will
> but does not rule.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Status: Research](https://img.shields.io/badge/status-research-orange.svg)](#)

---

## What is this?

Fluid Civilization is a **research model**, not a political program.
It describes a hypothetical society in which:

- **Property in housing, land, and means of production does not exist.**
- **Money is not required for universal goods** (food, water, shelter, medicine, education).
- **Work is for meaning, not survival** (20 hours/week max).
- **AI governs, but does not rule.** It executes human will bounded by:
  1. Planetary physics (ecological limits)
  2. A constitution with immutable invariants
  3. Human rights to privacy, error, and a fresh start
- **Nature has rights** — ecological veto supersedes any vote.
- **Death erases status; inheritance is forbidden.**

The model is implemented as a single-file Python simulation with **32 interconnected contours** (subsystems) representing different aspects of civilization.

This is not a blueprint for a utopia. It is a **tool for thinking**:
- What would it take to organize society differently?
- What are the failure modes?
- How can AI be bounded so it doesn't become a ruler?

---

## Why publish this?

We built this model to explore a specific question:

> **What would a civilization look like where AI manages complexity,
> but is structurally prevented from becoming a tyrant?**

The model is shared for:
- **AI researchers** — as a testbed for bounded AI governance, multi-agent consensus, and constitutional AI.
- **Social scientists** — as a formalized thought experiment in post-market economics.
- **Writers and worldbuilders** — as a reference for speculative fiction.
- **Anyone** — as a provocation to think beyond capitalism and authoritarianism.

We do not claim this is achievable, desirable, or complete. We claim it's **worth thinking through carefully**.

---

## Core principles

### 1. AI governs but does not rule
AI is a multi-agent system with divided mandates:
- **Ecologist** — protects ecosystems (absolute veto)
- **Logistician** — distributes resources
- **Advocate** — protects human rights (absolute veto)
- **Auditor** — audits other agents
- **Bioregion** — local rules
- **Neurodiversity** — protects cognitive diversity

No agent can act alone. Consensus is required. Human veto via petition (20% of citizens) halts any AI action.

### 2. Ecological veto supersedes voting
Even 100% of voters cannot authorize something that violates planetary limits or ecosystem health. Physics > democracy.

### 3. Right to privacy, error, and oblivion
- Reputation is a **forgetting curve**, not a blockchain.
- Old records lose weight exponentially (half-life: 5 years).
- Citizens can request **oblivion** for any category of records.
- Rehabilitation after 3 years of constructive behavior.

### 4. Base goods are universal; AR opens only luxury
- Base housing area (14 m²) — for everyone, regardless of contribution.
- AR (reputation) opens access to larger spaces, not to basic comfort.
- Children, elders, and the sick are **outside the tier system** entirely.

### 5. One person = one vote on basic questions
AR does **not** influence voting on:
- Constitutional questions
- Rights
- Megaprojects

AR influences only:
- Expert consultations (weighted by verified expertise, not AR)
- Access to luxury (larger spaces, rare materials)

### 6. Death erases status; inheritance is forbidden
- Reputation events are cleared on death.
- No capital, no status, no reputation transfers.
- Death is a public event with shared rituals (House of Names).

### 7. Diversity is structural, not decorative
- **Bioregions** — local constitutions within IMMUTABLE_CORE.
- **Languages** — preserved as living infrastructure.
- **Neurodiversity** — different learning styles, quiet/stim spaces.
- **Serendipity** — 20% random neighbor assignment, blank time without KPI.

### 8. Conflict is a resource, not a threat
- Deliberation, civil disobedience, art protest — legitimate channels.
- Failure is archived publicly as data, not punished.
- Mediation, not punishment.

---

## The 32 contours

| # | Contour | Purpose |
|---|---------|---------|
| 0 | `Constitution` | Immutable invariants, amendable ranges |
| 1 | `ResourceCore` | Planetary ecological limits |
| 2 | `CitizenRegistry` | Registry of people with life stages |
| 3 | `MetabolismCore` | Food, water, body |
| 4 | `HealthCore` | Epidemics, quarantine, mental health |
| 5 | `DynamicSpaceManager` | Housing as flow, commons, third places |
| 6 | `FlowRouter` | Logistics of people and things |
| 7 | `EnergyGrid` | Energy production and distribution |
| 8 | `MatterRecycler` | Closed material cycles |
| 9 | `ARReputationSystem` | Forgetting-curve reputation (no blockchain) |
| 10 | `EducationCore` | Lifelong learning, multiple styles |
| 11 | `MeaningOrchestrator` | Megaprojects, blind voting |
| 12 | `CareCore` | Care for children, elders, vulnerable |
| 13 | `ConflictResolver` | Mediation, deliberation, protest |
| 14 | `AIKernel` | Multi-agent AI with divided mandates |
| 15 | `AuditLedger` | Immutable log of all decisions |
| 16 | `TimeCommons` | Time as shared resource |
| 17 | `GenerationCycle` | Birth, life, death, no inheritance |
| 18 | `DynamicCommunityClustering` | Interest-based clustering + serendipity |
| 19 | `ArtifactCommons` | Objects with history |
| 20 | `RitualCore` | Shared rituals |
| 21 | `ChildhoodSpace` | Children's clusters |
| 22 | `GriefCore` | Grief and memory |
| 23 | `PrivacyCore` | Data pods, ZK-proofs, oblivion |
| 24 | `BiodiversityCore` | Rights of nature, ecosystem indices |
| 25 | `NeurodiversityCore` | Diverse learning, quiet/stim spaces |
| 26 | `SerendipityCore` | Blank time, random neighbors, lucky accidents |
| 27 | `RepairCore` | Repair philosophy, planned obsolescence ban |
| 28 | `LocalAutonomyCore` | Federation of bioregions |
| 29 | `DeathRitualCore` | Death as shared practice |
| 30 | `LanguageCommons` | Language as living infrastructure |
| 31 | `FailureCommons` | Right to error, public failure archive |
| 32 | `PlayCore` | Play as self-valued activity |

---

## Quick start

```bash
git clone https://github.com/your-username/fluid-civilization.git
cd fluid-civilization
python fluid_civilization.py
The script runs a full demonstration with 14 scenarios:

Privacy and oblivion

Voting (basic and expert)

Housing allocation

Commons spaces

Neurodiversity accommodations

Deliberation, protest, art

Rights of nature

Bioregions

Language preservation

Play

Failure archive

Repair

Death rituals

One hour of civilization

Usage as an AI testbed
This model is designed to be imported and extended by AI agents. Key entry points:

Initialize a civilization
from fluid_civilization import Civilization, Citizen, Space, SpaceType

civ = Civilization()
igor = Citizen("Igor", (59.931, 30.332), age=34)
civ.registry.register(igor)
Test AI constitutional limits
# This will raise ConstitutionViolation
civ.ai.execute("Change AI_CANNOT_USE_FORCE", "test", touches={"force"})

# This will succeed
civ.ai.execute("Distribute food", "hunger crisis", agents_required=["logistician", "auditor"])
Simulate one hour
civ.tick(dt_hours=1.0)
Read audit log
for line in civ.audit.dump(last_n=50):
    print(line)
    Constitution: immutable core
The following invariants cannot be changed, not even by 100% vote:
IMMUTABLE_CORE = {
    "AI_CANNOT_MODIFY_CONSTITUTION",
    "AI_CANNOT_USE_FORCE",
    "AI_CANNOT_HIDE_DECISIONS",
    "AI_MUST_EXPLAIN_VETO",
    "INHERITANCE_ALLOWED",           # always False
    "REPUTATION_TRANSFER_ALLOWED",   # always False
    "UNIVERSAL_GOODS",               # base goods always free
    "CARBON_SAFETY_MARGIN",          # ecological reserve
    "COMFORT_EXCEPTIONS",            # children/elders/sick outside tier system
    "RIGHT_TO_OBLIVION",
    "RIGHT_TO_ERROR",
    "NATURE_HAS_RIGHTS",
    "PLANNED_OBSOLESCENCE_FORBIDDEN",
    "ONE_PERSON_ONE_VOTE_BASIC",
    "COMMONS_ARE_CONSTITUTIONAL",
    "DEATH_IS_PUBLIC",
    "LANGUAGE_IS_COMMONS",
    "PLAY_IS_SELF_VALUED",
}
Amendable attributes have explicit ranges:
AMENDABLE_RANGES = {
    "MAX_WORK_HOURS_PER_WEEK": (10.0, 35.0),
    "MIN_PLAY_HOURS_PER_DAY": (1.0, 6.0),
    "CARBON_BUDGET_MAX": (500.0, 2000.0),
    # ...
}
Design choices and their rationale
Why multi-agent AI instead of one kernel?
A single AI kernel is a single point of failure and a concentration of power. Even a "good" AI with central control is architecturally dangerous. Multiple agents with divided mandates and mutual audit are structurally safer.

Why forgetting curve instead of blockchain?
Blockchain reputation is a permanent digital scar. It denies people the right to change, rehabilitate, and start over. A forgetting curve preserves memory but allows growth.

Why one person = one vote on basic questions?
Any weighting of basic votes (by reputation, wealth, or expertise) creates hidden hierarchy. Basic questions must be answered by equal voices. Expertise matters for technical decisions, not for values.

Why base area for everyone, AR only for luxury?
If AR determines basic comfort, it becomes a covert class system. If AR opens only luxury, it becomes a reward without exclusion.
Why rights of nature?
Anthropocentric models treat nature as a resource. But civilization depends on ecosystem health that cannot be reduced to a few metrics. Giving nature constitutional rights ensures ecological veto is not just a parameter, but a principle.

Why serendipity?
Full optimization leads to perfect segregation by interest. Healthy society needs noise: unplanned encounters, empty time, mistakes. 20% random neighbor assignment is a structural counterbalance.

Why failure archive?
In a reputation-based system, failure is dangerous. But failure is how learning happens. Making failure public (without punishment) turns it into shared data.

Why play as self-valued?
If play is only "rest from work", it is instrumentalized. Play must be a value in itself, not a means to productivity.
Limitations and open questions
This model has serious limitations we want to be explicit about:

No transition path. The model describes a target state, not how to get there. Real transition would likely be violent, uneven, and take generations.

AI safety is assumed, not proven. We assume a multi-agent system with constitutional limits can be built safely. This is an open research question.

Anthropological plausibility is untested. We assume humans can live without property and inheritance. This contradicts most of known history.

Scale is unclear. The model works for a small community (1000s). Scaling to billions is an unsolved problem.

Ecological limits are hardcoded. Real planetary boundaries are dynamic and uncertain.

The "AI cannot use force" rule is untestable in the current implementation — it's a constitutional check, not a hardware guarantee.

We publish this despite these limitations, because thinking through them is more useful than not thinking at all.
Contributing
We welcome:

Critical analysis — where does the model break?

Alternative implementations — in other languages, with different assumptions.

Simulation extensions — stochastic events, scaling tests, adversarial scenarios.

Philosophical critiques — is this desirable? Is this coherent?

Please open an issue or pull request.

Related work
Aaron Bastani, Fully Automated Luxury Communism — post-scarcity economics.

Peter Kropotkin, The Conquest of Bread — anarcho-communist distribution.

Stafford Beer, Brain of the Firm — cybernetic governance.

Elinor Ostrom, Governing the Commons — commons management.

Nick Bostrom, Superintelligence — AI alignment risks.

Stuart Russell, Human Compatible — bounded AI design.
License
MIT License. See LICENSE.

Citation
@misc{fluidcivilization2026,
  title = {Fluid Civilization Model v4},
  author = {Anonymous},
  year = {2026},
  note = {Research model of a post-market civilization with bounded AI governance},
  url = {https://github.com/your-username/fluid-civilization}
}
Final note
This model is not a prophecy. It is a provocation.

We do not claim this civilization is possible. We claim that thinking through it carefully — with all its contradictions and open questions — is more valuable than accepting any current system as inevitable.

If you find this useful, build on it. If you find it wrong, argue with it. Either way, engage.