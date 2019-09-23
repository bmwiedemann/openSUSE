#
# spec file for package quassel
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


%define realver 0.13.1
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           quassel
Version:        0.13.1
Release:        0
Summary:        Distributed IRC client
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Productivity/Networking/IRC
URL:            http://quassel-irc.org/
Source:         http://%{name}-irc.org/pub/%{name}-%{realver}.tar.bz2
Source1:        service.%{name}core
Source2:        sysconfig.%{name}core
Source3:        logrotate.%{name}core
Source5:        quassel-rpmlintrc
# PATCH-FIX-SUSE: Set the correct libraries and compiler flags in order to use qglobal.h in check_cxx_source_compiles function
Patch0:         quassel-set-required-libs-and-flags.patch
BuildRequires:  cmake >= 2.8.10
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  hicolor-icon-theme
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kf5-filesystem
BuildRequires:  knotifications-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  snorenotify-qt5-devel >= 0.7
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(qca2-qt5)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
%{?systemd_requires}

%description
Quassel IRC is a distributed IRC client, meaning that one (or
multiple) client(s) can attach to and detach from a central core --
much like the combination of GNU Screen and a text-based IRC client
such as WeeChat, but graphical.

%package mono
Summary:        Standalone client for the Quassel IRC client
Group:          Productivity/Networking/IRC
Requires:       %{name}-base = %{version}
Requires:       libqt5_sql_backend
Recommends:     libQt5Sql5-sqlite
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
Provides:       %{name}_ui = %{version}

%description mono
Quassel IRC is a distributed IRC client, meaning that one (or
multiple) client(s) can attach to and detach from a central core --
much like the combination of GNU Screen and a text-based IRC client
such as WeeChat, but graphical.

This is the quassel standalone client.

%package client
Summary:        KDE client for the Quassel IRC client
Group:          Productivity/Networking/IRC
Requires:       %{name}-base = %{version}
Provides:       %{name}_ui = %{version}

%description client
Quassel IRC is a distributed IRC client, meaning that one (or
multiple) client(s) can attach to and detach from a central core --
much like the combination of GNU Screen and a text-based IRC client
such as WeeChat, but graphical.

This is the quassel KDE client only.

%package client-qt5
Summary:        Qt5 client for the Quassel IRC client
Group:          Productivity/Networking/IRC
Requires:       %{name}-base = %{version}
Provides:       %{name}_ui = %{version}

%description client-qt5
Quassel IRC is a distributed IRC client, meaning that one (or
multiple) client(s) can attach to and detach from a central core --
much like the combination of GNU Screen and a text-based IRC client
such as WeeChat, but graphical.

This is the quassel Qt5 client only

%package core
Summary:        Core program for the Quassel IRC client
Group:          Productivity/Networking/IRC
Requires:       libqt5_sql_backend
Requires:       logrotate
Requires(pre):  %fillup_prereq
Requires(pre):  shadow
Recommends:     libqt5-sql-sqlite

%description core
Quassel IRC is a distributed IRC client, meaning that one (or
multiple) client(s) can attach to and detach from a central core --
much like the combination of GNU Screen and a text-based IRC client
such as WeeChat, but graphical.

This is the core only.

%package base
Summary:        Base files for the Quassel IRC client
Group:          Productivity/Networking/IRC
Requires:       %{name}_ui = %{version}

%description base
Quassel IRC is a distributed IRC client, meaning that one (or
multiple) client(s) can attach to and detach from a central core --
much like the combination of GNU Screen and a text-based IRC client
such as WeeChat, but graphical.

This contains common parts shared by %{name} and %{name}-client.

%prep
%setup -q -n %{name}-%{realver}
%patch0 -p1

%build
FAKE_BUILDDATE=$(LC_ALL=C date -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/common/quassel.cpp
FAKE_BUILDTIME=$(LC_ALL=C date -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i "s/__TIME__/\"$FAKE_BUILDTIME\"/" src/common/quassel.cpp

%cmake_kf5 -d build -- -DUSE_QT5=ON -DWITH_WEBENGINE=ON -DWITH_KDE=ON
make %{?_smp_mflags}
cd ..
%cmake_kf5 -d build-qt5 -- -DUSE_QT5=ON -DWITH_WEBENGINE=ON -DWITH_KDE=OFF
make %{?_smp_mflags}

%install
%kf5_makeinstall -C build

# Allow client qt5/kde co-install
mv %{buildroot}%{_bindir}/quasselclient %{buildroot}%{_bindir}/quasselclient-kde
install build-qt5/quasselclient %{buildroot}%{_bindir}/quasselclient-qt5
# Alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/quasselclient
ln -sf %{_sysconfdir}/alternatives/quasselclient %{buildroot}%{_bindir}/quasselclient

%fdupes %{buildroot}/%{_prefix}
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}core
install -d -m 755 %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/quasselcore.service
# Provide SUSE policy symlink /usr/sbin/rcFOO -> service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcquasselcore
install -D -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.quasselcore
install -d -m 751 %{buildroot}%{_localstatedir}/log/%{name}
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}core

# rewrite env shebang on scripts to normal shebang
sed -i '1{
    s,^#!%{_bindir}/env  *bash *$,#!/bin/bash,
    s,^#!%{_bindir}/env  *\([^ ]*\) *$,#!%{_bindir}/\1,
}' %{buildroot}%{_datadir}/%{name}/scripts/*

%pre core
%{_bindir}/getent group %{name}core >/dev/null || %{_sbindir}/groupadd -r %{name}core
%{_bindir}/getent passwd %{name}core >/dev/null || %{_sbindir}/useradd -r -d %{_localstatedir}/lib/%{name}core \
    -s /bin/false -c "%{name}core daemon" -g %{name}core %{name}core
%service_add_pre quasselcore.service

%post core
%{fillup_only -n quasselcore}
%service_add_post quasselcore.service

%preun core
%service_del_preun quasselcore.service

%postun core
%service_del_postun quasselcore.service

%if 0%{?suse_version} < 1500
%post base
%icon_theme_cache_post

%postun base
%icon_theme_cache_postun
%endif

%post client
update-alternatives --install %{_bindir}/quasselclient quasselclient %{_bindir}/quasselclient-kde 20

%postun client
if [ $1 -eq 0 ] ; then
    update-alternatives --remove quasselclient %{_bindir}/quasselclient-kde
fi

%post client-qt5
update-alternatives --install %{_bindir}/quasselclient quasselclient %{_bindir}/quasselclient-qt5 10

%postun client-qt5
if [ $1 -eq 0 ] ; then
    update-alternatives --remove quasselclient %{_bindir}/quasselclient-qt5
fi

%files mono
%doc AUTHORS ChangeLog README.md
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}

%files client
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}client-kde
%ghost %{_sysconfdir}/alternatives/quasselclient
%{_bindir}/%{name}client

%files client-qt5
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}client-qt5
%ghost %{_sysconfdir}/alternatives/quasselclient
%{_bindir}/%{name}client

%files core
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}core
%{_sbindir}/rc%{name}core
%{_unitdir}/%{name}core.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}core
%attr(-,%{name}core,%{name}core) %dir %{_localstatedir}/lib/%{name}core
%attr(-,%{name}core,%{name}core) %dir %{_localstatedir}/log/%{name}
%{_fillupdir}/sysconfig.%{name}core

%files base
%license COPYING
%{_datadir}/applications/%{name}client.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/knotifications5/%{name}.notifyrc

%changelog
