# Blackjack
A command-line Blackjack game written in Python. Play against a computer-controlled dealer using standard casino rules.
## How It Works
- The game uses a single 52-card deck (no suits, just ranks — face cards count as 10, Aces count as 11 or 1).
- You and the dealer are each dealt two cards. One of the dealer's cards stays hidden until it's their turn.
- On your turn, choose to **hit** (draw another card) or **stand** (keep your current hand).
- If you go over 21, you bust and lose automatically.
- Once you stand, the dealer draws until their hand totals 17 or higher.
- Standard Blackjack outcomes apply: bust, blackjack (21 with your first two cards), push (tie), win, or lose.
## Requirements
- Python 3
## Usage
```bash
python blackjack.py
```
When prompted, type `hit` to draw a card or `stand` to hold your hand.
## Possible Improvements
- Support playing multiple rounds without restarting the script
- Handle betting and a running balance
- Add input validation for `hit`/`stand`
- Reshuffle or replenish the deck when it runs low
