# yt-download

custom youtube downloader with python

# prerequisite

install pafy

```bash
python3 -m pip install git+https://github.com/mps-youtube/pafy
```

install youtube_dl

```bash
pip3 install youtube_dl
```

create alias on mac / linux

```bash
alias qw='path_to_python_bin/python3 see.py'
alias qwe='path_to_python_bin/python3 download.py'
```

Using the CLI is extremely straightforward as well. To download a video at the
highest progressive quality, you can use the following command:

```bash
qwe 'https://youtube.com/watch?v=b80a8XKX6ws'
```

or

```bash
qwe b80a8XKX6ws
```

the same thing goes to see info only without download

```bash
qw b80a8XKX6ws
```
