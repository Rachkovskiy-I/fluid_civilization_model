```markdown
# Contributing to Fluid Civilization Model

Thank you for considering a contribution. This is a research model, not a political program. We welcome **critique as much as code**.

## What we need

### 1. Critical analysis
Where does the model break? Which assumptions are unrealistic? Which contours contradict each other? Open an issue.

### 2. Simulation extensions
- Stochastic events (drought, pandemic, solar flare)
- Scaling tests (10k, 1M citizens)
- Adversarial scenarios (AI drift, capture, manipulation)
- Visualization of resource flows over time

### 3. Alternative implementations
- Ports to other languages (Rust, Julia, TypeScript)
- Different assumptions (smaller scale, different ecology, different AI design)

### 4. Philosophical critique
- Is this model desirable?
- Is it coherent?
- What does it miss?

## How to contribute

1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-idea`.
3. Make changes with clear commit messages.
4. Add tests if applicable.
5. Open a pull request describing **what** and **why**.

## Code style

- Python 3.9+
- Type hints where helpful
- Docstrings for public classes and methods
- No external dependencies (keep it single-file portable)
- Comments explain **why**, not **what**

## What we will not accept

- Changes that remove invariants from `IMMUTABLE_CORE`
- Changes that add market mechanisms (prices, currency for base goods)
- Changes that give AI more power without corresponding checks
- Changes that introduce hierarchy based on reputation in basic questions

These are not arbitrary restrictions. They are the **core design choices** of the model. If you disagree with them, open an issue first.

## Questions?

Open an issue. We read everything.