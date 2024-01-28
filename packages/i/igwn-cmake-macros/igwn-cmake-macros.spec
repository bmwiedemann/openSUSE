#
# spec file for package igwn-cmake-macros
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


Name:           igwn-cmake-macros
Version:        1.5.0
Release:        0
Summary:        Collection of macros to help convert autotools based projects into CMake
License:        GPL-2.0-only
URL:            https://git.ligo.org/computing/ldastools/igwn-cmake
Source:         https://software.igwn.org/lscsoft/source/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildArch:      noarch

%description
IGWN cmake macros is a collection of macros and scripts that were developed to
aid in the process of converting Autotools based projects into CMake.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc ChangeLog README.md
%{_datadir}/igwn-cmake/
%{_datadir}/pkgconfig/*.pc

%changelog

