#
# spec file for package mpDris2
#
# Copyright (c) 2023 SUSE LLC
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


Name:           mpDris2
Version:        0.9.1
Release:        0
Summary:        MPRIS V2.1 support for mpd
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/eonpatapon/mpDris2
Source:         https://github.com/eonpatapon/mpDris2/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          interpreter.patch
BuildRequires:  autoconf
BuildRequires:  automake
# g-i-devel: This is for automatic GObject Introspection bindings dependency generation:
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  python3-base
Requires:       python3-python-mpd2
Recommends:     %{name}-lang
BuildArch:      noarch
%{perl_requires}

%description
mpDris2 provide MPRIS 2 support to mpd (Music Player Daemon). mpDris2 is
run in the user session and monitors a local or distant mpd server.

%lang_package

%prep
%setup -q
%patch -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%files
%doc %{_docdir}/%{name}
%{_sysconfdir}/xdg/autostart/mpdris2.desktop
%{_bindir}/mpDris2
%{_userunitdir}/mpDris2.service
%{_datadir}/applications/mpdris2.desktop
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/org.mpris.MediaPlayer2.mpd.service

%files lang -f %{name}.lang

%changelog
