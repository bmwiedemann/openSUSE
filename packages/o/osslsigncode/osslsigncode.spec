#
# spec file for package osslsigncode
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


Name:           osslsigncode
Version:        2.7
Release:        0
Summary:        Platform-independent tool for Authenticode signing of EXE/CAB files
License:        GPL-3.0-only
Group:          Productivity/Security
URL:            https://github.com/mtrojnar/osslsigncode
Source0:        https://github.com/mtrojnar/osslsigncode/archive/%{version}/osslsigncode-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto) >= 1.1
BuildRequires:  pkgconfig(libcurl)

%description
osslsigncode is a small utility for placing signatures on Microsoft cabinate
files and executables.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING.txt LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}.bash

%changelog
