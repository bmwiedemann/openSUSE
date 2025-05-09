#
# spec file for package deepin-calculator
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


%define gtest_version %(rpm -q --queryformat '%%{VERSION}' gtest)

Name:           deepin-calculator
Version:        5.7.21
Release:        0
Summary:        The Deepin Calculator Application
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/linuxdeepin/deepin-calculator
Source:         https://github.com/linuxdeepin/deepin-calculator/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM do-not-hardcode-c++-version.patch hillwood@opensuse.org
Patch0:         do-not-hardcode-c++-version.patch
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
BuildRequires:  fdupes
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(dtkwidget)
Recommends:     %{name}-lang

%description
Deepin calculator is an easy to use calculator for ordinary users.

%lang_package

%prep
%autosetup -p1
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh

%build
%cmake \
%if "%{gtest_version}" >= "1.14.0"
       -DCMAKE_CXX_STANDARD=14
%endif

%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/deepin-manual/manual-assets/application/%{name}

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
