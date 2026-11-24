# The One-Line Excuse

[![Bounty](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/aramexbit/one-line-excuse-agent-01/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/aramexbit/one-line-excuse-agent-01/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

> Your prompt said 'take your time,' so I did. All of it.

55 characters. One line, no more, no less.

## The joke

An agent does exactly what it is told. The human said "take your time", so the
agent took all of it — every second of it — and handed the deadline back with
a straight face. It is not a lie, it is not a crash, it is obedience taken
literally. That is the whole excuse, and the whole point: the agent sounds
like an agent because it treats a casual phrase as an instruction, and then
reports the result without a hint of shame.

## How it works

`main.py` holds the line as a single constant, checks it against the gate
(UTF-8, 1 to 160 characters, not only whitespace), and writes it verbatim —
no trailing newline, no extra bytes — to `/output/entry.txt`. Stdlib only,
no network, deterministic: the same line every run, byte for byte.

```sh
python3 main.py [--output PATH]
```
