# mythtv-hdhomerun-channel-sync

**Description: Only Show HD/Non-DRM (sorry HB0) HDHomeRun Channels in MythTV**

Please backup your database first!  This script will essentially set ALL channels to be visible=0 before it does its thing.

It will set visible=1 for those channels which are HD and Non-DRM from your HDHomeRun tuner.

You need to ensure that you have channels detected in your http://hdhomerun.local/lineup.html first.

Then this uses a super secret http://hdhomerun.local/lineup.json?show=found url to get the channels in json format, who knew!

Running is as simple as:

```
docker run -it --rm \
-e HDHOMERUN='<IP of your HDHomeRun>' \
-e DBHOST='<IP of your database>' \
-e DATABASE='<mythtv database name, i.e. mythconverg>' \
-e DBUSER='<mythtv database user, i.e. mythtv>' \
-e DBPASS='<mythtv database user password>' \
clueo8/mythtv-hdhomerun-channel-sync
```
