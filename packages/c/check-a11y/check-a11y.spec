#
# spec file for package check-a11y
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?suse_version} < 1550
%global gcc_version 13
%global gcc_suffix -13
%endif
Name:           check-a11y
Version:        0+1695734895.5fd723d
Release:        0
Summary:        Tool to check whether the accessibility stack is working
License:        BSD-2-Clause
Group:          System/X11/Utilities
URL:            https://salsa.debian.org/a11y-team/check-a11y
Source:         %{name}-%{version}.tar.gz
Patch0:         Fix-qt6.patch
Patch1:         Intall-target.patch
Patch2:         %{name}-java8.patch
BuildRequires:  at-spi2-atk-devel
BuildRequires:  dbus-1-devel
BuildRequires:  gtk-sharp2
BuildRequires:  gtk-sharp3
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtk4-devel
BuildRequires:  java-devel >= 1.8
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-devel
%if 0%{?gcc_version}
BuildRequires:  gcc%{gcc_version}-c++
%endif

%description
This allows to check whether the accessibility stack is going right in an X11 environment.

%prep
%autosetup
sed -i -E -e 's|#!/usr/bin/env ([a-z0-9]+)|#!/usr/bin/\1|' atspi-top show_py* troubleshoot

%build
CXX=g++%{?gcc_suffix} %make_build

%install
CXX=g++%{?gcc_suffix} %make_install
mkdir -p %{buildroot}%{_bindir}
ln -s %{_prefix}/lib/check-a11y/troubleshoot %{buildroot}%{_bindir}/a11y-troubleshoot

%files
%license COPYING-BSD
%doc README
%{_bindir}/a11y-troubleshoot
%dir %{_prefix}/lib/check-a11y
%{_prefix}/lib/check-a11y/atspi-top
%{_prefix}/lib/check-a11y/check
%{_prefix}/lib/check-a11y/look
%{_prefix}/lib/check-a11y/show_gtk2
%{_prefix}/lib/check-a11y/show_gtk3
%{_prefix}/lib/check-a11y/show_gtk4
%{_prefix}/lib/check-a11y/show_gtksharp2
%{_prefix}/lib/check-a11y/show_java.class
%{_prefix}/lib/check-a11y/show_pygtk2
%{_prefix}/lib/check-a11y/show_pygtk3
%{_prefix}/lib/check-a11y/show_pyqt4
%{_prefix}/lib/check-a11y/show_pyqt4msg
%{_prefix}/lib/check-a11y/show_pyqt5
%{_prefix}/lib/check-a11y/show_pyqt5msg
%{_prefix}/lib/check-a11y/show_qt5
%{_prefix}/lib/check-a11y/show_qt6
%{_prefix}/lib/check-a11y/show_winforms
%{_prefix}/lib/check-a11y/troubleshoot

%changelog
