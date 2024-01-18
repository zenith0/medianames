import re

def clean_folder_name(folder_name):
    # Define a pattern to extract season and episode
    pattern = re.compile(r"([A-Za-z]+(\.[A-Za-z]+)+)[0-9]*\.[0-9]+([A-Za-z]+(\.[A-Za-z]+)+)", re.IGNORECASE)
    episode_pattern = re.compile(r'S(\d{1,2})E(\d{1,2})',  re.IGNORECASE)
    code_pattern=re.compile(r"([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?-[A-Za-z]+", re.IGNORECASE)
    title = re.sub(pattern, "", folder_name)
    match = episode_pattern.search(title)

    season_number = None
    episode_number = None

    if match:
        season_number = match.group(1)
        episode_number = match.group(2)
        title = re.sub(episode_pattern, "", title)
    else:
        print("episode pattern not found.")
    title = re.sub(code_pattern, "", title)

    # Replace dots with spaces in the first part
    title = title.replace('.', ' ')
    title = title.replace(".mkv", "")
    title = title.replace("mkv", "")

    # Can be that the last char was also a . 
    ## so we need to remove the last blank again
    while title[-1] == " ":
        title = title[:-1]
 
    if season_number:
        title = title + "-" + f'S{season_number.zfill(2)}'
    if episode_number:
         title = title + f'E{episode_number.zfill(2)}'


    
    return title   

def is_episode(folder_name):
    episode_pattern = re.compile(r'E(\d{1,2})', re.IGNORECASE)
    match = episode_pattern.search(folder_name)
    if match:
        return True 
    return False

def is_season(folder_name):
    season_pattern = re.compile(r'S(\d{1,2})', re.IGNORECASE)
    match = season_pattern.search(folder_name)
    if match:
        return True 
    return False

def get_season(folder_name):
    season_pattern = re.compile(r'S(\d{1,2})', re.IGNORECASE)
    match = season_pattern.search(folder_name)
    if match:
        return match.group(0) 

def get_show(folder_name):
    season_pattern = re.compile(r'\s*-\s*S(\d{1,2})',  re.IGNORECASE)
    episode_pattern = re.compile(r'E(\d{1,2})',  re.IGNORECASE)
    res = re.sub(season_pattern, "", folder_name)
    res = re.sub(episode_pattern, "", res)
    return res

