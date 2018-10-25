###Hubble Space Telescope wallpaper

This is a small script to fetch an image taken by the Hubble Space Telescope and set it as your wallpaper.

Executing the hubble_wp.py file will do the trick but if you want to schedule the execution (say to run it every hour) with crontab, the hubble-wp.sh file has to be used.

This is how to schedule the script to run every hour:

First you have to edit your crontab:
''' 
crontab -e
'''
If you haven't used crontab before you have to specify which text editor you want to use.
Then you have to add the following line to the end of the file that opens:
'''
0 * * * * /bin/sh /home/USER/hubble-wp/hubble-wp.sh >> /home/USER/hubble-wp/log.txt
'''

Remember to replace the user with your own username. Now save the file and close the text editor.

Voilà! Now the script is scheduled to on an hourly basis and every hour you are greeted with a new cool picture taken by the Hubble Space Telescope!
