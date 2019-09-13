#
# spec file for package sni-qt
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sni-qt
Version:        0.2.6
Release:        0
Summary:        Library that turns Qt tray icons into appindicators
License:        LGPL-3.0
Group:          System/Libraries
Url:            https://launchpad.net/sni-qt
Source:         https://launchpad.net/%{name}/trunk/0.2.6/+download/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Source2:        sni-qt.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kde4-filesystem
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(dbusmenu-qt)
Supplements:    packageand(plasma5-workspace:libqt4)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains a Qt plugin which turns all QSystemTrayIcon into
StatusNotifierItems (appindicators).


%prep
%setup -q

%build
  %cmake_kde4 -d build
  %make_jobs

%install
  %kde4_makeinstall -C build
  install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/settings/sni-qt.conf

%files
%defattr(-,root,root)
%doc NEWS README COPYING* LGPL*
%dir %{_kde4_libdir}/qt4/plugins/systemtrayicon/
%{_kde4_libdir}/qt4/plugins/systemtrayicon/libsni-qt.so
%dir %{_sysconfdir}/settings
%{_sysconfdir}/settings/sni-qt.conf

%changelog
