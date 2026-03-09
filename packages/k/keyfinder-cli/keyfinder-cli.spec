#
# spec file for package libkeyfinder
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Ákos Szőts <akos+rpm@szots.dev>
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


Name:           keyfinder-cli
Version:        1.1.4
Release:        0
Summary:        Utility to estimate the musical key of many different audio file formats
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/EvanPurkhiser/keyfinder-cli
Source0:        https://github.com/evanpurkhiser/keyfinder-cli/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libkeyfinder)
BuildRequires:  pkgconfig(libswresample)

%description
keyfinder-cli is a utility to estimate the musical key of many different audio file formats.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/%{name}.1

%changelog
