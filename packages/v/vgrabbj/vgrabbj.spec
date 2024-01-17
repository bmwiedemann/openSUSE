#
# spec file for package vgrabbj
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           vgrabbj
Version:        0.9.9
Release:        0
Summary:        Image grabber for v4l devices
License:        GPL-2.0+
Group:          Hardware/Camera
Url:            https://sourceforge.net/projects/vgrabbj/
Source0:        http://sourceforge.net/projects/vgrabbj/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libv4l-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
vgrabbj is used to grab single images from a video4linux device (e.g. webcam)
and store it in a file (jpg/png).

%prep
%setup -q

%build
%configure
make

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root,-)
%{_mandir}/man1/vgrabbj.1.gz
%{_mandir}/man5/vgrabbj.conf.5.gz
%doc COPYING AUTHORS NEWS README THANKS TODO ChangeLog*
%{_bindir}/%{name}
%config /etc/vgrabbj.conf

%changelog
