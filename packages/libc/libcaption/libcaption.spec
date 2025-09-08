#
# spec file for package libcaption
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           libcaption
Version:        0.8
Release:        0
Summary:        CEA608 / CEA708 closed-caption encoder/decoder
License:        MIT
URL:            https://github.com/szatmary/libcaption
Source:         https://github.com/szatmary/libcaption/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake

%description
libcaption is a library written in C to aid in the creating and parsing of
closed caption data, open sourced under the MIT license to use within community
developed broadcast tools.

%package devel
Summary:        CEA608 / CEA708 closed-caption encoder/decoder
Requires:       %{name} = %{version}

%description devel
libcaption is a library written in C to aid in the creating and parsing of
closed caption data, open sourced under the MIT license to use within community
developed broadcast tools.

This package contains the files requires for building with %{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# rollup package ships a binary of the name
mv %{buildroot}%{_bindir}/{,libcaption-}rollup

%check
%ctest

%files
%license LICENSE.txt
/usr/bin/flv+scc
%{_bindir}/flv2srt
%{_bindir}/flv+srt
%{_bindir}/libcaption-rollup
%{_bindir}/party
%{_bindir}/scc2srt
%{_bindir}/scc2vtt
%{_bindir}/sccdump
%{_bindir}/srt2vtt
%{_bindir}/srtdump
%{_bindir}/ts2srt
%{_bindir}/vttdump
%{_bindir}/vttsegmenter
%{_prefix}/lib/libcaption.so

%files devel
%license LICENSE.txt
%{_includedir}/caption

%changelog
