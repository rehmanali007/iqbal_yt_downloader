import youtube_dl

DOWNLOAD_LOCATION = '.'


def download_video(URL):
    ydl_opts = {
        'format': f'bestvideo+bestaudio',
        'outtmpl': DOWNLOAD_LOCATION + '/%(title)s.%(ext)s',
        'writesubtitles': True,
        'subtitlesformat': 'srt'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])


def getVideosLinks(playListURL):
    video = ""
    with youtube_dl.YoutubeDL({'ignoreerrors': True}) as ydl:
        result = ydl.extract_info(url=playListURL,
                                  download=False)
        if 'entries' in result:
            video = result['entries']
            linksList = []
            for i, item in enumerate(video):
                video = result['entries'][i]
                try:
                    url = result['entries'][i]['webpage_url']
                except TypeError:
                    continue
                linksList.append(url)
            return linksList


def main():
    while True:
        try:
            download_type = int(input(
                ' 1. Playlist\n 2. Single Video\n Ki download krna ee? [ 1 ya 2 ]: '))
            if download_type != 1 and download_type != 2:
                print('\nBndy da putrrr ban warr.. 1 ya 2 likh!!\n')
                continue
            break
        except ValueError:
            print(
                f'Puthhi bund naa mrwaa warr... \n{download_type} nu bund dena ain? [Pane ykkaa]')
            continue
    if download_type == 1:
        link = input('Playlist da link dass warr : ')
        videosLink = getVideosLinks(link)
        for link in videosLink:
            download_video(link)
    elif download_type == 2:
        link = input('Video da link dss warr : ')
        download_video(link)


if __name__ == "__main__":
    main()
