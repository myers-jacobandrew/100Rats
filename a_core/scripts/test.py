import re

import re

def extract_legendary_actions(text):
    legendary_actions = []
    legendary_action_count = 0

    # Extract the count of legendary actions
    action_count_match = re.search(r"(\d+) legendary actions", text)
    if action_count_match:
        legendary_action_count = int(action_count_match.group(1))

    # Find the index where legendary actions start using regex
    action_start_match = re.search(r"\n\n", text)
    if action_start_match:
        start_index = action_start_match.end()
        legendary_actions_text = text[start_index:].strip()

    # Remove leading/trailing whitespace
    legendary_actions_text = legendary_actions_text.strip()

    # Split legendary actions by newline followed by an indented line,
    # capturing cost information within parentheses (optional)
    action_blocks = re.findall(
        r"^([\w\s]+)\s*(?:\(([^)]+)\)\.\s)?(.*?)(?:\n|$)",
        legendary_actions_text,
        re.DOTALL | re.MULTILINE,
    )

    # Append all legendary actions
    for action_name, cost, action_description in action_blocks:
        # Combine action name and cost if present, otherwise use only action name
        if cost:
            action_name = f"{action_name.strip()} (Cost {cost.strip()} Actions)"
        else:
            action_name = action_name.strip()

        # Split the description at the newline character if present
        if '\n' in action_description:
            action_description, additional_description = action_description.split('\n', 1)
            legendary_actions.append({"Legendary Action": action_name, "Legendary Action Description": action_description.strip()})
            legendary_actions.append({"Legendary Action": action_name, "Legendary Action Description": additional_description.strip()})
        else:
            legendary_actions.append({"Legendary Action": action_name, "Legendary Action Description": action_description.strip()})

    return legendary_actions, legendary_action_count



# Define additional test blocks with different creatures and legendary actions
test_blocks = [
    """
    Legendary Actions
    Beholder can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature’s turn. Beholder regains spent legendary actions at the start of its turn.

        Eye Ray. The beholder casts a random eye ray.
        Teleport. The beholder magically teleports up to 120 feet to an unoccupied space it can see.
    """,
    """
    Legendary Actions
    Lich can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature’s turn. Lich regains spent legendary actions at the start of its turn.

        Paralyzing Touch. The lich uses its Paralyzing Touch.
        Frightening Gaze. The lich targets one creature it can see within 10 feet of it. If the target can see the lich, the target must succeed on a DC 18 Wisdom saving throw against this magic or become frightened for 1 minute. The frightened target can repeat the saving throw at the end of each of its turns, with disadvantage if the lich is within line of sight, ending the effect on itself on a success.
        Legendary Resistance (Costs 2 Actions). If the lich fails a saving throw, it can choose to succeed instead.
    """,
    """
    Legendary Actions
    Balor can take 4 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature’s turn. Balor regains spent legendary actions at the start of its turn.

        Whip. The balor makes a melee attack with its whip.
        Teleport. The balor magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see.
        Fire Aura (Costs 2 Actions). The balor ignites flames that shed bright light in a 20-foot radius and dim light for an additional 20 feet. The flames persist until the balor uses a bonus action to extinguish them. Any creature that hits the balor with a melee attack while within 5 feet of it takes 10 (3d6) fire damage.
    """,
    """
    Legendary Actions
    Sphinx can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature’s turn. Sphinx regains spent legendary actions at the start of its turn.

        Claw (Costs 2 Actions). The sphinx makes one claw attack.
        Teleport. The sphinx magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see.
    """,
    """
    Legendary Actions
    Kraken can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature’s turn. Kraken regains spent legendary actions at the start of its turn.

        Tentacle. The kraken makes one tentacle attack.
        Lightning Storm (Costs 2 Actions). The kraken causes a storm in a 60-foot radius centered on a point it can see within 120 feet of it. The storm lasts until the kraken dies or dismisses it as an action.
    """
]

# Loop through each test block
for i, test_block in enumerate(test_blocks, start=1):
    print(f"Test Block {i}:")
    print("-" * 20)
    legendary_actions, legendary_action_count = extract_legendary_actions(test_block)
    print(legendary_actions)
    print()
