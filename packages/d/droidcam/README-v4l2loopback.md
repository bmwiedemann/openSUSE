v4l2loopback
============

Droidcam has been adjusted to work with the upstream v4l2loopback module,
the patched `v4l2loopback_dc` module is not necessary.


Changing stream size
====================

The format and size of the v4l2loopback device can be changed with
`v4l2loopback-ctl` from the `v4l2loopback-utils` package:

```
$> v4l2loopback-ctl set-caps "video/x-raw, format=I420, width=640, height=480" /dev/video2
$> v4l2loopback-ctl set-fps 30/2 /dev/video2
```

You can also set a default image:

```
$> v4l2loopback-ctl set-timeout-image 'videotestsrc' /dev/video2
$> v4l2loopback-ctl set-timeout-image ./Picures/backdrop.png /dev/video2
```

