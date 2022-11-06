#
# spec file for package lxqt-session
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


Name:           lxqt-session
Version:        1.2.0
Release:        0
Summary:        LXQt Session Manager
License:        LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
# FIX-OPENSUSE mvetter@suse.com bsc#1099800
Patch0:         lxqt-0.13.0-xdg-config-dir.patch
# mvetter@suse.com bsc#1127043 - Use Openbox as default WM
Patch1:         lxqt-session-default_wm.patch
BuildRequires:  cmake >= 3.0.2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools-devel >= 0.11.0
BuildRequires:  pkgconfig
BuildRequires:  qtxdg-tools
BuildRequires:  xdg-user-dirs
BuildRequires:  cmake(KF5WindowSystem) >= 5.36.0
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.15
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(lxqt) >= 1.1.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
Requires(post): update-alternatives
Requires(postun):update-alternatives
Requires:       qtxdg-tools
Recommends:     %{name}-lang
Obsoletes:      lxqt-common <= 0.12.0
Obsoletes:      lxqt-l10n <= 0.12.0

%description
lxqt-session is the standard session manager used by LXQt. The lxqt-session manager
is used to automatically start a set of applications and set up a working desktop
environment. Moreover, the session manager is able to remember the applications in
use when a user logs out and to restart them the next time the user logs in.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
# Changing LXQt into X-LXQt in desktop files to be freedesktop compliant and shut rpmlint warnings
#find -name '*desktop.in*' -exec sed -ri 's/(LXQt;)/X-\1/' {} +

%build
%cmake -DPULL_TRANSLATIONS=No

%install
%cmake_install
%fdupes %{buildroot}/%{_datadir}

# for default-xsession
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%find_lang %{name} --with-qt

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/lxqt.desktop 20

%postun
[ -f %{_datadir}/xsessions/lxqt.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/lxqt.desktop

%files
%license LICENSE
%doc AUTHORS
%{_bindir}/lxqt-config-session
%{_bindir}/lxqt-session
%{_bindir}/lxqt-leave
%{_datadir}/applications/*.desktop
%{_mandir}/man?/lxqt-*%{ext_man}
%config %{_sysconfdir}/xdg/autostart/lxqt-xscreensaver-autostart.desktop
%{_bindir}/startlxqt
%{_mandir}/man1/startlxqt.1%{?ext_man}
%{_datadir}/xsessions/lxqt.desktop
%{_datadir}/lxqt/lxqt.conf
%{_datadir}/lxqt/session.conf
%{_datadir}/lxqt/windowmanagers.conf

# for default-xsession
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%ghost %{_sysconfdir}/alternatives/default.desktop
%{_datadir}/xsessions/*.desktop

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%{_datadir}/lxqt/translations/lxqt-config-session
%{_datadir}/lxqt/translations/lxqt-leave
%{_datadir}/lxqt/translations/lxqt-session

%changelog
