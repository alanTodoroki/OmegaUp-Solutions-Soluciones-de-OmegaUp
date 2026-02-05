# 🍉 Watermelon - Logic Challenge

## 📌 Problem Description

The goal is to determine if a given weight `w` can be divided into two parts, such that each part is a **positive even integer**.
*Note: The parts do not have to be equal.*

## 🧠 Logic & Analysis

Through mathematical analysis, we identified two essential conditions for a successful split:

1. **Parity**: The total weight `w` must be an even number ($w \pmod 2 = 0$).

2. **Minimum Bound**: The smallest possible sum of two positive even numbers is $2 + 2 = 4$. Therefore, even though **2** is an even number, it cannot be split into two positive even parts ($1 + 1$ are odd).

## 🛠️ Implementation

The solution is implemented in **Python 3** using a constant time complexity $O(1)$, ensuring maximum efficiency.

### Key Concepts Used:

* **Modulus Operator (`%`)**: To check for parity.

* **Conditional Logic**: To handle the edge case (weight = 2).

* **Type Hinting**: For cleaner and more maintainable code.


## 🚀 How to Run

1. Make sure you have Python installed.

2. Run the script:

   ```bash

   python solution.py 