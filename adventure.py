"""A short dungeon run: pick a hero, fight through five areas, face a relic-hoarding boss."""

import random

PRONOUNS = {
    "male": ("him", "his"),
    "female": ("her", "her"),
    "non-binary": ("them", "their"),
}

CLASSES = {
    "rogue": {
        "hp": 95,
        "weapons": [
            {
                "name": "Twin Daggers",
                "low": 10,
                "high": 16,
                "accuracy": 0.90,
                "hits": [
                    "You dart in low and open a gash across the {enemy}",
                    "A flurry of stabs finds the {enemy}'s ribs",
                    "You slip behind the {enemy} and bury both blades",
                ],
                "misses": [
                    "The {enemy} twists away from your blades",
                    "Your daggers scrape off the {enemy}'s guard",
                ],
            },
            {
                "name": "Shortbow",
                "low": 13,
                "high": 20,
                "accuracy": 0.78,
                "hits": [
                    "Your arrow buries itself in the {enemy}",
                    "You loose a shaft clean through the {enemy}'s guard",
                    "A drawn breath, a snap of the string, and the {enemy} staggers",
                ],
                "misses": [
                    "The arrow skitters off stone past the {enemy}",
                    "Your shot goes wide of the {enemy}",
                ],
            },
        ],
    },
    "mage": {
        "hp": 85,
        "weapons": [
            {
                "name": "Frost Wand",
                "low": 11,
                "high": 17,
                "accuracy": 0.85,
                "hits": [
                    "A lance of frost rimes the {enemy}",
                    "Ice cracks across the {enemy}'s hide",
                    "Your wand hums and hoarfrost sears the {enemy}",
                ],
                "misses": [
                    "The frost bolt fizzles short of the {enemy}",
                    "Rime spreads harmlessly past the {enemy}",
                ],
            },
            {
                "name": "Fire Staff",
                "low": 15,
                "high": 23,
                "accuracy": 0.72,
                "hits": [
                    "A gout of flame washes over the {enemy}",
                    "Your fireball bursts against the {enemy}",
                    "Cinders coil down the staff and engulf the {enemy}",
                ],
                "misses": [
                    "The flames roar wide of the {enemy}",
                    "Your spell guts out before it reaches the {enemy}",
                ],
            },
        ],
    },
    "warrior": {
        "hp": 100,
        "weapons": [
            {
                "name": "Sword & Shield",
                "low": 9,
                "high": 15,
                "accuracy": 0.88,
                "hits": [
                    "You batter the {enemy} down with your shield and run it through",
                    "Your blade bites deep into the {enemy}",
                    "You turn the {enemy}'s lunge and answer with steel",
                ],
                "misses": [
                    "The {enemy} turns your blade aside",
                    "Your thrust glances off the {enemy}",
                ],
            },
            {
                "name": "Greataxe",
                "low": 14,
                "high": 23,
                "accuracy": 0.70,
                "hits": [
                    "You cleave into the {enemy} with a two-handed swing",
                    "The axe head crunches through the {enemy}'s guard",
                    "You bring the greataxe down and the {enemy} folds",
                ],
                "misses": [
                    "Your heavy swing carves empty air",
                    "The {enemy} steps inside your arc",
                ],
            },
        ],
    },
}

ENEMY_HITS = [
    "The {enemy} lands a solid blow",
    "The {enemy} presses in and catches you",
    "You take a hit from the {enemy}",
]

ENEMY_MISSES = [
    "The {enemy} lunges and misses",
    "You slip aside from the {enemy}'s attack",
    "The {enemy}'s strike goes wide",
]

PAWNS = [
    {"name": "Goblin Scout", "hp": 16, "low": 3, "high": 6, "accuracy": 0.60},
    {"name": "Giant Rat", "hp": 14, "low": 3, "high": 5, "accuracy": 0.55},
    {"name": "Cave Bat", "hp": 15, "low": 3, "high": 5, "accuracy": 0.65},
    {"name": "Skeleton", "hp": 20, "low": 4, "high": 6, "accuracy": 0.55},
    {"name": "Green Slime", "hp": 22, "low": 3, "high": 6, "accuracy": 0.50},
    {"name": "Bandit Cutpurse", "hp": 18, "low": 4, "high": 7, "accuracy": 0.60},
    {"name": "Wild Boar", "hp": 21, "low": 4, "high": 7, "accuracy": 0.55},
    {"name": "Kobold Digger", "hp": 16, "low": 3, "high": 6, "accuracy": 0.60},
    {"name": "Shambling Zombie", "hp": 22, "low": 4, "high": 6, "accuracy": 0.50},
    {"name": "Soot Imp", "hp": 14, "low": 4, "high": 6, "accuracy": 0.65},
]

