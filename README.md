# fmg

## The fmagnet file

*"A worse torrent file, that isn't a torrent file at all."*

An fmagnet file contains three things:
- The file name
- The link to that file
- Whether or not to use yt-dlp to download the file

To generate an fmagnet file use the included `fmg` utility.

```
fmg generate myarchive.fmagnet
```

To preview the contents of an fmagnet file, run the following:
```
fmg preview myarchive.fmagnet
```

To download the file within an fmagnet file run the following:
```
fmg download myarchive.fmagnet
```
