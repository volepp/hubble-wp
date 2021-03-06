### Hubble Space Telescope wallpapers

*Note that this was developed on a machine that's running Ubuntu 18.04. The script doesn't seem to work on a machine running Ubuntu 16.04*

This is a small script to fetch an image taken by the Hubble Space Telescope and set it as your wallpaper.

Executing the hubble_wp.py file will do the trick but if you want to schedule the execution (say to run it every hour) with crontab, the hubble-wp.sh file has to be used.

This is how to schedule the script to run every hour:

First you have to edit your crontab:
```
crontab -e
```
If you haven't used crontab before you have to specify which text editor you want to use.

Now add the following line to the end of the file that opens:
```
0 * * * * cd /path/to/hubble-wp && /bin/sh /path/to/hubble-wp/hubble-wp.sh >> /path/to/hubble-wp/log.txt
```

Remember to replace the path to your own one. Now save the file and close the text editor.

Voilà! Now the script is scheduled to run on an hourly basis and every hour you will be greeted with a cool new picture taken by the Hubble Space Telescope!