ELITES = [
    {"name": "Orc Berserker", "hp": 40, "low": 8, "high": 13, "accuracy": 0.62},
    {"name": "Dire Wolf Alpha", "hp": 33, "low": 7, "high": 11, "accuracy": 0.70},
    {"name": "Harpy Matron", "hp": 31, "low": 7, "high": 11, "accuracy": 0.68},
    {"name": "Cave Troll", "hp": 44, "low": 9, "high": 13, "accuracy": 0.58},
    {"name": "Stone Golem", "hp": 42, "low": 8, "high": 12, "accuracy": 0.60},
    {"name": "Bandit Captain", "hp": 35, "low": 7, "high": 12, "accuracy": 0.68},
    {"name": "Grave Wraith", "hp": 32, "low": 8, "high": 12, "accuracy": 0.65},
    {"name": "Basilisk", "hp": 36, "low": 8, "high": 13, "accuracy": 0.62},
    {"name": "Minotaur", "hp": 41, "low": 9, "high": 13, "accuracy": 0.60},
    {"name": "Flame Cultist", "hp": 30, "low": 7, "high": 11, "accuracy": 0.72},
]

BOSSES = [
    {
        "name": "Ancient Dragon",
        "hp": 108,
        "low": 11,
        "high": 17,
        "accuracy": 0.72,
        "prize": "Emberheart Crown",
        "hint": (
            "They say the Emberheart Crown still burns at the mountain's root, "
            "curled beneath something very old and very patient."
        ),
        "speech": [
            "\"Little spark. I have outlived your grandmother's grandmother.\"",
            "\"Every thief who wanted my crown is ash beneath your boots.\"",
            "\"Come. Let me see what colour you burn.\"",
        ],
        "epilogue": (
            "The great wyrm settles, and the mountain's heat goes out of the air. "
            "You lift the Emberheart Crown from the cinders; it warms your hands "
            "without burning them. The valley below never freezes again, and the "
            "villages there light their winter fires from a single ember of yours."
        ),
    },
    {
        "name": "Lich King",
        "hp": 98,
        "low": 11,
        "high": 17,
        "accuracy": 0.78,
        "prize": "Phylactery of Endless Night",
        "hint": (
            "The Phylactery of Endless Night is said to lie at the bottom of the "
            "crypts, cradled by a king who refused to stop being one."
        ),
        "speech": [
            "\"You are the ninth this century. The others also had names.\"",
            "\"Death is a door I nailed shut. You are welcome to knock.\"",
            "\"Kneel, and I will make your ending brief.\"",
        ],
        "epilogue": (
            "The crown of bone clatters to the flagstones and is still. You take up "
            "the Phylactery of Endless Night and break it against the altar, and a "
            "hundred years of held-back dawn come flooding into the crypt. The dead "
            "sleep properly at last, and you walk out into a morning that is finally allowed to happen."
        ),
    },
    {
        "name": "Ogre Warlord",
        "hp": 112,
        "low": 10,
        "high": 16,
        "accuracy": 0.72,
        "prize": "Warhorn of the Broken Peaks",
        "hint": (
            "Somewhere past the bridge hangs the Warhorn of the Broken Peaks, "
            "and something enormous has been using it to call its war-bands home."
        ),
        "speech": [
            "\"Small thing. Loud boots.\"",
            "\"I have broken three hundred like you across this knee.\"",
            "\"The horn is mine. Come and be the three hundred and first.\"",
        ],
        "epilogue": (
            "The warlord topples like felled timber and the horde's drums fall silent. "
            "You cut down the Warhorn of the Broken Peaks and sound it once - a long, "
            "clean note that scatters the war-bands back into the hills. The mountain "
            "roads are safe for caravans again, and travellers still swear they hear "
            "that note on a clear night."
        ),
    },
    {
        "name": "Abyssal Kraken",
        "hp": 110,
        "low": 11,
        "high": 16,
        "accuracy": 0.74,
        "prize": "Tideglass Pearl",
        "hint": (
            "The Tideglass Pearl rests in the flooded deep, and the water down there "
            "moves when nothing should be moving it."
        ),
        "speech": [
            "\"You came down into the dark. Air-thing. Brief thing.\"",
            "\"The sea kept the pearl safe for an age before your kind had words.\"",
            "\"Breathe deep. It is the last one you may spend.\"",
        ],
        "epilogue": (
            "The coils go slack and sink, and the flood drains away through the cracks "
            "it came from. The Tideglass Pearl sits cool in your palm, showing you calm "
            "water wherever you look into it. Fisherfolk on that coast never lose a boat "
            "to a storm again, and they name the harbour after you."
        ),
    },
    {
        "name": "Fallen Paladin",
        "hp": 102,
        "low": 10,
        "high": 16,
        "accuracy": 0.78,
        "prize": "Oath-Sworn Blade",
        "hint": (
            "The Oath-Sworn Blade was never lost - it is still being carried, by someone "
            "who swore to guard it and then forgot why."
        ),
        "speech": [
            "\"I held this door before you were born. I hold it still.\"",
            "\"My order is dust and my oath is all that is left of me.\"",
            "\"If you want the blade, you will have to take the oath with it.\"",
        ],
        "epilogue": (
            "The fallen knight kneels, and this time it looks like rest. You take up the "
            "Oath-Sworn Blade and speak the old words over the body, finishing a vow that "
            "waited centuries for an ending. The blade never dulls in your hand, and the "
            "order is founded again - this time by someone who remembers what it was for."
        ),
    },
]

