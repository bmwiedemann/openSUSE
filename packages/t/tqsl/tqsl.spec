#
# spec file for package tqsl
#
# Copyright (c) 2017 Walter Fey DL8FCL
# Copyright (c) 2024 Wojciech Kazubski <wk@ire.pw.edu.pl>
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
#
# This file is under MIT license

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sover 2_5
Name:           tqsl
Version:        2.7.5
Release:        0
Summary:        TrustedQSL ham-radio applications
# https://spdx.org/licenses/TrustedQSL.html
License:        SUSE-Permissive
Group:          Productivity/Hamradio/Other
URL:            https://sourceforge.net/projects/trustedqsl/
Source:         https://www.arrl.org/tqsl/%{name}-%{version}.tar.gz
Patch0:         tqsl-tqsllib.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

%description
The TrustedQSL applications are used for generating digitally signed
QSO records (records of Amateur Radio contacts).

%package -n libtqsllib%{sover}
Summary:        TrustedQSL ham-radio library

%description -n libtqsllib%{sover}
The TrustedQSL applications are used for generating digitally signed
QSO records (records of Amateur Radio contacts).

This package contains the shared library.

%package devel
Summary:        The TrustedQSL Library development tools
Group:          Development/Libraries/Other
Requires:       libtqsllib%{sover} = %{version}

%description devel
Header files needed to build TrustedQSL applications.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang tqslapp

%check
%ctest

%ldconfig_scriptlets -n libtqsllib%{sover}

%files -f tqslapp.lang
%license LICENSE.txt
%{_bindir}/tqsl
%{_datadir}/TrustedQSL
%{_datadir}/applications/org.arrl.trustedqsl.desktop
%{_datadir}/pixmaps/TrustedQSL.png
%{_datadir}/icons/hicolor/*x*/apps/org.arrl.trustedqsl.png
%{_mandir}/man5/tqsl.5%{?ext_man}

%files -n libtqsllib%{sover}
%license LICENSE.txt
%{_libdir}/libtqsllib.so.*

%files devel
%license LICENSE.txt
%{_includedir}/*.h
%{_libdir}/libtqsllib.so

%changelog
