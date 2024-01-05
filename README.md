# medianames

# Description
This cmd tool should enable Emby media server to have the proper folder structures in place to make media scraping successful.

## #1 iteration clean file names (wip): 
Commandline tool which cleans the folder and file names recursively for the given folder name.
Per default "." (dot) will be replaced with " " (spaces). This should lead to scraper friendly folder names.

## #2 iteration TV-show support (planned): 
Organizes the folder structure and namings according to your tv-show scraper settings. 
Options to be available:
- default (0): Show/Season/episodes
- deep (1): Show/Season/episode/file
- lazy (2): Show/episodes (Files will be prefixed with "SxEx" to guarantee sorting and scraping)
