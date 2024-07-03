#
# spec file for package aseqview
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           aseqview
Version:        0.2.8
Release:        0
Summary:        ALSA Sequencer Event Viewer
License:        GPL-2.0-only
URL:            https://github.com/tiwai/aseqview
Source:         %{name}-%{version}.tar.xz
Source1:        aseqview.desktop
Source2:        aseqview.png
Patch0:         aseqview-0.2.2.dif
Patch1:         aseqview-quote-macros.patch
Patch2:         aseqview-piano-segfault-fix.patch
BuildRequires:  alsa-devel
BuildRequires:  automake
BuildRequires:  gtk2-devel
BuildRequires:  update-desktop-files

%description
ASeqView is an ALSA sequencer user client that works as an event viewer
and event filter.  It visualizes received events, such as note on and
off, controls, and pitch wheels, using bar graphs as seen in many
sequencer applications.

%prep
%setup -q
%patch -P 0
%patch -P 1 -p1
%patch -P 2 -p1

%build
autoreconf --force --install
%configure --enable-gtk2
%make_build

%install
%make_install
%suse_update_desktop_file -i aseqview AudioVideo Music GTK
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps

%files
%{_bindir}/*
%license COPYING
%doc README AUTHORS ChangeLog
%{_mandir}/man*/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
