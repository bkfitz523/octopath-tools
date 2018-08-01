import json
import pprint

pp = pprint.PrettyPrinter(indent=2)

stat_list = [
    'HP',
    'SP',
    'Physical Attack',
    'Elemental Attack',
    'Physical Defense',
    'Elemental Defense',
    'Accuracy',
    'Speed',
    'Critical',
    'Evasion'
    ]



# ophilia = {'Name': 'Ophilia', 'HP': 225}


# pp.pprint(ophilia)

def get_job_bonuses(job):
    with open('jobs\\{0}.json'.format(job)) as f:
        job_stats = json.load(f) 
    return job_stats


def calculate_job_bonuses(job_a_stats, job_b_stats):
    combined_job_bonuses = {}
    for x in range (0, 10):
        combined_job_bonuses[stat_list[x]] = job_a_stats[stat_list[x]] + job_b_stats[stat_list[x]]
    return combined_job_bonuses

def calculate_character_with_jobs(char_stats, total_job_stats):
    character_new_stats = {}
    for x in range (0, 10):
        character_new_stats[stat_list[x]] = char_stats[stat_list[x]] + (char_stats[stat_list[x]] * total_job_stats[stat_list[x]])
    return character_new_stats


character = 'cyrus'
job_1 = 'scholar'
job_2 = 'merchant'

job_1_stats = get_job_bonuses(job_1)
job_2_stats = get_job_bonuses(job_2)

job_bonuses = calculate_job_bonuses(job_1_stats, job_2_stats)

with open('characters\\{0}.json'.format(character)) as f:
    character_stats = json.load(f)

character_job_combo = calculate_character_with_jobs (character_stats, job_bonuses)
pp.pprint(character_job_combo)

# pp.pprint(job_bonuses)

# print(character_stats['Name'])
# print(character_stats['HP'])