AREAS = [
    {
        "name": "The Mossy Gate",
        "spawn": ("pawn", 1, 2),
        "intro": (
            "Ivy has pulled the gatehouse half into the earth. Something small and "
            "hungry is already moving in the green dark."
        ),
        "cleared": (
            "Well fought - the gate is yours. You scrape the moss from a worn "
            "signpost and read a name half the kingdom has forgotten. The road "
            "beyond slopes down, and down, and down."
        ),
    },
    {
        "name": "The Sunken Crypt",
        "spawn": ("pawn", 2, 2),
        "intro": (
            "Water stands ankle-deep between the tombs, and the lids of them are all "
            "on the wrong way round."
        ),
        "cleared": (
            "Nicely done. The last echo dies out among the tombs. Carved along the "
            "wall is a procession of figures carrying something bright toward the "
            "mountain's heart - and every one of them is walking the way you are."
        ),
    },
    {
        "name": "The Ember Tunnels",
        "spawn": ("mix", 1, 1),
        "intro": (
            "The rock here is warm to the touch. Cinders drift upward instead of "
            "settling, and the passage narrows around you."
        ),
        "cleared": (
            "That was a harder one - well earned. You catch your breath against the "
            "warm stone. The tunnel ahead breathes with a slow draft, as if the "
            "mountain is waiting to see whether you keep going."
        ),
    },
    {
        "name": "The Howling Bridge",
        "spawn": ("elite", 1, 2),
        "intro": (
            "A span of black stone crosses a gorge with no bottom worth mentioning. "
            "The wind up here sounds unpleasantly like speech."
        ),
        "cleared": (
            "Superb - the bridge is crossed and the wind falls quiet behind you. "
            "Ahead, a doorway stands open in the cliff face, and warm light spills "
            "out of it across the stone. Whatever waits in there already knows your name."
        ),
    },
    {
        "name": "The Throne of Ash",
        "spawn": ("boss", 1, 1),
        "intro": (
            "The hall is vast and grey, and everything in it has burned once already. "
            "At the far end, the prize you came for - and its keeper."
        ),
        "cleared": "",
    },
]

POTIONS = 3
POTION_HEAL = 30
DEFEND_REDUCTION = 0.5
FLEE_CHANCE = 0.5
MAX_NAME = 20
RULE_WIDTH = 56
BAR_WIDTH = 10

ACTIONS = {
    "a": "attack",
    "d": "defend",
    "p": "potion",
    "f": "flee",
}


def _rule(char="-"):
    print(char * RULE_WIDTH)


def _bar(current, maximum):
    filled = max(0, round(BAR_WIDTH * current / maximum))
    return "[" + "#" * filled + "-" * (BAR_WIDTH - filled) + "]"


def _choose(prompt, options):
    while True:
        print()
        for i, option in enumerate(options, 1):
            print(f"{i}) {option}")
        entry = input(f"{prompt} ").strip().lower()

        if entry.isdigit() and 1 <= int(entry) <= len(options):
            return options[int(entry) - 1]
        for option in options:
            if entry == option.lower():
                return option
        print("Pick one of the numbers or type the name exactly.")


def _choose_action():
    while True:
        entry = input("Action - [a]ttack  [d]efend  [p]otion  [f]lee: ").strip().lower()
        if entry in ACTIONS:
            return ACTIONS[entry]
        if entry in ACTIONS.values():
            return entry
        print("Type a, d, p or f.")


def _ask_name():
    name = input("\nWhat name will the songs remember you by? ").strip()
    return (name[:MAX_NAME] if name else "Wanderer")


def _roll_attack(attacker):
    if random.random() < attacker["accuracy"]:
        return random.randint(attacker["low"], attacker["high"])
    return 0


def _describe(lines, enemy_name):
    return random.choice(lines).format(enemy=enemy_name)


def _spawn(area, boss):
    tier, low, high = area["spawn"]
    if tier == "boss":
        drawn = [dict(boss)]
    elif tier == "mix":
        drawn = [dict(random.choice(PAWNS)), dict(random.choice(ELITES))]
    else:
        pool = PAWNS if tier == "pawn" else ELITES
        drawn = [dict(e) for e in random.sample(pool, random.randint(low, high))]
    for enemy in drawn:
        enemy["max_hp"] = enemy["hp"]
    return drawn


