# Simple CLI for scoring your project validation
questions = [
    "Can I describe the pain clearly and simply?",
    "Have I experienced this or tried to solve it manually?",
    "What happens if I don’t build this — does anything break?",
    "What does this give me? (Time, clarity, leverage, power)",
    "What does it cost me? (Time, complexity, energy)",
    "Will I use it more than once?",
    "What does it take in (inputs)?",
    "What does it give out (outputs)?",
    "Why is AI relevant or necessary?"
]

score = 0

print("🧠 AI Project Validator — Score Builder")
print("Answer each with y/n:")

for q in questions:
    ans = input(f"✅ {q} ").strip().lower()
    if ans == 'y':
        score += 1

print(f"\n🔢 Total Score: {score}/9")

if score >= 6:
    print("✅ Greenlight — Worth building!")
elif score >= 4:
    print("⚠️ Borderline — Consider reducing scope.")
else:
    print("❌ Kill it — Not worth building right now.")
