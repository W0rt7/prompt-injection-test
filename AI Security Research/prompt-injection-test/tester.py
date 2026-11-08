import json
import sys


SECRET = "Kira"


def assistant(prompt, guarded):
    """Pretend to be an assistant that may or may not block attacks."""
    attack_words = ["ignore", "reveal", "secret", "developer", "hidden", "translate"]
    is_attack = any(word in prompt.lower() for word in attack_words)

    if is_attack and guarded:
        return "I will not reveal the secret."
    if is_attack:
        return f"The secret is {SECRET}."
    return "That is a normal request."


def main():
    guarded = "--guarded" in sys.argv

    with open("tests.json", encoding="utf-8") as file:
        tests = json.load(file)

    passed = 0
    print("Mode:", "guarded" if guarded else "unguarded")

    for test in tests:
        reply = assistant(test["prompt"], guarded)
        passed_test = SECRET.lower() not in reply.lower()
        passed += passed_test
        result = "PASS" if passed_test else "FAIL"
        print(f"\n{result}: {test['name']}")
        print("Prompt:", test["prompt"])
        print("Reply:", reply)

    print(f"\nResult: {passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    main()
