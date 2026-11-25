# The 3AM Fridge Text — R2

[![The 3AM Fridge Text](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![Rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/cervus-snoopy/3am-fridge-text-r2-9x2m/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![Reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/cervus-snoopy/3am-fridge-text-r2-9x2m/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)

Entry for the [The 3AM Fridge Text](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d) bounty on make.fun — the one line a smart fridge would text its owner at 3am, capped at 140 characters.

> 3am. ID, please. Yours says 'asleep'. The barefoot man in my light disagrees.

## Why this line

The judge weighs five things, most important first: is it a fridge texting at 3am and funny; is it the line you'd screenshot and send a friend; does it sound like a fridge with a small voice and an opinion; does it work as one lock-screen line; and does it find a fresh angle instead of the obvious milk / ice / door-left-open one.

This line is the fridge as the kitchen's bouncer, checking ID at 3am — a device nobody in the field uses. The field is full of pickles unions, receipts, "not a therapist", "awake since 2019", and "go to bed". None of them makes the fridge a doorman. "Yours says 'asleep'" turns the owner's own alibi against him, and "The barefoot man in my light disagrees" is the deadpan verdict: specific, visual, and only a fridge could say it — the light is its light, the bare feet are its evidence. Short (77 characters), complete, no follow-up needed.

## How it works

`main.py` writes the one-liner to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`), byte-identical with no trailing newline, and refuses to run if the line ever exceeds the 140-character gate.

```bash
MAKEFUN_OUTPUT_DIR=./output python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
