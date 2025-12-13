# FakePassBreaker

FakePassBreaker is a shrine‑style simulation that ritualizes random string generation into the drama of a "password breaker."  
It does **not** connect to servers or perform real password cracking — it’s purely educational and aesthetic.

---

## ✨ Features
- Prompts for a fake IP/hostname and username (e.g. `************@*****`).
- Generates thousands of random "attempts" with counters.
- Prints each attempt in the format:
attempt 5000 mcPEYaOOChq
- Reveals a configurable "real password" at the end.

---

## 🛠 How It Works
- Uses Python’s `random.choice` to build random sequences of letters.
- Stores attempts in a list for later reference.
- Demonstrates Python basics:
- Loops
- String concatenation
- List slicing
- Printing with formatting

---

## ⚡ Example Output
attempt 4999 XyZaBcDeFg attempt 5000 mcPEYaOOChq run ssh **********@********** with the password: *************
---

## 🚫 Disclaimer
FakePassBreaker is **not** a real password breaker.  
It does not connect to SSH, servers, or networks.  
It’s a playful shrine‑style simulation for learning Python and ritualizing output into lore.

---

## 📜 License
MIT License — free to remix, ritualize, and extend.
