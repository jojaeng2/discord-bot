import random

# TODO 유튜브 검색 api 필요
playLists = [
    "https://www.youtube.com/watch?v=KGiJpEHFfTs",
    "https://www.youtube.com/watch?v=m-rdxNdR5G8",
    "https://www.youtube.com/watch?v=XFv5vVxUGlM",
    "https://www.youtube.com/watch?v=W3eKyh88hDo"
]

def getPlayList():
    return playLists[random.randrange(0, len(playLists))]