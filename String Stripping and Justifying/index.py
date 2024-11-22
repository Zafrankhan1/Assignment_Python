s: str = "   Python is fun!   "


trimmed_s = s.strip()

left_justified = trimmed_s.ljust(20, '*')

right_justified = trimmed_s.rjust(20, '*')

print(f"Trimmed: '{trimmed_s}'")
print(f"Left justified: '{left_justified}'")
print(f"Right justified: '{right_justified}'")
