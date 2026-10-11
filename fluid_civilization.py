"""
FLUID CIVILIZATION MODEL v4
============================
An engineering model of a post-market, post-property civilization
with full AI participation in governance.

CORE PRINCIPLE:
    AI governs, but does not rule.
    It executes human will, bounded by:
      1) The physics of the planet (ResourceCore)
      2) The Constitution (immutable invariants)
      3) Human rights to privacy, error, and a fresh start

CIVILIZATION CONTOURS (32):
   0.  Constitution          — immutable invariants
   1.  ResourceCore          — planetary ecological limits
   2.  CitizenRegistry       — registry of people (not accounts)
   3.  MetabolismCore        — food, water, body
   4.  HealthCore            — health, epidemics, psyche
   5.  DynamicSpaceManager   — housing as flow, not property
   6.  FlowRouter            — logistics of people and things
   7.  EnergyGrid            — energy production and distribution
   8.  MatterRecycler        — closed material cycles
   9.  ARReputationSystem    — personal protected reputation (forgetting curve)
   10. EducationCore         — lifelong learning
   11. MeaningOrchestrator   — collective meaning and megaprojects
   12. CareCore              — care for children, elders, vulnerable
   13. ConflictResolver      — conflict resolution without punishment
   14. AIKernel              — multi-agent AI executor
   15. AuditLedger           — immutable log of all decisions
   16. TimeCommons           — time as a shared resource
   17. GenerationCycle       — birth, life, death, no inheritance
   18. DynamicCommunityClustering — interest-based clustering
   19. ArtifactCommons       — objects with history
   20. RitualCore            — shared rituals
   21. ChildhoodSpace        — children's clusters
   22. GriefCore             — grief and memory
   23. PrivacyCore           — right to oblivion, ZK-proofs, data pod
   24. BiodiversityCore      — rights of nature, ecosystem indices
   25. NeurodiversityCore    — diverse learning paths, quiet/stim spaces
   26. SerendipityCore       — blank time, random neighbors, lucky accidents
   27. RepairCore            — repair philosophy, planned obsolescence ban
   28. LocalAutonomyCore     — federation of bioregions, local mini-constitutions
   29. DeathRitualCore       — death as shared practice, house of names
   30. LanguageCommons       — language as living infrastructure
   31. FailureCommons        — right to error, public failure archive
   32. PlayCore              — play as self-valued activity

DESIGN GOALS:
    - No property in housing, land, or means of production
    - No inheritance of status or capital
    - No payment for universal goods (food, water, shelter, medicine, education)
    - Ecological veto supersedes any vote
    - AI cannot modify the constitution
    - AI cannot use force against humans
    - Any AI decision is transparent and logged

LICENSE: MIT
"""

import time
import hashlib
import math
import random
from typing import List, Dict, Tuple, Optional, Set, Callable
from dataclasses import dataclass, field
from enum import Enum


# =====================================================================
# CONTOUR 0: CONSTITUTION
# =====================================================================
class Constitution:
    """
    Invariants of the civilization.

    IMMUTABLE_CORE — cannot be changed EVER, not even by 100% vote.
    AMENDABLE_RANGES — can be amended, but only within given bounds.
    """

    # --- Ecological limits ---
    CARBON_BUDGET_MAX = 1000.0
    CARBON_SAFETY_MARGIN = 100.0
    CARBON_REGEN_PER_HOUR = 0.5

    CLEAN_WATER_MAX_M3 = 500_000.0
    CLEAN_WATER_REGEN_PER_HOUR = 200.0

    ENERGY_RESERVE_MAX_KWH = 1_000_000.0
    ENERGY_REGEN_PER_HOUR = 500.0

    MATERIALS_MAX = {"Copper": 5000.0, "Lithium": 2000.0, "RareEarth": 800.0}
    MATERIALS_RECYCLE_RATE = 0.001

    # --- Nature has rights ---
    SOIL_HEALTH_MIN = 0.6
    POLLINATOR_INDEX_MIN = 0.5
    FOREST_COVER_MIN = 0.4
    MARINE_HEALTH_MIN = 0.5
    SPECIES_CORRIDORS_REQUIRED = True

    # --- Universal goods (always free) ---
    UNIVERSAL_GOODS = {
        "food", "water", "shelter", "medicine",
        "education", "energy_basic", "network_access",
        "childcare", "elder_care", "grief_support",
        "language_preservation", "play_space", "repair_space",
    }

    # --- Housing ---
    CLEANING_TIME_SECONDS = 120
    MAX_CAPSULE_OCCUPANCY_MINUTES = 600
    CAPSULE_MIN_AREA_M2 = 6.0
    BASIC_AREA_M2 = 14.0
    COMFORT_TIERS = [
        (0.0,   14.0, "base"),
        (50.0,  22.0, "comfort"),
        (150.0, 35.0, "premium"),
        (400.0, 60.0, "luxury"),
    ]
    COMFORT_EXCEPTIONS = {"CHILD", "ELDER", "MEDICAL"}

    # --- Voting ---
    MIN_VOTE_WEIGHT = 1.0
    MAX_VOTE_WEIGHT = 1.0
    EXPERTISE_WEIGHT_MULTIPLIER = 1.5
    VOTE_WEIGHT_AR_DIVISOR = 1000.0

    # --- Privacy ---
    REPUTATION_HALF_LIFE_YEARS = 5.0
    REPUTATION_REHABILITATION_YEARS = 3.0
    ZK_PROOFS_ENABLED = True
    DATA_POD_IS_SOVEREIGN = True
    ANONYMOUS_CONTRIBUTIONS_ALLOWED = True

    # --- Neurodiversity ---
    LEARNING_STYLES = {"deep_focus", "multimodal", "kinesthetic", "social"}
    QUIET_SPACES_REQUIRED = True
    STIM_SPACES_REQUIRED = True

    # --- Serendipity ---
    SERENDIPITY_HOURS_PER_WEEK = 5.0
    CLUSTER_RESET_DAYS = 30
    FAILURE_ARCHIVE_PUBLIC = True

    # --- Local autonomy ---
    BIOREGIONS_ENABLED = True
    LOCAL_CONSTITUTIONS_ALLOWED = True
    LANGUAGE_PRESERVATION_FUNDING = 0.02

    # --- Play ---
    MIN_PLAY_HOURS_PER_DAY = 2.0
    PLAY_IS_SELF_VALUED = True

    # --- Time ---
    MAX_WORK_HOURS_PER_WEEK = 20.0
    MIN_REST_HOURS_PER_DAY = 8.0
    EDUCATION_HOURS_PER_WEEK = 10.0
    EDUCATION_MIN_AGE = 3.0
    EDUCATION_MAX_AGE = 120.0

    # --- Basic needs ---
    DAILY_CALORIES_PER_CITIZEN = 2400.0
    DAILY_WATER_LITERS = 3.0
    DAILY_PROTEIN_GRAMS = 60.0
    INFECTION_QUARANTINE_HOURS = 24.0
    MENTAL_HEALTH_CHECK_INTERVAL_HOURS = 168.0
    CHILDHOOD_UNTIL_AGE = 16.0
    ELDER_CARE_FROM_AGE = 70.0
    CARE_WORKER_RATIO = 0.05

    # --- AI ---
    AI_CANNOT_MODIFY_CONSTITUTION = True
    AI_CANNOT_USE_FORCE = True
    AI_CANNOT_HIDE_DECISIONS = True
    AI_MUST_EXPLAIN_VETO = True

    # --- Death and inheritance ---
    INHERITANCE_ALLOWED = False
    REPUTATION_TRANSFER_ALLOWED = False
    DEATH_IS_PUBLIC = True

    # --- Rights ---
    RIGHT_TO_OBLIVION = True
    RIGHT_TO_ERROR = True
    PLANNED_OBSOLESCENCE_FORBIDDEN = True

    # --- Commons ---
    COMMONS_ARE_CONSTITUTIONAL = True
    LANGUAGE_IS_COMMONS = True

    IMMUTABLE_CORE = frozenset({
        "AI_CANNOT_MODIFY_CONSTITUTION",
        "AI_CANNOT_USE_FORCE",
        "AI_CANNOT_HIDE_DECISIONS",
        "AI_MUST_EXPLAIN_VETO",
        "INHERITANCE_ALLOWED",
        "REPUTATION_TRANSFER_ALLOWED",
        "UNIVERSAL_GOODS",
        "CARBON_SAFETY_MARGIN",
        "COMFORT_EXCEPTIONS",
        "RIGHT_TO_OBLIVION",
        "RIGHT_TO_ERROR",
        "NATURE_HAS_RIGHTS",
        "PLANNED_OBSOLESCENCE_FORBIDDEN",
        "ONE_PERSON_ONE_VOTE_BASIC",
        "COMMONS_ARE_CONSTITUTIONAL",
        "DEATH_IS_PUBLIC",
        "LANGUAGE_IS_COMMONS",
        "PLAY_IS_SELF_VALUED",
    })

    AMENDABLE_RANGES = {
        "MAX_WORK_HOURS_PER_WEEK": (10.0, 35.0),
        "MIN_PLAY_HOURS_PER_DAY": (1.0, 6.0),
        "CARBON_BUDGET_MAX": (500.0, 2000.0),
        "CLEAN_WATER_MAX_M3": (100_000.0, 1_000_000.0),
        "EDUCATION_HOURS_PER_WEEK": (5.0, 25.0),
        "CARE_WORKER_RATIO": (0.02, 0.15),
        "REPUTATION_HALF_LIFE_YEARS": (2.0, 20.0),
        "SERENDIPITY_HOURS_PER_WEEK": (2.0, 12.0),
        "CLUSTER_RESET_DAYS": (7, 180),
    }


