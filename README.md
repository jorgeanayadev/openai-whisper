# 

<div align="center" id="top"> 
  <img src="./.github/openai-whisper.png" alt="Example of Subtitles" />

  &#xa0;  
</div>

<h1 align="center">openai-whisper</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/jorgeanayadev/openai-whisper?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/jorgeanayadev/openai-whisper?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jorgeanayadev/openai-whisper?color=56BEB8">

  <!-- <img alt="License" src="https://img.shields.io/github/license/jorgeanayadev/openai-whisper?color=56BEB8"> -->

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/jorgeanayadev/openai-whisper?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/jorgeanayadev/openai-whisper?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/jorgeanayadev/openai-whisper?color=56BEB8" /> -->
</p>


<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#zap-usage">Usage</a> &#xa0; | &#xa0;
  <a href="#vhs-ffmpeg-useful-commands"> FFMPEG useful commands</a> &#xa0; | &#xa0;
  <a href="#page_with_curl-response-formats">Response Formats</a> &#xa0; | &#xa0;
  <a href="https://github.com/jorgeanayadev/" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Using openai for python, this is a script to extract text from speech (speech to text). Added options to get json, text and subtitles format. 

&#xa0;  

## :zap: Usage ##

```bash

python whisper.py <API_KEY> <AUDIO_FILE> <FORMAT_RESPONSE>

```


**:key: <API_KEY>**

Get access to the [openai platform](https://platform.openai.com/) under [account > api keys](https://platform.openai.com/account/api-keys) you can reate a new API-KEY. 

Format: sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

&#xa0;

**🎵 <AUDIO_FILE>**

The audio file to transcribe, in one of these formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm

&#xa0;

**📄 <FORMAT_RESPONSES>**

The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt

&#xa0;

****

EXAMPLE
```bash
# Will create a openai-ceo-sam-altman-ai-reshape-society-acknowledges.srt file with SRT format.
$>python whisper.py sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX openai-ceo-sam-altman-ai-reshape-society-acknowledges.mp3 srt 
``` 
 
&#xa0;
 
## :vhs: FFMPEG useful commands ##


**Extract audio from video**

_Sometimes is better to work with small files even if the api support video formats this will be faster to process._

```bash

$> ffmpeg -i openai-ceo-sam-altman-ai-reshape-society-acknowledges.mp4 -vn -acodec libmp3lame -q:a 2 openai-audio-only.mp3

```

&#xa0;

**Get a fragment of the mp3**

_Useful when you want to test the transcript service if you a have a big file. We'll get the first 30 seconds_
```bash

$> ffmpeg -ss 00:00:00 -to 00:00:30 -i openai-audio-only.mp3 -c copy openai-audio-only-first-30s.mp3

```

&#xa0;

**Add Subtitles to video**

_Finally we can add a valid subtitles file into the video (srt or vtt)_

```bash

$> ffmpeg -i video_file.mp4 -i subtitle_file.srt -c copy -c:s mov_text -metadata:s:s:0 language=spa final_video_with_subtitles.mp4

```

&#xa0;

##  :page_with_curl: Response Formats ##

Here is a list of the response formats whisper will answer you back


**JSON**
```json
{
  "text": "This is a transcript example using openai whisper"
}
```

**VERBOSE JSON**
```json
{
  "task": "transcribe",
  "language": "spanish",
  "duration": 30.02,
  "segments": [
    {
      "id": 0,
      "seek": 0,
      "start": 0.0,
      "end": 7.0,
      "text": "This is a transcript example",
      "tokens": [
        806,
        4631,
        26662,
        383,
        2191,
        289,
        17315,
        2095
      ],
      "temperature": 0.0,
      "avg_logprob": -0.5680031085836477,
      "compression_ratio": 1.6981132075471699,
      "no_speech_prob": 0.5106183290481567,
      "transient": false
    },
    {
      "id": 1,
      "seek": 0,
      "start": 2.0,
      "end": 8.0,
      "text": "using openai whisper",
      "tokens": [
        2458,
        66,
        5291,
        11,
        806,
        4631,
        26662,
        11,
        785
      ]
   }
  ]
}
```


**TEXT**
```text
This is a transcript example using openai whisper 
```


**SRT**
```srt
1
00:00:00,000 --> 00:00:07,000
This is a transcript example

2
00:00:07,060 --> 00:00:09,000
using openai whisper 
```


**VTT**
```vtt
WEBVTT

00:00:00.000 --> 00:00:07.000
This is a transcript example

00:00:07.060 --> 00:00:09.000
using openai whisper 
```

&#xa0;

## 🔗 REFERENCES ##

https://platform.openai.com/docs/api-reference/audio/create

&#xa0;

***

Made with :heart::egg::fire: by <a href="https://github.com/jorgeanayadev/" target="_blank">Jorge Anaya</a>

&#xa0;

<a href="#top">Back to top</a>
