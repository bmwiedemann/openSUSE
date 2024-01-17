#
# spec file for package qtilitools
#
# Copyright (c) 2023 SUSE LLC
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


Name:           qtilitools
Version:        0.1.2
Release:        0
Summary:        Scripts/commands used in the Qtilities organization
License:        BSD-3-Clause
URL:            https://github.com/qtilities/qtilitools
Source0:        https://github.com/qtilities/qtilitools/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildArch:      noarch

%description
Scripts/commands used in the Qtilities organization.

  - qtls-translate: shell script based on lxqt-transupdate plus some additions to update and compile translations.

  - AppStream.cmake: converts a given string to a freedesktop' desktop entry specification compliant name.

  - QtAppResources.cmake: configures and installs various application' resources, including translations.

  - Translate.cmake: modified version of LXQtTranslateTs.cmake merged with LXQtTranslateDesktop.cmake, to work also with Qt6.

  - TranslateDesktop.pl: Renamed LXQtTranslateDesktopYaml.pl used by Translate.cmake.


%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license COPYING
%{_bindir}/qtls-translate
%{_datadir}/cmake/%{name}

%changelog
