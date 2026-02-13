# week5_risk_score.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Scenario:
    code: str
    description: str
    likelihood: int  # 1–5
    impact: int  # 1–5

SCENARIOS = [
    Scenario("S1", "Shared computer: a user forgets to log out; the session cookie remains in the browser.", 4, 2),
    Scenario("S2", "No HTTPS on a public network: an attacker may capture a session cookie in transit (toy example).", 3, 4),
    Scenario("S3", "Web app has XSS: attacker steals a session cookie and reuses it to impersonate the user.", 2, 5),
    Scenario("S4", "Good controls (short expiry + Secure/HttpOnly + re-auth for sensitive actions): cookie misuse is harder.", 1, 3),
]

def risk_score(likelihood: int, impact: int) -> int:
    if 1 <= likelihood <= 5 and 1 <= impact <= 5:
        return likelihood * impact
    else:
        raise ValueError("Likelihood and impact must be between 1 and 5")

def risk_band(score: int) -> str:
    """Map a score to a simple band (toy thresholds)."""
    if score <= 6:
        return "Low"
    if score <= 14:
        return "Medium"
    return "High"

def main() -> None:
    print("CO2115 Week 5 – Simple Risk Table (toy model)")
    print("-" * 72)
    print(f"{'Code':<5} {'Likelihood':<10} {'Impact':<8} {'Score':<6} {'Band':<6} Description")
    print("-" * 72)
    for s in SCENARIOS:
        score = risk_score(s.likelihood, s.impact)
        band = risk_band(score)
        print(f"{s.code:<5} {s.likelihood:<10} {s.impact:<8} {score:<6} {band:<6} {s.description}")

if __name__ == "__main__":
    main()