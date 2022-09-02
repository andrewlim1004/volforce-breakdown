import pickle, json

# All multipliers and calculations were taken from BemaniWIKI.

grades6 = [0, 0.8, 0.82, 0.85, 0.88, 0.91, 0.94, 0.97, 1, 1.02, 1.05] # Exceed Gear Multipliers
grades4 = [0, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1] # Heavenly Haven Multipliers
g_strings = ["" , "D", "C", "B", "A", "A+", "AA", "AA+", "AAA", "AAA+", "S"] # LMAO
diffs = ["NOV" , "ADV" , "EXH"]
alt_diffs = ["", "", "INF", "GRV", "HVN", "VVD", "XCD"] # I don't know what the point of doing this is lol
clears = [0, 0.5, 1, 1.02, 1.05, 1.1] # Heavenly Haven not using these was a mistake, thank god they fixed it
c_strings = ["", "FAILED", "CLEAR", "EXCESSIVE", "ULT CHAIN", "PERFECT"]

class Volforce6: # Relevant and more accurate than dan courses

    def __init__ (self, song, abbrev, level, score, grade, clear):
        self.song = song
        self.abbrev = abbrev
        self.level = level
        self.score = score
        self.grade = grade
        self.clear = clear
        self.true_valuation = level * score / 10000000 * grades6[grade] * clears[clear] 
        self.true_val_display = int(self.true_valuation * 1000) / 1000.0
        self.actual_vf = int(self.true_val_display * 20) / 1000.0

    def __str__(self):
        return "VF: {} Valulation: {} | {} {} {} Score: {} Grade: {} Clear: {}".format( 
            self.actual_vf, self.true_val_display, self.song, self.abbrev, self.level, self.score, g_strings[self.grade], c_strings[self.clear])
        
    def __gt__(self, compare_to):
        return self.true_valuation > compare_to.true_valuation

class Volforce4: # This algorithm is so outdated and shitty and is not indicative of a person's skill. This is only here for legacy purposes.
    def __init__ (self, song, abbrev, level, score, grade):
        self.song = song
        self.abbrev = abbrev
        self.level = level
        self.score = score
        self.grade = grade
        self.true_valuation = 25 * (self.level + 1) * score / 10000000 * grades4[grade] # why was there such an overemphasis on chart level lmfao
        self.actual_vf = int(self.true_valuation)
    
    def __str__(self):
        return "VF: {} | {} {} {} Score: {} Grade: {}".format(self.actual_vf, self.song, self.abbrev, self.level, self.score, g_strings[self.grade])
        
    def __gt__(self, compare_to):
        return self.true_valuation > compare_to.true_valuation

def calculate(v6, v4):
    v6.sort(reverse=True)
    v4.sort(reverse=True)
    vol6 = vol4 = 0.0
    print("EXCEED GEAR VOLFORCE BREAKDOWN\n")
    for i in range(50):
        vol6 += v6[i].actual_vf
        print("Rank", i + 1 , str(v6[i]))
    print("EXCEED GEAR VOLFORCE: {}\n".format(int(vol6 * 1000) / 1000.0))  # Exceed Gear always truncates VF values to 3 decimal places, meaning that a good amount of precision is lost.
    print("------------------------------------------------------\n")
    print("HEAVENLY HAVEN VOLFORCE BREAKDOWN\n") # Heavenly Haven always rounds down to the nearest int, so precision loss is also an issue here.
    for i in range(20):
        vol4 += v4[i].actual_vf
        print("Rank", i + 1 , str(v4[i]))
    print("HEAVENLY HAVEN VOLFORCE: {}\n".format(int(vol4)))


def main():
    songs = pickle.load(open("songs.pkl", "rb"))
    f = open("sdvx@asphyxia.db" , "r") # add your sdvx savedata db file here
    vf6 = []
    vf4 = []
    for line in f.readlines(): # if your db file has duplicate scores, run the plugin and close it once it loads. All duplicates should disappear.
        line_dict = json.loads(line)
        if "collection" not in line_dict.keys(): # all scores are stored in JSONs containing the value music in collection.
            continue
        elif line_dict["collection"] != "music": 
            continue
        else:
            id_num = int(line_dict["mid"])
            if id_num not in songs.keys():
                continue
            song = songs[id_num]["song"]
            diff = int(line_dict["type"])
            level = songs[id_num]["diff"][diff]
            abbrev = ""
            if diff == 4:
                abbrev = "MXM"
            elif diff == 3:
                abbrev = alt_diffs[songs[id_num]["inf_str"]]
            else:
                abbrev = diffs[diff]
            score = line_dict["score"]
            clear = line_dict["clear"]
            grade = line_dict["grade"]
        vf6.append(Volforce6(song, abbrev, level, score, grade, clear))
        vf4.append(Volforce4(song, abbrev,level, score, grade))
    calculate(vf6, vf4)


if __name__ == "__main__":
    main()