def fight(player, enemy):
    weapon = player["weapon"]
    print()
    _rule("=")
    print(f"  {enemy['name']} ({enemy['hp']} HP) blocks your way!")
    _rule("=")
    round_number = 0

    while True:
        round_number += 1
        print()
        _rule()
        print(f"Round {round_number}")
        print(
            f"  {player['name']:<16} {_bar(player['hp'], player['max_hp'])} "
            f"{player['hp']}/{player['max_hp']} HP   potions: {player['potions']}"
        )
        print(
            f"  {enemy['name']:<16} {_bar(enemy['hp'], enemy['max_hp'])} "
            f"{enemy['hp']}/{enemy['max_hp']} HP"
        )
        _rule()
        action = _choose_action()
        print()
        defending = False

        if action == "attack":
            damage = _roll_attack(weapon)
            if damage:
                enemy["hp"] -= damage
                print(f"  > {_describe(weapon['hits'], enemy['name'])} ({damage} damage).")
            else:
                print(f"  > {_describe(weapon['misses'], enemy['name'])}.")
            if enemy["hp"] <= 0:
                enemy["hp"] = 0
                print(f"  > The {enemy['name']} falls.")
                return "won"

        elif action == "defend":
            defending = True
            print("  > You set your guard and brace for the next blow.")

        elif action == "potion":
            if not player["potions"]:
                print("  > Your last vial is already empty.")
                continue
            if player["hp"] >= player["max_hp"]:
                print("  > You are unhurt - no sense wasting a vial.")
                continue
            player["potions"] -= 1
            healed = min(POTION_HEAL, player["max_hp"] - player["hp"])
            player["hp"] += healed
            print(f"  > You drink a potion and recover {healed} HP.")

        else:
            if random.random() < FLEE_CHANCE:
                print("  > You break away and run for the daylight.")
                return "fled"
            print(f"  > You turn to run and the {enemy['name']} cuts you off.")

        damage = _roll_attack(enemy)
        if damage:
            if defending:
                damage = max(1, int(damage * DEFEND_REDUCTION))
                print(
                    f"  < {_describe(ENEMY_HITS, enemy['name'])}, but your guard holds "
                    f"({damage} damage)."
                )
            else:
                print(f"  < {_describe(ENEMY_HITS, enemy['name'])} ({damage} damage).")
            player["hp"] -= damage
        else:
            print(f"  < {_describe(ENEMY_MISSES, enemy['name'])}.")

        if player["hp"] <= 0:
            player["hp"] = 0
            return "died"


def play_adventure():
    name = _ask_name()
    gender = _choose("Choose your gender:", list(PRONOUNS))
    obj, possessive = PRONOUNS[gender]
    klass = _choose("Choose your class:", list(CLASSES))
    weapon_names = [w["name"] for w in CLASSES[klass]["weapons"]]
    chosen = _choose("Choose your weapon:", weapon_names)
    weapon = next(w for w in CLASSES[klass]["weapons"] if w["name"] == chosen)

    player = {
        "name": name,
        "hp": CLASSES[klass]["hp"],
        "max_hp": CLASSES[klass]["hp"],
        "weapon": weapon,
        "potions": POTIONS,
    }

    boss = random.choice(BOSSES)

    print(f"\n=== {name} of the {klass.title()}s ===")
    print(
        f"{name} takes up {possessive} {weapon['name']} and steps under the broken arch. "
        f"Five halls lie between {obj} and the deep, and {name} intends to walk every one of them."
    )
    print(boss["hint"])
    print(f"You carry {player['potions']} healing potions. Nothing else is coming to help.")

    for index, area in enumerate(AREAS, 1):
        print(f"\n=== Area {index}: {area['name']} ===")
        print(area["intro"])

        if area["spawn"][0] == "boss":
            print()
            for line in boss["speech"]:
                print(line)

        for enemy in _spawn(area, boss):
            result = fight(player, enemy)
            if result == "died":
                print(f"\n{name} falls in {area['name']}, and the {boss['prize']} stays lost.")
                print("The dungeon keeps its quiet. Somewhere, someone else hears the story and starts sharpening a blade.")
                return
            if result == "fled":
                print(f"\n{name} escapes with {possessive} life.")
                print(
                    f"The {boss['prize']} remains where it has always been - but so does {name}, "
                    "breathing, under an open sky. Not every story needs a relic in it."
                )
                return

        if area["cleared"]:
            print(f"\n{area['cleared']}")

    print(f"\n=== The {boss['prize']} ===")
    print(boss["epilogue"])
    print(f"And {name} lived happily ever after.")
