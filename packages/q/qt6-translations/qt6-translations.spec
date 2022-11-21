#
# spec file for package qt6-translations
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


%define real_version 6.4.1
%define short_version 6.4
%define tar_name qttranslations-everywhere-src
%define tar_suffix %{nil}
#
Name:           qt6-translations
Version:        6.4.1
Release:        0
Summary:        Qt 6 Translations
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  fdupes
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools) >= %{real_version}
BuildArch:      noarch

%description
Translations for Qt6 libraries and tools.

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%fdupes %{buildroot}%{_qt6_translationsdir}

%files
%license LICENSES/*
%{_qt6_translationsdir}/*

%changelog
