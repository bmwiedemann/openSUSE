#
# spec file for package aseqview
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


Name:           aseqview
BuildRequires:  alsa-devel
BuildRequires:  automake
BuildRequires:  gtk2-devel
BuildRequires:  update-desktop-files
Summary:        ALSA Sequencer Event Viewer
License:        GPL-2.0-only
Version:        0.2.8
Release:        0
Source:         %{name}-%{version}.tar.xz
Source1:        aseqview.desktop
Source2:        aseqview.png
Patch0:         aseqview-0.2.2.dif
Patch1:         aseqview-quote-macros.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://www.alsa-project.org/~iwai/alsa.html

%description
ASeqView is an ALSA sequencer user client that works as an event viewer
and event filter.  It visualizes received events, such as note on and
off, controls, and pitch wheels, using bar graphs as seen in many
sequencer applications.

%prep
%setup
%patch0
%patch1 -p1

%build
autoreconf --force --install
%configure --enable-gtk2
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
%suse_update_desktop_file -i aseqview AudioVideo Music GTK
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%files
%defattr(-,root,root)
%{_bindir}/*
%doc README AUTHORS ChangeLog
%doc %{_mandir}/man*/*
%if %suse_version > 820
%{_datadir}/applications/*.desktop
%endif
%{_datadir}/pixmaps/*.png

%changelog