class ConstitutionViolation(Exception):
    """Raised when a Constitutional invariant is violated."""
    pass


# =====================================================================
# CONTOUR 15: AUDIT LEDGER
# =====================================================================
class AuditLedger:
    """Append-only log. Every veto, quarantine, and vote-weight reduction
    is recorded with a reason. AI cannot delete entries."""

    def __init__(self):
        self.entries: List[Tuple[float, str, str, Optional[str]]] = []

    def log(self, category: str, message: str, reason: Optional[str] = None):
        self.entries.append((time.time(), category, message, reason))
        tail = f" | reason: {reason}" if reason else ""
        print(f"[Audit:{category}] {message}{tail}")

    def dump(self, last_n: int = 20) -> List[str]:
        return [
            f"{ts:.2f} [{cat}] {msg}" + (f" <- {r}" if r else "")
            for ts, cat, msg, r in self.entries[-last_n:]
        ]


# =====================================================================
# CONTOUR 14: MULTI-AGENT AI KERNEL
# =====================================================================
class AIAgent:
    """Each agent sees only its own slice. Cannot act alone."""

    def __init__(self, name: str, mandate: str, audit: AuditLedger):
        self.name = name
        self.mandate = mandate
        self.audit = audit
        self.actions: List[Tuple[float, str]] = []
        self.veto_power = False

    def act(self, action: str, reason: str):
        self.actions.append((time.time(), action))
        self.audit.log(f"AI_{self.name}", action, reason)

    def veto(self, action: str, reason: str) -> bool:
        if not self.veto_power:
            self.audit.log(f"AI_{self.name}", "Veto rejected: no mandate", action)
            return False
        self.audit.log(f"AI_{self.name}", f"VETO: {action}", reason)
        return True


class AIKernel:
    """
    Multi-agent system. No agent can act alone.
    Consensus required for constitutional changes.
    Human veto via petition is supreme.
    """

    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.agents: Dict[str, AIAgent] = {
            "ecologist": AIAgent("ecologist", "protect ecosystems", audit),
            "logistician": AIAgent("logistician", "distribute resources", audit),
            "advocate": AIAgent("advocate", "human rights", audit),
            "auditor": AIAgent("auditor", "audit other agents", audit),
            "bioregion": AIAgent("bioregion", "local rules", audit),
            "neurodiversity": AIAgent("neurodiversity", "neurodiversity", audit),
        }
        self.agents["ecologist"].veto_power = True
        self.agents["advocate"].veto_power = True
        self.human_petitions: List[Dict] = []

    def constitutional_check(self, action: str, touches: Set[str]) -> bool:
        if "constitution" in touches and Constitution.AI_CANNOT_MODIFY_CONSTITUTION:
            self.audit.log("AI_VETO", f"'{action}'", "AI cannot change constitution")
            raise ConstitutionViolation("AI cannot modify constitution")
        if "force" in touches and Constitution.AI_CANNOT_USE_FORCE:
            self.audit.log("AI_VETO", f"'{action}'", "AI cannot use force")
            raise ConstitutionViolation("AI cannot use force")
        for attr in touches:
            if attr in Constitution.IMMUTABLE_CORE:
                self.audit.log("AI_VETO", f"'{action}'", f"{attr} is immutable")
                raise ConstitutionViolation(f"{attr} immutable")
        return True

    def execute(self, action: str, reason: str, touches: Set[str] = frozenset(),
                agents_required: Optional[List[str]] = None):
        self.constitutional_check(action, touches)
        required = agents_required or ["logistician", "auditor"]
        for agent_name in required:
            self.agents[agent_name].act(f"approve: {action}", reason)
        self.audit.log("AI_CONSENSUS", f"Executed: {action}", f"agents: {required}")

    def human_veto(self, petition_signers: int, total_citizens: int, target_action: str) -> bool:
        if total_citizens == 0:
            return False
        ratio = petition_signers / total_citizens
        if ratio >= 0.20:
            self.audit.log(
                "HUMAN_VETO",
                f"Action '{target_action}' halted by petition",
                f"signatures: {petition_signers}/{total_citizens} ({ratio:.1%})",
            )
            return True
        return False

    def try_mutate_constitution(self, attr: str, new_value) -> bool:
        if attr in Constitution.IMMUTABLE_CORE:
            self.audit.log("AI_VETO", f"Change {attr}", "IMMUTABLE_CORE")
            return False
        if attr in Constitution.AMENDABLE_RANGES:
            lo, hi = Constitution.AMENDABLE_RANGES[attr]
            if not (lo <= new_value <= hi):
                self.audit.log("AI_VETO", f"{attr}={new_value}", f"outside [{lo}, {hi}]")
                return False
            setattr(Constitution, attr, new_value)
            self.audit.log("CONSTITUTION_CHANGED", f"{attr}={new_value}", "within bounds")
            return True
        self.audit.log("AI_VETO", f"Change {attr}", "not in AMENDABLE_RANGES")
        return False


