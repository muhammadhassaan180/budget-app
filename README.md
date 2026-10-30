# Budget App

A freeCodeCamp Python certification project: a budget tracker built with Python classes — track spending across categories and visualize relative spending in a text-based chart.

## Features

- **Category class:** `deposit`, `withdraw`, `get_balance`, `transfer`, and `check_funds`, all backed by a transaction ledger
- **Transfers:** move money between categories with automatic `Transfer to/from` descriptions — `check_funds` prevents overdrafts
- **Formatted statement:** printing a category shows a 30-character title bar, aligned transaction descriptions and amounts, and the total
- **Spend chart:** `create_spend_chart` renders a text bar chart of spending percentages per category

## How to Run

```bash
python main.py
```

## What I Learned

1. **Classes clicked:** the `Category` class — ledger, deposits/withdrawals, transfers, and reusing `check_funds` in two places — was understandable and satisfying to build
2. **The hard part was `create_spend_chart`:** summing withdrawals, flooring percentages to the nearest 10, and drawing an ASCII grid row by row. I needed help here — and now understand how each piece works
3. **`range(start, stop, step)`:** counting down (100 → 0) to draw the chart top-down
4. **Requirements can go beyond the lessons:** reading them carefully and breaking a big problem into small steps is its own skill

---

*Built as part of the freeCodeCamp Scientific Computing with Python certification.*
