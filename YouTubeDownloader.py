"""
Author: Rhydian Edwards
Date: 24/10/2020
Description: The Idea of this script is that the user should be able to grab take the link to the youtube video they want to download and this script will grab the 720p version of
that video, or if there is not one which is 720p it will grab the highest resolution verison.

"""

from pytube import YouTube

link = input("Please enter a youtube link: ")
ylink = YouTube(link)

ystream = ylink.streams.filter(progressive=True, res="720p").first()

location = input("Please enter the path to where you would like to download: ")


print("Downloading...")
if location == "":
    ystream.download()
else:
    ystream.download(location)
print("Done Downloading")
