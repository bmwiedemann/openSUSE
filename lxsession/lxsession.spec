#
# spec file for package lxsession
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


Name:           lxsession
Version:        0.5.3
Release:        0
Summary:        LXDE Session Manager, required for running the desktop environment
License:        GPL-2.0
Group:          System/GUI/LXDE
Url:            http://www.lxde.org/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  dbus-1-glib-devel
BuildRequires:  docbook-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libgee-devel
BuildRequires:  libtool
BuildRequires:  libunique1-devel
BuildRequires:  libxslt
BuildRequires:  pkg-config
BuildRequires:  polkit-devel
BuildRequires:  vala >= 0.16
Obsoletes:      lxsession-edit <= 0.2.0
Obsoletes:      lxpolkit <= 0.1.0
Provides:       lxsession-edit > 0.2.0
Provides:       lxpolkit > 0.1.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
make %{?_smp_mflags} V=1

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
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog README COPYING TODO
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
%{_mandir}/man1/*.1.gz
%{_sysconfdir}/xdg/autostart/lxpolkit.desktop
%dir /usr/lib/lxsession
/usr/lib/lxsession/lxsession-xsettings

%changelog
