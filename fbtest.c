/*
 * fbtest(.c)
 *
 * Copyright 2008 Werner Fink, 2008 SUSE LINUX Products GmbH, Germany.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 */

#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/sysmacros.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <errno.h>
#include <fcntl.h>
#include <getopt.h>
#include <unistd.h>
#include <linux/fb.h>

static struct option options[] = {
    { "fb",   required_argument, 0, 'f'},
    { "vc",   required_argument, 0, 'C'},
    { "help", no_argument,	 0, 'h'},
    { (const char*)0, 0, (int*)0, 0}
};

int main(int argc, char * argv[])
{
    struct fb_con2fbmap map = {1, -1};
    const char *base = basename(argv[0]);
    const char * fb = (char*)0;
    const char * vc = (char*)0;
    struct stat st;
    int c, fd;

    opterr = 0;
    while ((c = getopt_long(argc, argv, "hf:C:", options, (int *)0)) != -1) {
	switch (c) {
	case 'f':
	    fb = optarg;
	    break;
	case 'C':
	    vc = optarg;
	    break;
	case 'h':
	    fprintf(stderr, "%s: Usage:\n    %s [-f <fb_device>] [-C <vc_device>]\n", base, base);
	    fprintf(stderr, "Valid options are:\n");
	    fprintf(stderr, "    -f <fb_device>       The frame buffer device (default /dev/fb0)\n");
	    fprintf(stderr, "    -C <vc_device>       The virtual console device (default /dev/tty1)\n");
	    return 0;
	case '?':
	    fprintf(stdout, "%s: Invalid option for help use:\n    %s --help\n", base, base);
	    return 1;
	    break;
	default:
	    break;
	}
    }

    if (fb == (char*)0) {
	fb = "/dev/fb/0";
	if (stat(fb, &st) < 0) {
	    if (errno != ENOENT && errno != ENOTDIR) {
		fprintf(stderr, "%s: %s: %m\n", base, fb);
		return 1;
	    }
	    fb = "/dev/fb0";
	    if (stat(fb, &st) < 0) {
		fprintf(stderr, "%s: %s: %m\n", base, fb);
		return 1;
	    }
	}
    }

    if (vc == (char*)0)
	vc = "/dev/tty1";

    if (stat(vc, &st) < 0) {
	fprintf(stderr, "%s: %s: %m\n", base, vc);
	return 1;
    }

    if (major(st.st_rdev) != (dev_t)4) {
	errno = ECANCELED;
	fprintf(stderr, "%s: %s: %m\n", base, vc);
	return 1;
    }

    if ((fd = open(fb, O_RDONLY|O_NOCTTY)) < 0) {
	if (errno != ENODEV)
	    fprintf(stderr, "%s: %s: %m\n", base, fb);
	return 1;
    }

    map.console = (typeof(map.console))minor(st.st_rdev);
    map.framebuffer = (typeof(map.framebuffer))-1;

    if (ioctl(fd, FBIOGET_CON2FBMAP, &map) < 0) {
	fprintf(stderr, "%s: %s: %m\n", base, fb);
	return 1;
    }

    return map.framebuffer > FB_MAX;
}
