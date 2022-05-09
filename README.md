This is a script which retrieves the most recent accounts that specific users have followed. Useful way to hunt for new crypto projects. If reader isn't familiar with Django file structure, the script is found in Twitscrape -> views.py. Simple UI can be viewed at https://twitbot14.herokuapp.com/

Twitter api has a throttle on requests. A single page load of this scraper hits the limit, so page can only be loaded once every 15 minutes. I never added a proper 404, so if page doesn't work, that's probably why

Django secret key was left in, didn't need to mess around with making environment var since this was a personal project with no valuable private data
