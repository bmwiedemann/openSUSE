# ueberzugpp

URL: [ueberzugpp](https://github.com/jstkdng/ueberzugpp)

----

Überzug++ is a command line utility written in C++ which allows to draw images
on terminals by using child windows or using sixel on supported terminals.
This is a drop-in replacement for the now defunct ueberzug project.

Advantages over w3mimgdisplay and ueberzug:

- support for wayland (sway only)
- support for MacOS
- no race conditions as a new window is created to display images
- expose events will be processed, so images will be redrawn on switch
  workspaces
- tmux support on X11
- terminals without the WINDOWID environment variable are supported
- chars are used as position - and size unit
- No memory leak (usage of smart pointers)
- A lot of image formats supported (through opencv and libvips).
- GIF and animated WEBP support on X11 and Sixel
- Fast image downscaling (through opencv and opencl)
- Cache resized images for faster viewing
