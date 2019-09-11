#
# spec file for package vkeybd
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           vkeybd
Version:        0.1.18d
Release:        0
Summary:        Virtual Keyboard Instrument
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            http://www.alsa-project.org/~iwai/alsa.html
Source:         ftp://ftp.suse.com/pub/people/tiwai/vkeybd/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(tk)

%description
Vkeybd is a virtual keyboard (as in musical instrument) for AWE32/64,
raw MIDI, and ALSA sequencer drivers.  It is written in Tcl/Tk.  Enjoy
playing music with your "computer" keyboard.

%prep
%setup -q -n %{name}

%build
TCL_VERSION=$(echo 'puts $tcl_version' | tclsh)
make COPTFLAGS="%{optflags}" \
	PREFIX=%{_prefix} \
	TCL_VERSION=$TCL_VERSION \
	USE_LASH=0 \
	XLIB=""

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install
make DESTDIR=%{buildroot} MAN_DIR=%{_mandir} install-man
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install-desktop
ln -sf vkeybd_48x48.png %{buildroot}%{_datadir}/pixmaps/
%suse_update_desktop_file vkeybd AudioVideo Music

%files
%{_bindir}/*
%{_datadir}/vkeybd
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_mandir}/man*/*
%doc README ChangeLog

%changelog
