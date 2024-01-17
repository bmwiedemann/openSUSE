# minidlna container

The command to run this container is as example:

```sh
  podman run -d --rm -v /media:/media --net=host --name minidlna --env MINIDLNA_MEDIA_DIR=/media registry.opensuse.org/opensuse/minidlna
```

Note: You need to run the container in host mode for it to be able to receive UPnP broadcast packets. The default bridge mode will not work.

Supported environment variables:

Prefix any configuration directive of MiniDLNA with MINIDLNA_
E.g.:
MINIDLNA_MEDIA_DIR=/media
MINIDLNA_MEDIA_DIR_1=A,/media/audio
MINIDLNA_MEDIA_DIR_2=V,/media/video
MINIDLNA_FRIENDLY_NAME="My DNLA Server"
