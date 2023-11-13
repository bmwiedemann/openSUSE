#
# spec file for package mac
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


%define _version 1026
Name:           mac
Version:        10.26
Release:        0
Summary:        APE codec and decompressor
License:        BSD-3-Clause
URL:            https://www.monkeysaudio.com/
Source0:        https://monkeysaudio.com/files/MAC_%{_version}_SDK.zip
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  unzip

%description
Monkey’s Audio is a fast and easy way to compress digital music.

%package devel
Summary:        Development files for APE
Requires:       mac = %{version}

%description devel
Development files for Monkey's Audio codec and decompressor.

%prep
%setup -qc
tr -d '\r' <Readme.txt >README

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README
%license License.txt
%{_bindir}/mac
%{_libdir}/libMAC.so.10

%files devel
%{_includedir}/MAC
%{_libdir}/libMAC.so

%changelog
