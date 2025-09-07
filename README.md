# Secure Login System (C++) - Practice Demo

A minimal command-line login/registration system. Uses **salt + std::hash** for passwords to illustrate the concept of hashing.
> `std::hash` is **NOT cryptographically secure**. This is **for learning only**.

## Build & Run (Windows, using g++)
1. Install **MinGW-w64** (or use WSL/Ubuntu) and ensure `g++` is in PATH.
2. In this folder, run:
   ```bash
   g++ -std=c++17 -O2 -o secure_login main.cpp
   ./secure_login
   ```

## How it works
- On **register**, a random salt is generated; we store `username:salt:digest` in `users.txt`.
- On **login**, we recompute the digest with the stored salt and compare.

## Files
- `main.cpp` - program source
- `users.txt` - generated credentials database *(gitignored)*
