#
# spec file for package grfcodec
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        6.2.0
Release:        0
Summary:        A suite of programs to modify Transport Tycoon Deluxe's GRF files
License:        GPL-2.0-or-later
URL:            https://github.com/OpenTTD/grfcodec
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.17
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libpng-devel
Provides:       nforenum = %{version}
Obsoletes:      nforenum < %{version}

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
%license COPYING
%doc %{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/COPYING
%{_bindir}/grfcodec
%{_bindir}/grfid
%{_bindir}/grfstrip
%{_bindir}/nforenum
%{_mandir}/man1/grfcodec.1%{?ext_man}
%{_mandir}/man1/grfid.1%{?ext_man}
%{_mandir}/man1/grfstrip.1%{?ext_man}
%{_mandir}/man1/nforenum.1%{?ext_man}

%changelog
