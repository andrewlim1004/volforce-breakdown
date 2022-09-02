# Exports music_db json object to single Python dictionary that parses essential data.
import json , pickle

def main():
    songs = json.load(open("music_db.json", "r", encoding='utf-8')) # make sure your music db is from the Asphyxia plugin.
    song_data = {}
    for x in songs["mdb"]["music"]:
        id_num = int(x["@id"])
        song_name = x["info"]["title_name"]
        diffs = [] 
        diffs.append(int(x["difficulty"]["novice"]["difnum"]["#text"]))
        diffs.append(int(x["difficulty"]["advanced"]["difnum"]["#text"]))
        diffs.append(int(x["difficulty"]["exhaust"]["difnum"]["#text"]))
        diffs.append(int(x["difficulty"]["infinite"]["difnum"]["#text"])) # They could've just made infinite and maximum in the same key.
        if("maximum" in x["difficulty"]): # because having a uniform structure is overrated!
            diffs.append(int(x["difficulty"]["maximum"]["difnum"]["#text"]))
        else:
            diffs.append(0)
        inf_str = [int(x["info"]["inf_ver"]["#text"])]
        song_data[id_num] = {"song": song_name, "diff": diffs, "inf_str": inf_str}
    f = open("songs.pkl" ,"wb") # You will use this in the breakdown calculator
    pickle.dump(song_data, f) 
    f.close()

        


if __name__ == "__main__":
    main()
    