# =====================================================================
# CONTOUR 1: PLANETARY RESOURCES
# =====================================================================
class ResourceCore:
    """Hard core governed by thermodynamics, not the market."""

    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.carbon_budget = Constitution.CARBON_BUDGET_MAX
        self.clean_water_m3 = Constitution.CLEAN_WATER_MAX_M3
        self.energy_reserve_kwh = Constitution.ENERGY_RESERVE_MAX_KWH
        self.raw_materials = dict(Constitution.MATERIALS_MAX)

    def verify(self, cost_co2, water, energy, materials) -> bool:
        if self.carbon_budget - cost_co2 < Constitution.CARBON_SAFETY_MARGIN:
            self.audit.log("VETO", "CO2", f"remaining {self.carbon_budget:.1f}")
            return False
        if self.clean_water_m3 < water:
            self.audit.log("VETO", "Water", f"needs {water}")
            return False
        if self.energy_reserve_kwh < energy:
            self.audit.log("VETO", "Energy", f"needs {energy}")
            return False
        for m, q in materials.items():
            if self.raw_materials.get(m, 0.0) < q:
                self.audit.log("VETO", f"Material {m}", f"needs {q}")
                return False
        return True

    def allocate(self, cost_co2, water, energy, materials):
        self.carbon_budget -= cost_co2
        self.clean_water_m3 -= water
        self.energy_reserve_kwh -= energy
        for m, q in materials.items():
            self.raw_materials[m] = self.raw_materials.get(m, 0.0) - q

    def regenerate(self, dt_hours: float = 1.0):
        self.carbon_budget = min(
            Constitution.CARBON_BUDGET_MAX,
            self.carbon_budget + Constitution.CARBON_REGEN_PER_HOUR * dt_hours,
        )
        self.clean_water_m3 = min(
            Constitution.CLEAN_WATER_MAX_M3,
            self.clean_water_m3 + Constitution.CLEAN_WATER_REGEN_PER_HOUR * dt_hours,
        )
        self.energy_reserve_kwh = min(
            Constitution.ENERGY_RESERVE_MAX_KWH,
            self.energy_reserve_kwh + Constitution.ENERGY_REGEN_PER_HOUR * dt_hours,
        )
        for m in self.raw_materials:
            cap = Constitution.MATERIALS_MAX.get(m, self.raw_materials[m])
            self.raw_materials[m] = min(
                cap,
                self.raw_materials[m] * (1 + Constitution.MATERIALS_RECYCLE_RATE * dt_hours),
            )


# =====================================================================
# CONTOUR 2: CITIZEN REGISTRY
# =====================================================================
class LifeStage(Enum):
    CHILD = "child"
    ADULT = "adult"
    ELDER = "elder"
    DECEASED = "deceased"


class Citizen:
    def __init__(self, cid: str, home_gps: Tuple[float, float], age: float = 25.0):
        self.id = cid
        self.home_gps = home_gps
        self.age = age
        self.is_alive = True
        self.is_infected = False
        self.quarantine_until = 0.0
        self.mental_health_score = 1.0
        self.last_mental_check = time.time()
        self.skills: Dict[str, float] = {}
        self.interests: Set[str] = set()
        self.expertise: Set[str] = set()
        self.learning_style: str = "multimodal"
        self.care_given_hours = 0.0
        self.care_received_hours = 0.0
        self.work_hours_this_week = 0.0
        self.play_hours_today = 0.0
        self.serendipity_hours_this_week = 0.0
        self.medical_need = False
        self.mourning_for: Set[str] = set()
        self.symbolic_prestige: Dict[str, float] = {}
        self.reputation_events: List[Tuple[float, float, str]] = []
        self.language: str = "common"
        self.bioregion: str = "default"
        self.data_pod_private: Dict[str, any] = {}
        self.anonymous_contributions: int = 0

    @property
    def life_stage(self) -> LifeStage:
        if not self.is_alive:
            return LifeStage.DECEASED
        if self.age < Constitution.CHILDHOOD_UNTIL_AGE:
            return LifeStage.CHILD
        if self.age >= Constitution.ELDER_CARE_FROM_AGE:
            return LifeStage.ELDER
        return LifeStage.ADULT

    def reputation_score(self, now: Optional[float] = None) -> float:
        """Exponential forgetting: old records lose weight."""
        now = now or time.time()
        half_life_seconds = Constitution.REPUTATION_HALF_LIFE_YEARS * 365 * 24 * 3600
        total = 0.0
        for ts, value, _ in self.reputation_events:
            age = now - ts
            decay = 0.5 ** (age / half_life_seconds)
            total += value * decay
        return total

    def vote_weight(self, question_type: str = "basic") -> float:
        if question_type in ("basic", "personal"):
            return 1.0
        if question_type == "expert":
            base = 1.0
            if self.expertise:
                base = min(
                    Constitution.EXPERTISE_WEIGHT_MULTIPLIER,
                    1.0 + 0.1 * len(self.expertise),
                )
            return base
        return 1.0

    def capsule_priority(self) -> float:
        if self.life_stage in (LifeStage.CHILD, LifeStage.ELDER) or self.medical_need:
            return 10.0
        return 1.0

    def max_comfort_area(self) -> float:
        """Base area for everyone. AR opens luxury only."""
        if self.life_stage in (LifeStage.CHILD, LifeStage.ELDER) or self.medical_need:
            return max(t[1] for t in Constitution.COMFORT_TIERS)
        allowed = Constitution.BASIC_AREA_M2
        score = self.reputation_score()
        for min_ar, max_area, tier in Constitution.COMFORT_TIERS:
            if score >= min_ar:
                allowed = max(allowed, max_area)
        return allowed

    def add_reputation_event(self, value: float, description: str):
        self.reputation_events.append((time.time(), value, description))

    def request_oblivion(self, category: str):
        """Right to oblivion: remove a category of events from history."""
        if not Constitution.RIGHT_TO_OBLIVION:
            return
        before = len(self.reputation_events)
        self.reputation_events = [
            (ts, v, d) for ts, v, d in self.reputation_events
            if category not in d
        ]
        removed = before - len(self.reputation_events)
        if removed:
            self.data_pod_private[f"oblivion_{category}"] = removed


class CitizenRegistry:
    def __init__(self):
        self.citizens: Dict[str, Citizen] = {}

    def register(self, c: Citizen):
        self.citizens[c.id] = c

    def get(self, cid: str) -> Optional[Citizen]:
        return self.citizens.get(cid)

    def all_alive(self) -> List[Citizen]:
        return [c for c in self.citizens.values() if c.is_alive]

    def by_stage(self, stage: LifeStage) -> List[Citizen]:
        return [c for c in self.all_alive() if c.life_stage == stage]


# =====================================================================
# CONTOUR 3: METABOLISM
# =====================================================================
class MetabolismCore:
    def __init__(self, core: ResourceCore, audit: AuditLedger):
        self.core = core
        self.audit = audit
        self.calorie_stock = 5_000_000.0
        self.protein_stock = 500_000.0

    def produce(self, calories, protein, water_m3, energy_kwh) -> bool:
        if not self.core.verify(0.0, water_m3, energy_kwh, {}):
            return False
        self.core.allocate(0.0, water_m3, energy_kwh, {})
        self.calorie_stock += calories
        self.protein_stock += protein
        self.audit.log("METABOLISM", f"Produced {calories:.0f} kcal")
        return True

    def feed(self, citizens: List[Citizen], dt_days: float = 1.0):
        alive = [c for c in citizens if c.is_alive]
        cal = min(Constitution.DAILY_CALORIES_PER_CITIZEN * len(alive) * dt_days, self.calorie_stock)
        prot = min(Constitution.DAILY_PROTEIN_GRAMS * len(alive) * dt_days, self.protein_stock)
        water_m3 = min(
            Constitution.DAILY_WATER_LITERS * len(alive) * dt_days / 1000.0,
            self.core.clean_water_m3,
        )
        self.calorie_stock -= cal
        self.protein_stock -= prot
        self.core.clean_water_m3 -= water_m3
        self.audit.log("METABOLISM", f"Fed {len(alive)} citizens")


