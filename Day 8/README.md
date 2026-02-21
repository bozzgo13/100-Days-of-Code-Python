# 🛡️ Caesar Cipher Tool

A Python implementation of the classic **Caesar Cipher** encryption and decryption technique. Instead of using a predefined list for the alphabet, this version utilizes **ASCII code logic** to handle letter shifting.

---

## 📝 Description

The Caesar Cipher is one of the simplest and most well-known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

This specific project demonstrates:
* **ASCII Manipulation**: Using `ord()` and `chr()` functions to shift characters without a manual alphabet list.
* **Wrap-around Logic**: Ensuring that a shift past 'z' circles back to 'a' (and vice-versa for decryption).
* **Non-Alphabetic Preservation**: Symbols, spaces, and numbers remain unchanged during the process.
* **Continuous Loop**: Allows the user to perform multiple operations until typing 'end'.
