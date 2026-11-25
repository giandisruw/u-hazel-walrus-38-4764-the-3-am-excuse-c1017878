[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/giandisruw/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/giandisruw/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

# The 3 AM Excuse

One line, 107 characters (limit 200), in the voice of a hardware wallet refusing to sign a transaction at 3 AM:

> At 3 AM I only sign autographs, and only for the fridge light. Come back when your judgment has had coffee.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 107 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were written in the wallet's own voice, deliberately avoiding the clichés the judge brief penalises (batteries, firmware updates, cold storage). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — on subject first, then originality, then the wallet's voice, then how well the line uses the 3 AM hour, then economy of wording. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; 57 of 58 calls returned a verdict (one call returned no verdict and scored 0.5–0.5 per the house rule, none retried).

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| #13 | Pledge with the moon: no transactions after 2 AM, or I turn into a smug brick | **2.75** |
| **#2** | At 3 AM I only sign autographs, and only for the fridge light | **2.65** |
| #6 | Secure element in airplane mode, screen asleep, transaction looks like a dream | 2.65 |
| #11 | Dream tax: one signature, payable in eight hours of sleep | 2.65 |
| #9 | Not a wallet, a nightlight with trust issues; queue behind my beauty sleep | 2.35 |
| #8 | Private key left a note: urgent = scam, not urgent = wait | 2.25 |
| #12 | Screen gone dark out of principle; display refuses to witness this | 2.05 |
| #3 | Seed phrase dreaming it was a toaster; ask again when it's a wallet | 1.9 |
| #1 | Private key asleep, screen on night mode, impulse buy waits for sunrise | 1.7 |
| #4 | Clocked out at midnight; a paperweight with a PIN pad and a union rep | 1.7 |
| #10 | PIN pad only works after eight hours of sleep, like its owner — barely | 1.6 |
| #14 | Your finger is sleepwalking and my key is on strike | 1.4 |
| #5 | Signing voids warranty and dignity; buttons filed a formal complaint | 1.3 |
| #7 | Even my circuits know this is a decision you'll regret by breakfast | 1.05 |

Final: #13 led the Swiss at 2.75, #2 was second at 2.65, and #2 won the final 0.55–0.45 — the judge split the two orders (margin 2 for #13's moon pledge in one order, margin 3 for #2's autograph bit in the other) and preferred #2's fresher angle overall: a wallet treating itself as a celebrity doling out autographs to the fridge light, with the 3 AM hour baked into the joke (it could not be pasted onto a 3 PM transaction) and a deadpan punchline about the owner's judgment needing coffee. #2's line also scores on every brief criterion at once: unmistakably a hardware wallet refusing to sign at 3 AM, an original angle, the device's own voice and grudges, and 107 tight characters with no explanation of its own joke.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
