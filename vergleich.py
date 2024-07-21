import json
from itertools import combinations

def load_quelle(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_quelle(target, quelle):
    target_data = quelle[target]
    results = []

    for (bl1, bl2) in combinations(quelle.keys(), 2):
        if bl1 == target or bl2 == target:
            continue

        bl1_data = quelle[bl1]
        bl2_data = quelle[bl2]

        combined_fläche = bl1_data['fläche'] + bl2_data['fläche']
        combined_einwohner = bl1_data['einwohner'] + bl2_data['einwohner']

        fläche_difference = abs(target_data['fläche'] - combined_fläche)
        einwohner_difference = abs(target_data['einwohner'] - combined_einwohner)

        result = {
            'combination': (bl1, bl2),
            'fläche_difference': round(fläche_difference, 2),
            'einwohner_difference': einwohner_difference
        }

        results.append(result)

    return results

if __name__ == "__main__":
    quelle = load_quelle('quelle.json')
    target = input("Gib das Ziel-Bundesland oder die Ziel-Stadt ein: ")

    if target in quelle:
        vergleiche = compare_quelle(target, quelle)
        vergleiche.sort(key=lambda x: (x['fläche_difference'], x['einwohner_difference']))

        print(f"Die 5 besten Vergleiche für {target}:")
        for vergleich in vergleiche[:5]:
            print(f"Kombination: {vergleich['combination']}, Flächendifferenz: {vergleich['fläche_difference']} km², Einwohnerdifferenz: {vergleich['einwohner_difference']}")
    else:
        print("Das eingegebene Bundesland oder die eingegebene Stadt ist ungültig.")
