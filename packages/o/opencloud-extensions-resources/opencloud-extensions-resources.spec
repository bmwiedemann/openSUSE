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


Name:           opencloud-extensions-resources
Version:        1.0.0
Release:        0
Summary:        Resources for the OpenCloud client and desktop shell integrations
License:        GPL-2.0-or-later
URL:            https://github.com/opencloud-eu/desktop-shell-integration-resources
Source0:        https://github.com/opencloud-eu/desktop-shell-integration-resources/archive/v%{version}.tar.gz#/desktop-shell-integration-resources-%{version}.tar.gz
BuildRequires:  cmake >= 3.18
BuildRequires:  extra-cmake-modules

%description

This package provides resources like icons for the OpenCloud client and the shell integrations

%prep
%autosetup -p1 -n desktop-shell-integration-resources-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_libdir}/cmake/OpenCloudShellResources/
%{_datadir}/icons/*/*/*/*
%doc README.md
%license COPYING

%changelog

