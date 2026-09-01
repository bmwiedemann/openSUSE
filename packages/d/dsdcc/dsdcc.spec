#
# spec file for package dsdcc
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2017-2025, Martin Hauke <mardnh@gmx.de>
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


%define sover 1
Name:           dsdcc
Version:        1.9.6
Release:        0
Summary:        Digital Speech Decoder (DSD) rewritten as a C++ library
# Legal-Review-Notice: upstream ships no LICENSE file. 58 of 64 sources carry a box
# header truncated after "as version 3 of the License, or" - no later-version clause,
# and identical in v1.0.0, so it is upstream's wording rather than a reflow accident.
# Read as or-later: the same author's locator.{cpp,h} carry the clause in full and his
# in-tree debian/copyright declares GPL-3.0+. nxdnconvolution.{cpp,h} and
# nxdncrc.{cpp,h} are GPL-2.0-or-later (G4KLX), which GPL-3.0-or-later absorbs.
# NEEDS A RULING: descramble.cpp carries a second G4KLX notice reading "version 2 of
# the License." with no later clause (GPL-2.0-only), beneath F4EXB's own GPL-3 header
# relicensing his derivative. It is compiled into libdsdcc.
License:        GPL-3.0-or-later
URL:            https://github.com/f4exb/dsdcc
#Git-Clone:     https://github.com/f4exb/dsdcc.git
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
DSDcc is a complete rewrite of the original DSD (Digital Speech Decoder)
project. It decodes the DMR, dPMR, D-Star and Yaesu System Fusion (YSF)
standards.

This package contains the dsdccx command line decoder.

# both subpackages inherit License from the main package; spec-cleaner strips an
# explicit duplicate, so do not re-add it
%package -n libdsdcc%{sover}
Summary:        Digital Speech Decoder (DSD) rewritten as a C++ library

%description -n libdsdcc%{sover}
DSDcc is a complete rewrite of the original DSD (Digital Speech Decoder)
project. It decodes the DMR, dPMR, D-Star and Yaesu System Fusion (YSF)
standards.

This subpackage contains the shared library libdsdcc.

%package devel
Summary:        Development files for the dsdcc library
Requires:       libdsdcc%{sover} = %{version}

%description devel
DSDcc is a complete rewrite of the original DSD (Digital Speech Decoder)
project. It decodes the DMR, dPMR, D-Star and Yaesu System Fusion (YSF)
standards.

This subpackage contains libraries and header files for developing
applications that want to make use of libdsdcc.

%prep
%autosetup -p1

%build
# upstream hardcodes CMAKE_INSTALL_RPATH to <prefix>/lib and the cmake macro only
# strips it on suse_version <= 1500, leaving a bogus lib64-less RUNPATH on both ELFs
# mbelib is not in Factory: the AMBE/IMBE vocoder it implements is patent-encumbered
%cmake \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
  -DUSE_MBELIB=OFF
%cmake_build

%install
%cmake_install

# no test suite to wire up: testfec/ are print-only exercisers that all return 0

%ldconfig_scriptlets -n libdsdcc%{sover}

%files
%doc CHANGELOG messagefile.md Readme.md
%{_bindir}/dsdccx

%files -n libdsdcc%{sover}
%{_libdir}/libdsdcc.so.%{sover}
%{_libdir}/libdsdcc.so.%{sover}.*

%files devel
%{_includedir}/dsdcc
%{_libdir}/libdsdcc.so
%{_libdir}/pkgconfig/libdsdcc.pc

%changelog
