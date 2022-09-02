# SDVX Volforce Breakdown

Calculates Sound Voltex Exceed Gear and Heavenly Haven Volforce for Asphyxia plugin save data.  
Also written to prove how absurd the first Volforce algorithm used in Heavenly Haven actually was compared to Exceed Gear.

This is intended to work with the Asphyxia plugin. 

# Setup

First time users: Make sure your ```music_db.json``` and your ```sdvx@asphyxia.db``` files are in the same directory as these scripts.  
Confirm that these files are from the Asphyxia plugin itself.  
Run ```python 3 song_db_reader.py``` to generate a simplified pickle object of the song database.
Then, run ```python 3 volforce_breakdown.py``` to create a chart that contains score information, as well as VF ranking.