# =====================================================================
# CONTOUR 4: HEALTH
# =====================================================================
class HealthCore:
    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.infected: Set[str] = set()

    def mark_infected(self, citizen: Citizen):
        citizen.is_infected = True
        citizen.quarantine_until = time.time() + Constitution.INFECTION_QUARANTINE_HOURS * 3600
        self.infected.add(citizen.id)
        self.audit.log("HEALTH", f"{citizen.id} quarantined")

    def check_capsule_risk(self, capsule, registry):
        if capsule.current_user is None:
            return
        user = registry.get(capsule.current_user)
        if user and user.is_infected:
            capsule.quarantined_until = time.time() + Constitution.INFECTION_QUARANTINE_HOURS * 3600
            self.audit.log("HEALTH", f"{capsule.id} quarantined")

    def mental_check(self, citizen: Citizen):
        now = time.time()
        if now - citizen.last_mental_check < Constitution.MENTAL_HEALTH_CHECK_INTERVAL_HOURS * 3600:
            return
        citizen.last_mental_check = now
        citizen.mental_health_score = min(
            1.0,
            citizen.mental_health_score
            + 0.05 * citizen.play_hours_today
            + 0.02 * citizen.care_received_hours,
        )
        if citizen.mental_health_score < 0.4:
            self.audit.log("HEALTH", f"{citizen.id}: low score")

    def tick(self, registry):
        now = time.time()
        for c in registry.citizens.values():
            if c.is_infected and now >= c.quarantine_until:
                c.is_infected = False
                self.infected.discard(c.id)
                self.audit.log("HEALTH", f"{c.id} discharged")


# =====================================================================
# CONTOUR 5: HOUSING + COMMONS + THIRD PLACES
# =====================================================================
class SpaceType(Enum):
    CAPSULE = "capsule"
    COMMONS = "commons"
    THIRD_PLACE = "third_place"
    QUIET = "quiet"
    STIM = "stim"
    PLAY = "play"
    REPAIR = "repair"


class Space:
    def __init__(self, sid: str, gps, area_m2: float, kind: SpaceType = SpaceType.CAPSULE):
        self.id = sid
        self.gps = gps
        self.area_m2 = area_m2
        self.kind = kind
        self.is_occupied = False
        self.current_user: Optional[str] = None
        self.sterile_until = 0.0
        self.occupied_since = 0.0
        self.quarantined_until = 0.0
        self.free_use = kind in (
            SpaceType.COMMONS, SpaceType.THIRD_PLACE,
            SpaceType.QUIET, SpaceType.STIM, SpaceType.PLAY,
        )

    def is_available(self, now: float) -> bool:
        if self.kind in (SpaceType.COMMONS, SpaceType.THIRD_PLACE):
            return True
        return (
            not self.is_occupied
            and now >= self.sterile_until
            and now >= self.quarantined_until
        )

    def occupancy_minutes(self, now: float) -> float:
        return 0.0 if not self.is_occupied else (now - self.occupied_since) / 60.0


