#
# spec file for package hello
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gphoto2-webcam
Summary:        A wrapper script for running a webcam based on gphoto2
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
Version:        1
Release:        0
Url:            http://gphoto.org/
Source0:        gphoto2-webcam.sh
Source1:	COPYING
Requires:  	gphoto
Requires:  	ffmpeg
Requires:  	v4l-utils
Requires:  	kmod(v4l2loopback.ko)

%description
This package contains a gphoto2-webcam script that feeds gphoto2 previews
into a virtual video4linux2 loopback device.

You need to run as root:

	modprobe v4l2loopback exclusive_caps=1 card_label="GPhoto2 Webcam"

%prep

cp %SOURCE1 .

%install
install -d                 %buildroot/usr/bin
install -c -m 755 %SOURCE0 %buildroot/usr/bin/gphoto2-webcam

%files
%defattr(-, root, root)
%license COPYING
%{_bindir}/gphoto2-webcam

%changelog
