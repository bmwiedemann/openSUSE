#
# spec file for package recordmydesktop
#
# Copyright (c) 2021 SUSE LLC
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


Name:           recordmydesktop
Version:        0.4.0
Release:        0
Summary:        Desktop Recorder
License:        GPL-2.0
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://enselic.github.io/recordmydesktop/
Source:         https://github.com/Enselic/recordmydesktop/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  alsa-devel
BuildRequires:  jack-devel
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
recordMyDesktop is a program that captures audio and video data from a Linux
desktop session, producing an Ogg-encapsulated Theora-Vorbis file. The main
goal is to be as unobstrusive as possible by proccessing only regions of the
screen that have changed.

%prep
%setup -q

%build
%configure --enable-jack=yes
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/recordmydesktop
%{_mandir}/man1/recordmydesktop.1%{?ext_man}

%changelog
