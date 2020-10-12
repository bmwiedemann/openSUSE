#
# spec file for package gphoto
#
# Copyright (c) 2020 SUSE LLC
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


Name:           gphoto
BuildRequires:  cdk-devel
BuildRequires:  libgphoto2-devel >= 2.5.17
BuildRequires:  libjpeg-devel
BuildRequires:  pkg-config
BuildRequires:  popt-devel
BuildRequires:  readline-devel
URL:            http://gphoto.sourceforge.net
Summary:        A Digital Camera Utility
License:        GPL-2.0-or-later
Group:          Hardware/Camera
Version:        2.5.26
Release:        0
Source0:        https://downloads.sourceforge.net/project/gphoto/gphoto/%{version}/%{name}2-%{version}.tar.bz2
Source1:        https://downloads.sourceforge.net/project/gphoto/gphoto/%{version}/%{name}2-%{version}.tar.bz2.asc
Source2:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
gPhoto (GNU Photo) is a command line tool for previewing, retrieving,
and capturing images from a range of supported digital cameras to your
local hard drive. It does not support digital cameras based on the USB
storage protocol, because those can be mounted by Linux directly. Find
the list of supported cameras at the following URL:

http://gphoto.org/proj/libgphoto2/support.php

or by running

gphoto2 --list-cameras

%prep
%setup -q -n gphoto2-%{version}

%build
pkg-config --libs libgphoto2
export CFLAGS="$RPM_OPT_FLAGS -fPIE"
export LDFLAGS="-pie"
%configure	\
  --with-cdk-prefix=/usr		\
  --with-doc-dir=%{_defaultdocdir}/%{name}
make

%check
make check

%install
make DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}
mv $RPM_BUILD_ROOT/usr/share/doc/gphoto2/* $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}
%find_lang %{name}2

%files -f %{name}2.lang
%defattr(-,root,root)
%{_defaultdocdir}/%{name}
%{_prefix}/bin/gphoto2
%{_mandir}/man1/gphoto2.1*

%changelog
