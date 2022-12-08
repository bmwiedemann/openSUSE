#
# spec file for package kochmorse
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           kochmorse
Version:        3.5.1
Release:        0
Summary:        A simple morse tutor using the Koch method
License:        GPL-2.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://github.com/hmatuschek/kochmorse
#Git-Clone:     https://github.com/hmatuschek/kochmorse.git
Source:         https://github.com/hmatuschek/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         kochmorse-fix-desktop-file-and-iconpath.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
A simple morse tutor using the Koch method.

%prep
%setup -q
%patch0 -p1

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%doc ChangeLog README.md
%license LICENSE
%{_bindir}/kochmorse
%{_datadir}/applications/kochmorse.desktop
%{_datadir}/icons/hicolor/scalable/apps/kochmorse.svg

%changelog
