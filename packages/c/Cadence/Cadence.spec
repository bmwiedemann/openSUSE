#
# spec file for package Cadence
#
# Copyright (c) 2022 SUSE LLC
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


Name:           Cadence
Version:        0.9.2
Release:        0
Summary:        A JACK Audio Toolbox
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://kx.studio/Applications:Cadence
Source:         https://github.com/falkTX/Cadence/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  alsa-devel
BuildRequires:  dbus-1-python3-devel
BuildRequires:  libjack-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       a2jmidid
Requires:       dbus-1-python3
Requires:       jack_capture
Requires:       ladish
Requires:       python3-qt5
Recommends:     zita-a2jbridge

%description
Cadence is a set of tools useful for audio production.
Cadence itself is also an application (the main one).
There are other applications that are part of the Cadence suite,
they are usually named as the "Cadence tools".
They are:

    Catarina
    Catia
    Claudia

Some of these also have sub-tools, such as Cadence-JackMeter and Claudia-Launcher.

%prep
%setup -q -n Cadence-%{version}

%build
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"
%if 0%{?suse_version}
#sed -i 's:pyuic4:py3uic4:' Makefile
sed -i 's:wildcard /:wildcard $(DESTDIR)/:' Makefile
%endif
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d
make install DESTDIR=%{buildroot} PREFIX="%{_prefix}"
%if 0%{?suse_version}
 %suse_update_desktop_file -r cadence AudioVideo Music
 %suse_update_desktop_file -r catarina AudioVideo Music
 %suse_update_desktop_file -r catia AudioVideo Music
 %suse_update_desktop_file -r claudia AudioVideo Music
 %suse_update_desktop_file -r claudia-launcher AudioVideo Music
%endif

%files
%license COPYING
%doc TODO INSTALL.md README.md
%{_bindir}/*
%{_sysconfdir}/xdg/autostart/cadence-session-start.desktop
%if 0%{?suse_version}
%dir %{_sysconfdir}/X11/xinit
%dir %{_sysconfdir}/X11/xinit/xinitrc.d
%{_sysconfdir}/X11/xinit/xinitrc.d/*
%endif

%if %{defined fedora}
%dir %{_sysconfdir}/X11/Xsession.d
%{_sysconfdir}/X11/Xsession.d/*
%endif

%dir %{_datadir}/cadence
%{_datadir}/cadence/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/

%changelog
