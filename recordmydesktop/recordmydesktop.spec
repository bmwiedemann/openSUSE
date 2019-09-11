#
# spec file for package recordmydesktop
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
Version:        0.3.8.1
Release:        0
Summary:        Desktop Recorder
License:        GPL-2.0
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://recordmydesktop.sourceforge.net
Source:         %{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE add x11 includes (>= 11.3 only)
Patch0:         recordmydesktop-x11-includes.patch
# PATCH-FIX-OPENSUSE add gcc includes
Patch1:         recordmydesktop-gcc-includes.patch
# PATCH-FIX-UPSTREAM recordmydesktop-sane-theora-defaults.patch rh#525155 dimstar@opensuse.org -- Use sane default values for Theora encoder
Patch2:         recordmydesktop-sane-theora-defaults.patch
BuildRequires:  alsa-devel
BuildRequires:  jack-devel
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(ice)
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
%if 0%{?suse_version} >= 1130
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1

%build
%configure --enable-jack=yes
make %{?_smp_mflags}

%install
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/recordmydesktop
%doc %{_mandir}/man1/recordmydesktop.1*

%changelog
