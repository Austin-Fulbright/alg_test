# Algorithm Testing Repository

A workspace for developing, optimizing, and comparing algorithm solutions across multiple languages and implementations.

**Workflow per problem:**
1. **Python** — initial implementation for clarity and correctness.  
2. **Optimized Python** — refined for performance (e.g., faster algorithms or in‑place tricks).  
3. **C** — manual implementation, built with CMake for speed.  
4. **Rust** — safe, high-performance implementation using Cargo.

---

## 🚀 Getting Started

### Python

```bash
# Run the initial solution:
python3 python/<problem>.py

# Run the optimized version:
python3 python/<problem>_optimized.py
```

### C (CMake)

```bash
cd c
mkdir -p build && cd build
cmake ..
make
# Example: run Game of Life
./game_of_life
```

### Rust (Cargo)

```bash
cd rust/<problem>
cargo build --release
# Run the compiled binary:
cargo run --release
```

---

Feel free to explore each language directory to compare implementation clarity, performance, and memory usage.

