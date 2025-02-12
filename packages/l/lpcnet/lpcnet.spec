#
# spec file for package lpcnet
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


%define sover 0_5
Name:           lpcnet
Version:        0.5
Release:        0
Summary:        Experimental Neural Net speech coding for FreeDV
License:        BSD-3-Clause
URL:            https://github.com/drowe67/LPCNet
Source:         https://github.com/drowe67/LPCNet/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        http://rowetel.com/downloads/deep/lpcnet_191005_v1.0.tgz
BuildRequires:  cmake
BuildRequires:  sox
%{?suse_build_hwcaps_libs}

%description
Experimental version of LPCNet that has been used to develop FreeDV 2020 - a HF
radio Digital Voice mode for over the air experimentation with Neural Net
speech coding. It includes a prebuilt model.

%package -n liblpcnetfreedv%{sover}
Summary:        Experimental Neural Net speech coding for FreeDV

%description -n liblpcnetfreedv%{sover}
Experimental version of LPCNet that has been used to develop FreeDV 2020 - a HF
radio Digital Voice mode for over the air experimentation with Neural Net
speech coding. It includes a prebuilt model.

This package contains the shared library.

%package devel
Summary:        Development files for lpcnet
Requires:       liblpcnetfreedv%{sover} = %{version}

%description devel
Experimental version of LPCNet that has been used to develop FreeDV 2020 - a HF
radio Digital Voice mode for over the air experimentation with Neural Net
speech coding. It includes a prebuilt model.

This package contains files needed for building with lpcnet.

%prep
%autosetup -p1 -n LPCNet-%{version}
mkdir build
cp %{SOURCE2} build/

%build
%cmake \
	-DCMAKE_SHARED_LINKER_FLAGS:STRING="-lm" \
	%{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n liblpcnetfreedv%{sover}

%files
%license COPYING
%doc README.md
%{_bindir}/lpcnet_enc
%{_bindir}/lpcnet_dec

%files -n liblpcnetfreedv%{sover}
%license COPYING
%{_libdir}/liblpcnetfreedv.so.*

%files devel
%license COPYING
%{_includedir}/lpcnet
%{_libdir}/cmake/lpcnetfreedv
%{_libdir}/liblpcnetfreedv.so

%changelog