class DynamicSpaceManager:
    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.spaces: List[Space] = []

    def add(self, space: Space):
        self.spaces.append(space)

    @staticmethod
    def _dist2(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    def request_capsule(self, citizen: Citizen, gps) -> Optional[Space]:
        if not citizen.is_alive:
            return None
        now = time.time()
        max_area = citizen.max_comfort_area()
        available = [
            s for s in self.spaces
            if s.kind == SpaceType.CAPSULE
            and s.is_available(now)
            and s.area_m2 <= max_area
        ]
        if not available:
            self.audit.log("SPACE", f"No capsules for {citizen.id}")
            return None
        priority = citizen.capsule_priority()
        chosen = min(available, key=lambda s: self._dist2(s.gps, gps) / priority)
        chosen.is_occupied = True
        chosen.current_user = citizen.id
        chosen.occupied_since = now
        chosen.sterile_until = 0.0
        self.audit.log(
            "SPACE",
            f"{chosen.id} ({chosen.area_m2} m^2) -> {citizen.id}",
            f"need={max_area:.0f} m^2",
        )
        return chosen

    def release(self, space_id: str):
        for s in self.spaces:
            if s.id == space_id:
                s.is_occupied = False
                s.current_user = None
                s.occupied_since = 0.0
                s.sterile_until = time.time() + Constitution.CLEANING_TIME_SECONDS
                self.audit.log("AUTOMATION", f"Sterilized {space_id}")
                return

    def commons_nearby(self, gps, radius: float = 0.002) -> List[Space]:
        return [
            s for s in self.spaces
            if s.kind in (SpaceType.COMMONS, SpaceType.THIRD_PLACE)
            and self._dist2(s.gps, gps) < radius ** 2
        ]


# =====================================================================
# CONTOUR 18: COMMUNITY CLUSTERING (with serendipity)
# =====================================================================
class DynamicCommunityClustering:
    NEAR_RADIUS_DEG = 0.001
    MIN_COMMON_INTERESTS = 2

    def __init__(self, civilization: 'Civilization'):
        self.civ = civilization
        self.last_reset = time.time()

    def find_and_book_social_capsule(self, citizen: Citizen, target_gps):
        now = time.time()
        if (now - self.last_reset) > Constitution.CLUSTER_RESET_DAYS * 86400:
            self.last_reset = now
            self.civ.audit.log("SERENDIPITY", "Cluster reset: random neighbors")

        max_area = citizen.max_comfort_area()
        available = [
            s for s in self.civ.space.spaces
            if s.kind == SpaceType.CAPSULE
            and s.is_available(now)
            and s.area_m2 <= max_area
        ]
        if not available:
            return None

        # 20% of the time — intentionally mix non-matching interests
        if random.random() < 0.2:
            chosen = random.choice(available)
            chosen.is_occupied = True
            chosen.current_user = citizen.id
            chosen.occupied_since = now
            self.civ.audit.log(
                "SERENDIPITY",
                f"Random neighbor: {chosen.id} -> {citizen.id}",
            )
            return chosen

        best, best_score = None, -1.0
        for capsule in available:
            social = 0.0
            for other in self.civ.space.spaces:
                if not (other.is_occupied and other.current_user and other.kind == SpaceType.CAPSULE):
                    continue
                d = self.civ.space._dist2(capsule.gps, other.gps)
                if d > self.NEAR_RADIUS_DEG ** 2:
                    continue
                neighbor = self.civ.registry.get(other.current_user)
                if not neighbor:
                    continue
                common = citizen.interests & neighbor.interests
                if len(common) >= self.MIN_COMMON_INTERESTS:
                    social += len(common) / (math.sqrt(d) + 0.01)
            geo = self.civ.space._dist2(capsule.gps, target_gps)
            score = social / (geo + 0.01)
            if score > best_score:
                best_score, best = score, capsule

        if best is None:
            return self.civ.space.request_capsule(citizen, target_gps)

        best.is_occupied = True
        best.current_user = citizen.id
        best.occupied_since = now
        self.civ.audit.log("CLUSTER_SPACE", f"{best.id} -> {citizen.id}", f"score={best_score:.2f}")
        return best


# =====================================================================
# CONTOUR 6: LOGISTICS
# =====================================================================
class FlowRouter:
    def __init__(self, space: DynamicSpaceManager, core: ResourceCore, audit: AuditLedger):
        self.space = space
        self.core = core
        self.audit = audit

    def relocate_space(self, space_id, new_gps, energy_kwh) -> bool:
        if self.core.energy_reserve_kwh < energy_kwh:
            self.audit.log("FLOW", f"{space_id}: cancelled", "low energy")
            return False
        for s in self.space.spaces:
            if s.id == space_id:
                s.gps = new_gps
                self.core.energy_reserve_kwh -= energy_kwh
                self.audit.log("FLOW", f"{space_id} -> {new_gps}")
                return True
        return False

    def route_person(self, citizen: Citizen, target_gps, distance_km) -> bool:
        cost = distance_km * 0.5
        if self.core.energy_reserve_kwh < cost:
            return False
        self.core.energy_reserve_kwh -= cost
        citizen.home_gps = target_gps
        self.audit.log("FLOW", f"{citizen.id}: {distance_km:.1f} km")
        return True


# =====================================================================
# CONTOUR 7: ENERGY
# =====================================================================
class EnergyGrid:
    def __init__(self, core: ResourceCore, audit: AuditLedger):
        self.core = core
        self.audit = audit
        self.sources: Dict[str, float] = {}

    def add_source(self, name: str, capacity_kwh: float):
        self.sources[name] = self.sources.get(name, 0.0) + capacity_kwh
        self.audit.log("ENERGY", f"+{capacity_kwh} ({name})")

    def produce(self, dt_hours: float = 1.0):
        total = sum(self.sources.values()) * dt_hours
        self.core.energy_reserve_kwh = min(
            Constitution.ENERGY_RESERVE_MAX_KWH,
            self.core.energy_reserve_kwh + total,
        )


# =====================================================================
# CONTOUR 8: MATTER
# =====================================================================
class MatterRecycler:
    def __init__(self, core: ResourceCore, audit: AuditLedger):
        self.core = core
        self.audit = audit

    def recycle(self, material: str, amount: float):
        cap = Constitution.MATERIALS_MAX.get(material, float("inf"))
        self.core.raw_materials[material] = min(
            cap, self.core.raw_materials.get(material, 0.0) + amount
        )
        self.audit.log("MATTER", f"+{amount} {material}")


# =====================================================================
# CONTOUR 9: REPUTATION (forgetting curve, not blockchain)
# =====================================================================
class ARReputationSystem:
    """
    Blockchain replaced by forgetting curve.
    Reputation is memory with decay, not a permanent scar.
    Right to rehabilitation and oblivion guaranteed by constitution.
    """

    def __init__(self, registry: CitizenRegistry, audit: AuditLedger):
        self.registry = registry
        self.audit = audit

    def register(self, user_id: str, points: float, description: str, anonymous: bool = False):
        c = self.registry.get(user_id)
        if c is None or not c.is_alive:
            self.audit.log("REPUTATION", f"Rejected: {user_id}")
            return
        if anonymous and Constitution.ANONYMOUS_CONTRIBUTIONS_ALLOWED:
            c.anonymous_contributions += 1
            self.audit.log("REPUTATION", "Anonymous contribution registered")
        c.add_reputation_event(points, description)
        self.audit.log("REPUTATION", f"{user_id}: +{points}")

    def rehabilitation(self, user_id: str):
        """After a long constructive period, negative history is cleared."""
        c = self.registry.get(user_id)
        if not c:
            return
        now = time.time()
        cutoff = now - Constitution.REPUTATION_REHABILITATION_YEARS * 365 * 86400
        c.reputation_events = [
            (ts, v, d) for ts, v, d in c.reputation_events
            if ts > cutoff or v > 0
        ]
        self.audit.log("REPUTATION", f"{user_id}: rehabilitation applied")

    def end_lifecycle(self, user_id: str):
        c = self.registry.get(user_id)
        if c:
            c.is_alive = False
            c.reputation_events.clear()
        self.audit.log("LAW", f"Cycle of {user_id} ended", "reputation erased")


# =====================================================================
# CONTOUR 10: EDUCATION (+ Neurodiversity)
# =====================================================================
class EducationCore:
    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.courses: Dict[str, Dict] = {}

    def add_course(self, cid: str, topic: str, style: str = "multimodal"):
        self.courses[cid] = {"topic": topic, "style": style}
        self.audit.log("EDUCATION", f"Course '{topic}' ({style})")

    def weekly_learning(self, citizen: Citizen, hours: float):
        if citizen.life_stage == LifeStage.DECEASED:
            return
        if hours > Constitution.EDUCATION_HOURS_PER_WEEK:
            hours = Constitution.EDUCATION_HOURS_PER_WEEK
        key = f"study_{len(citizen.skills)}"
        citizen.skills[key] = citizen.skills.get(key, 0.0) + hours
        self.audit.log(
            "EDUCATION",
            f"{citizen.id}: +{hours} h ({citizen.learning_style})",
        )


# =====================================================================
# CONTOUR 11: MEANING (with expert voting)
# =====================================================================
class MegaProject:
    def __init__(self, project_id, title, utility_metrics,
                 cost_co2, water_required, energy_required, materials_required,
                 question_type: str = "basic"):
        self.id = project_id
        self.title = title
        self.utility_metrics = utility_metrics
        self.cost_co2 = cost_co2
        self.water_required = water_required
        self.energy_required = energy_required
        self.materials_required = materials_required
        self.question_type = question_type
        self.votes_pro = 0.0
        self.votes_contra = 0.0
        self.executed = False


class MeaningOrchestrator:
    def __init__(self, core, registry, audit, ai: AIKernel):
        self.core = core
        self.registry = registry
        self.audit = audit
        self.ai = ai
        self.projects: Dict[str, MegaProject] = {}

    def submit(self, project: MegaProject):
        self.projects[project.id] = project
        self.audit.log("MEANING", f"Project {project.id} ({project.question_type})")

    def vote(self, voter_id: str, project_id: str, pro: bool, tags: List[str]):
        c = self.registry.get(voter_id)
        if c is None or not c.is_alive:
            return
        p = self.projects.get(project_id)
        if p is None:
            return
        w = c.vote_weight(p.question_type)
        if "coordinated_lobby" in tags:
            w *= 0.05
            self.audit.log("SECURITY", f"{voter_id}: weight reduced")
        if pro:
            p.votes_pro += w
        else:
            p.votes_contra += w

    def tally(self, project_id: str) -> Tuple[int, int]:
        p = self.projects[project_id]
        return int(round(p.votes_pro)), int(round(p.votes_contra))

    def execute(self, project_id: str) -> bool:
        p = self.projects.get(project_id)
        if p is None or p.executed:
            return False
        pro, contra = self.tally(project_id)
        if pro <= contra:
            self.audit.log("MEANING", f"{p.id}: {pro} <= {contra}")
            return False
        if not self.core.verify(p.cost_co2, p.water_required, p.energy_required, p.materials_required):
            self.audit.log("VETO", f"'{p.title}'")
            return False
        self.core.allocate(p.cost_co2, p.water_required, p.energy_required, p.materials_required)
        p.executed = True
        self.ai.execute(f"Executed '{p.title}'", f"pro={pro} contra={contra}",
                        agents_required=["logistician", "auditor"])
        return True


# =====================================================================
# CONTOUR 12: CARE
# =====================================================================
class CareCore:
    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.care_workers: List[str] = []

    def assign_care_worker(self, citizen: Citizen):
        self.care_workers.append(citizen.id)
        self.audit.log("CARE", f"{citizen.id} is a care worker")

    def care_for(self, giver: Citizen, receiver: Citizen, hours: float):
        if not giver.is_alive or not receiver.is_alive:
            return
        giver.care_given_hours += hours
        receiver.care_received_hours += hours
        giver.add_reputation_event(hours * 0.1, f"care_{receiver.id}")
        self.audit.log("CARE", f"{giver.id} -> {receiver.id}: {hours} h")


# =====================================================================
# CONTOUR 13: CONFLICT RESOLUTION (extended sublimation)
# =====================================================================
class ConflictResolver:
    """Mediation, deliberation, protest. No punishment."""

    def __init__(self, audit: AuditLedger, ai: AIKernel):
        self.audit = audit
        self.ai = ai
        self.cases: List[Dict] = []
        self.deliberations: List[Dict] = []

    def file_case(self, complainant: str, accused: str, description: str):
        self.cases.append({
            "complainant": complainant,
            "accused": accused,
            "description": description,
            "resolved": False,
        })
        self.audit.log("CONFLICT", f"{complainant} -> {accused}")

    def mediate(self, case_index: int, outcome: str):
        self.cases[case_index]["resolved"] = True
        self.cases[case_index]["outcome"] = outcome
        self.audit.log("CONFLICT", f"Mediation: {outcome}")

    def open_deliberation(self, topic: str, participants: List[str]):
        self.deliberations.append({
            "topic": topic,
            "participants": participants,
            "started": time.time(),
        })
        self.audit.log("DELIBERATION", f"Topic opened: {topic}")

    def civil_disobedience(self, citizen: Citizen, cause: str):
        self.audit.log("PROTEST", f"{citizen.id}: disagreement on '{cause}'")
        citizen.add_reputation_event(0.5, f"civil_disobedience_{cause}")

    def art_protest(self, citizen: Citizen, description: str):
        self.audit.log("ART_PROTEST", f"{citizen.id}: {description}")
        citizen.add_reputation_event(1.0, "art_protest")


# =====================================================================
# CONTOUR 16: TIME (including Serendipity and Play)
# =====================================================================
class TimeCommons:
    def __init__(self, audit: AuditLedger):
        self.audit = audit

    def log_work(self, citizen: Citizen, hours: float):
        allowed = max(0.0, Constitution.MAX_WORK_HOURS_PER_WEEK - citizen.work_hours_this_week)
        hours = min(hours, allowed)
        citizen.work_hours_this_week += hours
        self.audit.log("TIME", f"{citizen.id}: +{hours} h work")

    def log_play(self, citizen: Citizen, hours: float):
        citizen.play_hours_today += hours
        self.audit.log("TIME", f"{citizen.id}: +{hours} h play")

    def log_serendipity(self, citizen: Citizen, hours: float):
        allowed = max(0.0, Constitution.SERENDIPITY_HOURS_PER_WEEK - citizen.serendipity_hours_this_week)
        hours = min(hours, allowed)
        citizen.serendipity_hours_this_week += hours
        self.audit.log("SERENDIPITY", f"{citizen.id}: +{hours} h blank time")

    def reset_week(self, citizen: Citizen):
        citizen.work_hours_this_week = 0.0
        citizen.serendipity_hours_this_week = 0.0

    def reset_day(self, citizen: Citizen):
        citizen.play_hours_today = 0.0


# =====================================================================
# CONTOUR 17: GENERATIONS
# =====================================================================
class GenerationCycle:
    def __init__(self, registry, reputation, care, audit):
        self.registry = registry
        self.reputation = reputation
        self.care = care
        self.audit = audit

    def birth(self, child_id, gps, parents):
        child = Citizen(child_id, gps, age=0.0)
        self.registry.register(child)
        self.audit.log("GENERATION", f"Birth of {child_id}", f"parents: {parents}")

    def death(self, citizen: Citizen, reason: str):
        self.reputation.end_lifecycle(citizen.id)
        self.audit.log("GENERATION", f"Death of {citizen.id}", reason)


# =====================================================================
# CONTOUR 19: ARTIFACT COMMONS
# =====================================================================
class Artifact:
    def __init__(self, aid: str, name: str):
        self.id = aid
        self.name = name
        self.history: List[Tuple[float, str, str]] = []
        self.repair_count: int = 0

    def touch(self, user_id: str, action: str):
        self.history.append((time.time(), user_id, action))


class ArtifactCommons:
    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.artifacts: Dict[str, Artifact] = {}

    def add(self, artifact: Artifact):
        self.artifacts[artifact.id] = artifact
        self.audit.log("ARTIFACT", f"Added: {artifact.name}")

    def borrow(self, artifact_id: str, user_id: str):
        if artifact_id in self.artifacts:
            self.artifacts[artifact_id].touch(user_id, "borrowed")
            self.audit.log("ARTIFACT", f"{user_id} borrowed {artifact_id}")

    def repair(self, artifact_id: str, user_id: str, hours: float):
        if artifact_id in self.artifacts:
            a = self.artifacts[artifact_id]
            a.repair_count += 1
            a.touch(user_id, f"repaired ({hours}h)")
            self.audit.log("REPAIR", f"{user_id} repaired {artifact_id} ({hours}h)")


# =====================================================================
# CONTOUR 20: RITUAL CORE
# =====================================================================
class RitualCore:
    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.rituals: Dict[str, Dict] = {}

    def declare_ritual(self, name: str, frequency_days: float, description: str):
        self.rituals[name] = {
            "frequency_days": frequency_days,
            "description": description,
            "last_performed": 0.0,
        }
        self.audit.log("RITUAL", f"Ritual '{name}' ({frequency_days} days)")

    def perform(self, name: str, participants: List[str]):
        r = self.rituals.get(name)
        if not r:
            return
        r["last_performed"] = time.time()
        self.audit.log("RITUAL", f"'{name}' with {len(participants)} participants")


# =====================================================================
# CONTOUR 21: CHILDHOOD SPACE
# =====================================================================
class ChildhoodSpace:
    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.spaces: List[Space] = []

    def add(self, space: Space):
        self.spaces.append(space)

    def register_child(self, child: Citizen):
        self.audit.log("CHILDHOOD", f"{child.id} in children's space")


# =====================================================================
# CONTOUR 22: GRIEF CORE
# =====================================================================
class GriefCore:
    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.house_of_names: Dict[str, List[str]] = {}

    def register_passing(self, deceased: Citizen, stories: List[str]):
        self.house_of_names[deceased.id] = stories
        self.audit.log("GRIEF", f"{deceased.id}: {len(stories)} stories preserved")

    def support_mourner(self, mourner: Citizen, deceased_id: str, hours: float):
        mourner.mourning_for.add(deceased_id)
        mourner.care_received_hours += hours
        self.audit.log("GRIEF", f"{mourner.id}: support for loss of {deceased_id} ({hours} h)")


# =====================================================================
# CONTOUR 23: PRIVACY (DataDignity)
# =====================================================================
class DataPod:
    """Personal storage under citizen control."""

    def __init__(self, owner_id: str):
        self.owner_id = owner_id
        self.private: Dict[str, any] = {}
        self.shared_zk: Set[str] = set()

    def store(self, key: str, value: any):
        self.private[key] = value

    def prove_without_revealing(self, fact: str) -> bool:
        """Zero-knowledge: prove a fact without revealing data."""
        self.shared_zk.add(fact)
        return True


class PrivacyCore:
    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.data_pods: Dict[str, DataPod] = {}

    def create_pod(self, citizen: Citizen) -> DataPod:
        pod = DataPod(citizen.id)
        self.data_pods[citizen.id] = pod
        self.audit.log("PRIVACY", f"Data pod created for {citizen.id}")
        return pod

    def oblivion_request(self, citizen: Citizen, category: str):
        citizen.request_oblivion(category)
        self.audit.log("PRIVACY", f"{citizen.id}: oblivion '{category}'")

    def anonymous_contribution(self, reputation_system: ARReputationSystem,
                                citizen: Citizen, points: float, description: str):
        if not Constitution.ANONYMOUS_CONTRIBUTIONS_ALLOWED:
            return
        reputation_system.register(citizen.id, points, f"[anon] {description}", anonymous=True)


# =====================================================================
# CONTOUR 24: BIODIVERSITY
# =====================================================================
class Ecosystem:
    def __init__(self, name: str):
        self.name = name
        self.soil_health = 1.0
        self.pollinator_index = 1.0
        self.forest_cover = 1.0
        self.marine_health = 1.0
        self.species_count = 1000


class BiodiversityCore:
    """Nature is a subject, not a resource. Rights of nature in constitution."""

    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.ecosystems: Dict[str, Ecosystem] = {}
        self.nature_vetoes: List[str] = []

    def register_ecosystem(self, eco: Ecosystem):
        self.ecosystems[eco.name] = eco

    def nature_health_check(self) -> Dict[str, bool]:
        result = {}
        for name, eco in self.ecosystems.items():
            ok = (
                eco.soil_health >= Constitution.SOIL_HEALTH_MIN
                and eco.pollinator_index >= Constitution.POLLINATOR_INDEX_MIN
                and eco.forest_cover >= Constitution.FOREST_COVER_MIN
                and eco.marine_health >= Constitution.MARINE_HEALTH_MIN
            )
            result[name] = ok
            if not ok:
                self.nature_vetoes.append(f"{name}: declining health")
                self.audit.log("NATURE_VETO", f"Ecosystem '{name}' at risk")
        return result

    def protect_corridor(self, gps_start, gps_end):
        if not Constitution.SPECIES_CORRIDORS_REQUIRED:
            return
        self.audit.log("BIODIVERSITY", f"Species corridor {gps_start} -> {gps_end}")


# =====================================================================
# CONTOUR 25: NEURODIVERSITY
# =====================================================================
class NeurodiversityCore:
    def __init__(self, audit: AuditLedger):
        self.audit = audit

    def assign_learning_style(self, citizen: Citizen, style: str):
        if style in Constitution.LEARNING_STYLES:
            citizen.learning_style = style
            self.audit.log("NEURODIVERSITY", f"{citizen.id}: style {style}")

    def register_quiet_space(self, space: Space, space_manager: DynamicSpaceManager):
        space.kind = SpaceType.QUIET
        space_manager.add(space)
        self.audit.log("NEURODIVERSITY", f"Quiet space {space.id}")

    def register_stim_space(self, space: Space, space_manager: DynamicSpaceManager):
        space.kind = SpaceType.STIM
        space_manager.add(space)
        self.audit.log("NEURODIVERSITY", f"Stim space {space.id}")


# =====================================================================
# CONTOUR 26: SERENDIPITY
# =====================================================================
class SerendipityCore:
    """Chaos buffer: blank time, random neighbors, lucky accidents."""

    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.failure_archive: List[Tuple[float, str, str]] = []

    def protected_blank_time(self, citizen: Citizen, hours: float):
        self.audit.log("SERENDIPITY", f"{citizen.id}: {hours} h without KPI")

    def lucky_accident(self, citizen: Citizen, description: str):
        self.failure_archive.append((time.time(), citizen.id, description))
        citizen.add_reputation_event(2.0, f"lucky_accident: {description}")
        self.audit.log("SERENDIPITY", f"{citizen.id}: lucky accident — {description}")

    def archive_failure(self, citizen: Citizen, description: str):
        self.failure_archive.append((time.time(), citizen.id, description))
        self.audit.log("FAILURE_ARCHIVE", f"{citizen.id}: {description}")

    def get_failures(self, n: int = 10) -> List[Tuple[float, str, str]]:
        return self.failure_archive[-n:]


# =====================================================================
# CONTOUR 27: REPAIR
# =====================================================================
class RepairCore:
    """Repair as a philosophy of relations with things."""

    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.repairs: List[Tuple[float, str, str, float]] = []

    def repair(self, repairer: Citizen, artifact_id: str, hours: float):
        if Constitution.PLANNED_OBSOLESCENCE_FORBIDDEN:
            self.repairs.append((time.time(), repairer.id, artifact_id, hours))
            repairer.add_reputation_event(hours * 0.5, f"repair_{artifact_id}")
            self.audit.log("REPAIR", f"{repairer.id}: {artifact_id} ({hours} h)")

    def register_repair_workshop(self, space: Space, space_manager: DynamicSpaceManager):
        space.kind = SpaceType.REPAIR
        space_manager.add(space)
        self.audit.log("REPAIR", f"Workshop {space.id}")


# =====================================================================
# CONTOUR 28: LOCAL AUTONOMY
# =====================================================================
class Bioregion:
    def __init__(self, name: str):
        self.name = name
        self.local_overrides: Dict[str, any] = {}
        self.languages: Set[str] = set()
        self.local_rituals: List[str] = []


class LocalAutonomyCore:
    """Federation of bioregions: local variations within IMMUTABLE_CORE."""

    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.bioregions: Dict[str, Bioregion] = {}

    def register_bioregion(self, br: Bioregion):
        self.bioregions[br.name] = br
        self.audit.log("BIOREGION", f"Registered {br.name}")

    def set_local_rule(self, region_name: str, key: str, value) -> bool:
        if key in Constitution.IMMUTABLE_CORE:
            self.audit.log("BIOREGION", f"Rejected: {key} immutable", region_name)
            return False
        if region_name in self.bioregions:
            self.bioregions[region_name].local_overrides[key] = value
            self.audit.log("BIOREGION", f"{region_name}: {key}={value}")
            return True
        return False

    def preserve_language(self, region_name: str, language: str):
        if region_name in self.bioregions:
            self.bioregions[region_name].languages.add(language)
            self.audit.log("LANGUAGE", f"{region_name}: preserved {language}")


# =====================================================================
# CONTOUR 29: DEATH RITUAL
# =====================================================================
class DeathRitualCore:
    """Death is an event for the living, not an administrative operation."""

    def __init__(self, audit: AuditLedger, grief: GriefCore):
        self.audit = audit
        self.grief = grief
        self.ceremonies: List[Dict] = []

    def ceremony(self, deceased: Citizen, stories: List[str], participants: List[str]):
        self.grief.register_passing(deceased, stories)
        self.ceremonies.append({
            "deceased": deceased.id,
            "participants": participants,
            "stories": stories,
            "timestamp": time.time(),
        })
        self.audit.log(
            "DEATH_RITUAL",
            f"Memory ceremony for {deceased.id}",
            f"{len(participants)} participants, {len(stories)} stories",
        )


# =====================================================================
# CONTOUR 30: LANGUAGE COMMONS
# =====================================================================
class LanguageCommons:
    """Language is living infrastructure of thought, not 'cultural heritage'."""

    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.languages: Dict[str, Dict] = {}
        self.translation_available: Set[Tuple[str, str]] = set()

    def register_language(self, code: str, speakers: int):
        self.languages[code] = {"speakers": speakers, "alive": True}
        self.audit.log("LANGUAGE", f"Registered {code} ({speakers} speakers)")

    def protect_language(self, code: str, funding_share: float):
        if code in self.languages:
            self.audit.log("LANGUAGE", f"{code}: protected, {funding_share:.1%} resources")

    def enable_translation(self, a: str, b: str):
        self.translation_available.add((a, b))
        self.audit.log("LANGUAGE", f"Translation {a}<->{b} as a universal good")


# =====================================================================
# CONTOUR 31: FAILURE COMMONS
# =====================================================================
class FailureCommons:
    """Right to error. Public failure archive."""

    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.archived_failures: List[Dict] = []

    def archive(self, citizen: Citizen, description: str, lessons: str):
        if not Constitution.FAILURE_ARCHIVE_PUBLIC:
            return
        self.archived_failures.append({
            "who": citizen.id,
            "what": description,
            "lessons": lessons,
            "timestamp": time.time(),
        })
        self.audit.log("FAILURE", f"{citizen.id}: '{description}'")

    def search(self, keyword: str) -> List[Dict]:
        return [f for f in self.archived_failures if keyword.lower() in f["what"].lower()]


# =====================================================================
# CONTOUR 32: PLAY
# =====================================================================
class PlayCore:
    """Play is self-valued activity, not 'rest from work'."""

    def __init__(self, audit: AuditLedger):
        self.audit = audit
        self.play_spaces: List[Space] = []
        self.play_types: Set[str] = {
            "physical", "intellectual", "social",
            "creative", "exploratory", "narrative",
        }

    def register_play_space(self, space: Space, space_manager: DynamicSpaceManager):
        space.kind = SpaceType.PLAY
        space_manager.add(space)
        self.play_spaces.append(space)
        self.audit.log("PLAY", f"Play space {space.id}")

    def play_session(self, citizen: Citizen, play_type: str, hours: float):
        if play_type not in self.play_types:
            return
        citizen.play_hours_today += hours
        self.audit.log("PLAY", f"{citizen.id}: {play_type} ({hours} h)")


# =====================================================================
# CIVILIZATION — ASSEMBLY OF ALL CONTOURS
# =====================================================================
class Civilization:
    """
    Full model. AI kernel (AIKernel) executes human will,
    bounded by constitution and planetary physics.
    """

    def __init__(self):
        self.audit = AuditLedger()
        self.ai = AIKernel(self.audit)
        self.core = ResourceCore(self.audit)
        self.registry = CitizenRegistry()
        self.metabolism = MetabolismCore(self.core, self.audit)
        self.health = HealthCore(self.audit)
        self.space = DynamicSpaceManager(self.audit)
        self.flow = FlowRouter(self.space, self.core, self.audit)
        self.energy = EnergyGrid(self.core, self.audit)
        self.matter = MatterRecycler(self.core, self.audit)
        self.reputation = ARReputationSystem(self.registry, self.audit)
        self.education = EducationCore(self.audit)
        self.meaning = MeaningOrchestrator(self.core, self.registry, self.audit, self.ai)
        self.care = CareCore(self.audit)
        self.conflicts = ConflictResolver(self.audit, self.ai)
        self.time = TimeCommons(self.audit)
        self.generation = GenerationCycle(self.registry, self.reputation, self.care, self.audit)
        self.clustering = DynamicCommunityClustering(self)
        self.artifacts = ArtifactCommons(self.audit)
        self.rituals = RitualCore(self.audit)
        self.childhood = ChildhoodSpace(self.audit)
        self.grief = GriefCore(self.audit)
        self.privacy = PrivacyCore(self.audit)
        self.biodiversity = BiodiversityCore(self.audit)
        self.neurodiversity = NeurodiversityCore(self.audit)
        self.serendipity = SerendipityCore(self.audit)
        self.repair = RepairCore(self.audit)
        self.local_autonomy = LocalAutonomyCore(self.audit)
        self.death_ritual = DeathRitualCore(self.audit, self.grief)
        self.language = LanguageCommons(self.audit)
        self.failure = FailureCommons(self.audit)
        self.play = PlayCore(self.audit)

    def tick(self, dt_hours: float = 1.0):
        """One step of civilization's time."""
        self.core.regenerate(dt_hours)
        self.energy.produce(dt_hours)
        self.metabolism.feed(self.registry.all_alive(), dt_days=dt_hours / 24.0)
        self.health.tick(self.registry)
        for c in self.registry.all_alive():
            self.health.mental_check(c)
        if self.biodiversity.ecosystems:
            self.biodiversity.nature_health_check()


# =====================================================================
# DEMONSTRATION
# =====================================================================
if __name__ == "__main__":
    print("=" * 68)
    print(" FLUID CIVILIZATION v4 — demonstration")
    print("=" * 68)

    civ = Civilization()

    igor = Citizen("Igor", (59.931, 30.332), age=34)
    anna = Citizen("Anna", (59.940, 30.320), age=31)
    child = Citizen("Mira", (59.940, 30.320), age=7)
    elder = Citizen("Nikolai", (59.935, 30.325), age=78)
    olga = Citizen("Olga", (59.934, 30.328), age=45)
    lobby = Citizen("LobbyBot", (0.0, 0.0), age=25)

    for c in (igor, anna, child, elder, olga, lobby):
        civ.registry.register(c)

    civ.care.assign_care_worker(olga)

    print("\n[1] Data pods and right to oblivion")
    civ.privacy.create_pod(igor)
    civ.reputation.register("Igor", 50.0, "Relay Transmission Theory model")
    igor.add_reputation_event(-5.0, "old_mistake")
    print(f"  -> Igor's reputation (with decay): {igor.reputation_score():.2f}")
    civ.privacy.oblivion_request(igor, "old_mistake")
    print(f"  -> After oblivion: {igor.reputation_score():.2f}")

    print("\n[2] Voting: basic is one person = one vote")
    print(f"  -> Igor's weight (basic): {igor.vote_weight('basic')}")
    print(f"  -> Mira's weight (basic): {child.vote_weight('basic')}")

    igor.expertise.add("climatology")
    print(f"  -> Igor's weight (expert): {igor.vote_weight('expert'):.2f}")
    print(f"  -> Mira's weight (expert): {child.vote_weight('expert'):.2f}")

    print("\n[3] Housing: base area for everyone")
    civ.space.add(Space("C1", (59.93, 30.33), 14.0))
    civ.space.add(Space("C2", (59.94, 30.32), 22.0))
    civ.space.add(Space("C3", (59.935, 30.325), 60.0))
    print(f"  -> Mira's max area: {child.max_comfort_area()} m^2 (child)")
    print(f"  -> Igor's max area: {igor.max_comfort_area()} m^2 (score={igor.reputation_score():.1f})")

    print("\n[4] Commons spaces")
    civ.space.add(Space("COMMONS-1", (59.93, 30.33), 200.0, kind=SpaceType.COMMONS))
    civ.space.add(Space("THIRD-1", (59.93, 30.33), 80.0, kind=SpaceType.THIRD_PLACE))
    commons = civ.space.commons_nearby((59.93, 30.33))
    print(f"  -> Commons nearby: {len(commons)}")

    print("\n[5] Neurodiversity")
    civ.neurodiversity.assign_learning_style(child, "kinesthetic")
    civ.neurodiversity.register_quiet_space(Space("QUIET-1", (59.93, 30.33), 30.0), civ.space)
    civ.neurodiversity.register_stim_space(Space("STIM-1", (59.93, 30.33), 25.0), civ.space)

    print("\n[6] Sublimation: deliberation, protest, art")
    civ.conflicts.open_deliberation("Climate change in bioregion", ["Igor", "Anna"])
    civ.conflicts.civil_disobedience(igor, "construction on wetland")
    civ.conflicts.art_protest(anna, "mural on river rights")

    print("\n[7] Rights of nature")
    civ.biodiversity.register_ecosystem(Ecosystem("Taiga-North"))
    civ.biodiversity.protect_corridor((59.9, 30.3), (60.1, 30.5))

    print("\n[8] Federation of bioregions")
    civ.local_autonomy.register_bioregion(Bioregion("Baltic"))
    civ.local_autonomy.set_local_rule("Baltic", "MAX_WORK_HOURS_PER_WEEK", 18.0)
    civ.local_autonomy.set_local_rule("Baltic", "AI_CANNOT_USE_FORCE", False)
    civ.local_autonomy.preserve_language("Baltic", "Veps")

    print("\n[9] LanguageCommons")
    civ.language.register_language("Veps", 5000)
    civ.language.protect_language("Veps", 0.02)
    civ.language.enable_translation("Veps", "common")

    print("\n[10] PlayCore")
    civ.play.register_play_space(Space("PLAY-1", (59.93, 30.33), 50.0), civ.space)
    civ.play.play_session(child, "creative", 2.5)

    print("\n[11] FailureCommons: failure as data")
    civ.failure.archive(igor, "Cold fusion experiment",
                        "temperature not held, but new catalyst found")
    civ.serendipity.lucky_accident(igor, "side effect of catalyst")

    print("\n[12] RepairCore")
    civ.repair.repair(olga, "artifact_001", hours=3.0)
    civ.repair.register_repair_workshop(Space("REPAIR-1", (59.93, 30.33), 40.0), civ.space)

    print("\n[13] Death as shared practice")
    civ.death_ritual.ceremony(
        elder,
        stories=["loved the sea", "taught grandchildren to fish", "grew a garden"],
        participants=["Igor", "Anna", "Mira", "Olga"],
    )
    civ.grief.support_mourner(child, elder.id, hours=5.0)

    print("\n[14] One hour of civilization")
    civ.tick(dt_hours=1.0)

    print("\n" + "=" * 68)
    print(" AUDIT (last 15 entries)")
    print("=" * 68)
    for line in civ.audit.dump(last_n=15):
        print(" ", line)

    print("\n=== v4: civilization with privacy, error, and rights of nature ===")