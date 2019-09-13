#
# spec file for package psgplay
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           psgplay
BuildRequires:  automake
BuildRequires:  zlib-devel
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Players
Version:        0.6
Release:        0
Summary:        Player for Atari ST Music Files
Source:         psgplay-0.6.tar.gz
Patch:          psgplay-codecleanup.diff
Patch1:         psgplay-autotools.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package allows you to play music from Atari ST games and demos on
your PC.

You can find a comprehensive archive on the World Wide Web at
http://www.nocrew.org/software/psgplay/tunes/

%prep
%setup -q -n psgplay-0.6
%patch
%patch1
rm -f acconfig.h

%build
autoreconf -fi
export CFLAGS="$RPM_OPT_FLAGS -Wall"
./configure --prefix=/usr
make

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
/usr/bin/psgplay

%changelog
