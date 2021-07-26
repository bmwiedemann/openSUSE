#
# spec file for package grfcodec
#
# Copyright (c) 2021 SUSE LLC
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


Name:           grfcodec
Version:        6.0.6+39
Release:        0
Summary:        A suite of programs to modify Transport Tycoon Deluxe's GRF files
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/OpenTTD/grfcodec
Source:         %{name}-%{version}.tar.xz
Patch0:         grfcodec-cmake-install.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel >= 1.36
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libpng-devel
Provides:       nforenum = %{version}
Obsoletes:      nforenum < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.
Contains GRFCodec for encoding and decoding the actual GRF files,
GRFDiff and GRFMerge for making and applying patches for GRF files,
GRFID for extracting the (unique) NewGRF identifier and NFORenum,
a format correcter and linter for the NFO language. NFO and PCX
or PNG files are encoded to form GRF files.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root,-)
%{_bindir}/grfcodec
%{_bindir}/grfid
%{_bindir}/grfstrip
%{_bindir}/nforenum

%changelog
