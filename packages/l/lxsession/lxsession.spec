#
# spec file for package lxsession
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


Name:           lxsession
Version:        0.5.5
Release:        0
Summary:        LXDE Session Manager, required for running the desktop environment
License:        GPL-2.0-only
Group:          System/GUI/LXDE
URL:            http://www.lxde.org/
Source0:        https://sourceforge.net/projects/lxde/files/LXSession%20%28session%20manager%29/LXSession%200.5.x/%{name}-%{version}.tar.xz
BuildRequires:  dbus-1-glib-devel
BuildRequires:  docbook-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libgee-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
BuildRequires:  vala >= 0.16
Obsoletes:      lxpolkit <= 0.1.0
Obsoletes:      lxsession-edit <= 0.2.0
Provides:       lxpolkit > 0.1.0
Provides:       lxsession-edit > 0.2.0

%description
LXSession is the standard session manager used by LXDE. The LXSession manager
is used to automatically start a set of applications and set up a working desktop
environment. Moreover, the session manager is able to remember the applications in
use when a user logs out and to restart them the next time the user logs in.

%prep
%setup -q

%build
%configure \
	--enable-man
%make_build

%install
%make_install
%find_lang %{name}

# fix icon problems
# no such icon lxsession-default-apps
sed -i "3d" %{buildroot}%{_datadir}/applications/lxsession-default-apps.desktop
# why lxde use xfwm4 icon ?
sed -i "3d" %{buildroot}%{_datadir}/applications/lxsession-edit.desktop

%fdupes %{buildroot}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_bindir}/lxlock
%{_bindir}/lxsession
%{_bindir}/lxsession-logout
%{_bindir}/lxclipboard
%{_bindir}/lxpolkit
%{_bindir}/lxsession-default
%{_bindir}/lxsession-default-apps
%{_bindir}/lxsession-default-terminal
%{_bindir}/lxsession-xdg-autostart
%{_bindir}/lxsession-edit
%{_bindir}/lxsession-db
%{_bindir}/lxsettings-daemon
%{_datadir}/lxsession/
%{_datadir}/applications/lxsession-default-apps.desktop
%{_datadir}/applications/lxsession-edit.desktop
%{_mandir}/man1/*.1%{?ext_man}
%{_sysconfdir}/xdg/autostart/lxpolkit.desktop
%dir %{_libexecdir}/lxsession
%{_libexecdir}/lxsession/lxsession-xsettings

%changelog
