#
# spec file for package cutecom
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


Name:           cutecom
Version:        0.51.0
Release:        0
Summary:        A graphical serial terminal
License:        GPL-3.0-or-later
Group:          System/X11/Terminals
URL:            https://gitlab.com/cutecom/cutecom
Source:         %{name}-%{version}.tgz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-build-with-Qt-5.15.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5SerialPort)
BuildRequires:  cmake(Qt5Widgets)

%description
CuteCom is a graphical serial terminal, similar to minicom. It is
written using the Qt library.

It is aimed mainly at hardware developers or other people who need a
terminal to talk to their devices.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

install -Dpm 644 %{name}.1 \
  %{buildroot}/%{_mandir}/man1/%{name}.1
install -Dpm 644 distribution/openSUSE/cutecom.desktop \
  %{buildroot}%{_datadir}/applications/cutecom.desktop
install -Dpm 644 images/cutecom.svg \
  %{buildroot}%{_datadir}/pixmaps/cutecom.svg

%files
%license LICENSE
%doc Changelog TODO CREDITS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/cutecom.svg

%changelog
