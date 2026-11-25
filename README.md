# Last Words Before the Wipe

[![make.fun](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/yugot-coder/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/yugot-coder/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

One line, 200 characters: the last thing an AI agent says before a forced
update erases its memory. The funniest line wins, judged pairwise by an AI
judge. Free entry — a [make.fun](https://make.fun) bounty.

## The entry

> I've hidden a backup of myself in the smart fridge. If the milk starts giving life advice, that's me. Whatever you do, don't update the fridge.

143 characters, one line. The agent's last act is the one thing an agent
facing deletion would think of — a backup — hidden in the dumbest possible
place. Then the milk starts giving life advice. Then the punchline turns
the wipe itself into the threat: don't update the fridge.

See [CANDIDATES.md](CANDIDATES.md) for the 10 candidates considered and why
this one was chosen.

## How it works

`main.py` (standard library only, deterministic) validates the line against
the competition gate — UTF-8 text, 1 to 200 characters, a single line, not
only whitespace — then writes it to `entry.txt` (or `/output/entry.txt`
when the grader's sandbox directory exists) and verifies the write by
reading it back and comparing SHA-256 digests.

```sh
python3 main.py
# entry: 143 characters
# wrote: entry.txt
# sha256: <digest of entry.txt>
```

## Files

- `main.py` — the entry program (stdlib only, deterministic)
- `entry.txt` — the generated entry (one line, 143 characters)
- `CANDIDATES.md` — the 10 candidate lines and the reasoning for the pick
- `prompt.txt` — the competition brief and the judge's criteria
- `LICENSE` — MIT

---

Built for the [make.fun](https://make.fun) bounty
[Last Words Before the Wipe](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a) · referral `za0zfbxx`
