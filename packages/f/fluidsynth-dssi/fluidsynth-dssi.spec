#
# spec file for package fluidsynth-dssi
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _rev 3a9b7f16ce00a069decd9e4b6efbe31389fefd6d
Name:           fluidsynth-dssi
Version:        1.9.9+git13012019
Release:        0
Summary:        Fluidsynth Plug-In for Disposable Soft Synth Interface
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
Url:            http://dssi.sf.net
Source:         https://github.com/schnitzeltony/%{name}/archive/%{_rev}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fluidsynth-dssi-add-closedir.diff
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gail)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)

%description
FluidSynth-DSSI is the plug-in implementation of fluidsynth on DSSI
(Disposable Soft Synth Interface) with a GTK+ GUI.

%prep
%setup -q -n %{name}-%{_rev}
%autopatch -p1

%build
autoreconf --force --install
CFLAGS="%{optflags} -fno-strict-aliasing" \
%configure --with-gtk2
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/dssi
%doc README ChangeLog TODO
%license COPYING

%changelog
