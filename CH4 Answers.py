#Problem 1
import re
emails = ["user@example.com", "bad-email", "test@domain.org"]
pattern = r"^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.(com|org|edu)$"
for email in emails:
    if re.match(pattern, email):
        print(f"{email} → Valid")
    else:
        print(f"{email} → Invalid")

#Problem 2
import re
text = "I love #Python and #AI."
hashtags = re.findall(r"#\w+", text)
print(hashtags)

#Problem 3
import re
pattern = r"^(\(\d{3}\)|\d{3})[-.]\d{3}[-.]\d{4}$"
tests = ["(123)-456-7890", "123-456-7890", "123.456.7890", "5551234"]
for t in tests:
    print(t, "→", bool(re.match(pattern, t)))


#Problem 4
import re
from collections import Counter
text = "Python, Python! AI is great; python AI."
words = re.findall(r"[A-Za-z]+", text)
counts = Counter(word.capitalize() for word in words)
print(dict(counts))

#Problem 5
import re
text = "This is is a test test"
duplicates = re.findall(r"\b(\w+)\s+\1\b", text)
matches = [f"{w} {w}" for w in duplicates]
print(matches)


#Problem 6
import re
text = "The events are on 2023-05-12 and 2024-01-01."
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
print(dates)


#Problem 7
import re
text = "Card: 1234-5678-9012-3456"
masked = re.sub(r"\d(?=\d{4})", "*", text)
print(masked)


#Problem 8
import re
text = "I know Python, Java, and C++ but not Ruby."
languages = re.findall(r"\b[A-Za-z]+\+*\b", text)
print(languages)