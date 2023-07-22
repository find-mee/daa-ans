def stableMatch(men, women, men_pref, women_pref):
    proposals = {}
    men_matched = {}
    women_matched = {}

    # Initialize men_matched and proposals dictionaries
    for man in men:
        men_matched[man] = None
        proposals[man] = 0

    # Initialize women_matched and proposals dictionaries
    for woman in women:
        women_matched[woman] = None
        proposals[woman] = 0

    while True:
        free_man = None
        for man in men:
            if men_matched[man] is None and proposals[man] < len(women):
                free_man = man
                break
    
        if free_man is None:
            break

        preferences = men_pref[free_man]

        for woman in preferences:
            if women_matched[woman] is None:
                women_matched[woman] = free_man
                men_matched[free_man] = woman
                proposals[free_man] += 1
                break
            
            current_man = women_matched[woman]
            current_man_index = women_pref[woman].index(current_man)
            free_man_index = women_pref[woman].index(free_man)
            
            if current_man_index > free_man_index:
                women_matched[woman] = free_man
                men_matched[free_man] = woman
                proposals[free_man] += 1
                men_matched[current_man] = None
                break
        
        proposals[free_man] += 1
        
    return men_matched

men = ['A', 'B', 'C']
women = ['V', 'W', 'X']

men_pref = {
    'A': ['V', 'W', 'X'],
    'B': ['W', 'V', 'X'],
    'C': ['V', 'W', 'X']
}

women_pref = {
    'V': ['A', 'B', 'C'],
    'W': ['B', 'C', 'A'],
    'X': ['C', 'A', 'B']
}

men_matched_with_women = stableMatch(men, women, men_pref, women_pref)

for man, woman in men_matched_with_women.items():
    print(f"{man} is matched with {woman}")

