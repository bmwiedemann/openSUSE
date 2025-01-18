#
# spec file for package codec2
#
# Copyright (c) 2025 SUSE LLC
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


%define libname lib%{name}-1_2
Name:           codec2
Version:        1.2.0
Release:        0
Summary:        Low bit rate speech codec
# octave/plot_fsk_demod_stats.py is GPL-3.0-or-later, unused
License:        LGPL-2.1-only
URL:            https://rowetel.com/codec2.html
Source:         https://github.com/drowe67/codec2/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch0:         codec2-1.2.0-install-binaries.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.13
BuildRequires:  pkgconfig
%{?suse_build_hwcaps_libs}

%description
Codec 2 is a speech codec designed for communications quality speech
between 700 and 3200 bit/s.

%package -n %{libname}
Summary:        Low bit rate speech codec

%description -n %{libname}
Codec 2 is a speech codec designed for communications quality speech
between 700 and 3200 bit/s.

%package devel
Summary:        Development library for codec2
Requires:       %{libname} = %{version}

%description devel
Codec 2 is a speech codec designed for communications quality speech
between 700 and 3200 bit/s.

%package examples
Summary:        Example code for Codec 2
Group:          Productivity/Hamradio/Other
BuildArch:      noarch

%description examples
Example code for Codec 2, including test voices and matlab/octave files.

%prep
%autosetup -p1
rm -rf octave/

%build
%cmake \
  -DUNITTEST=FALSE
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -rv raw wav %{buildroot}%{_datadir}/%{name}/

%ldconfig_scriptlets -n %{libname}

%files
%license COPYING
%{_bindir}/*

%files -n %{libname}
%license COPYING
%doc README*
%{_libdir}/libcodec2.so.*

%files devel
%license COPYING
%{_includedir}/*
%dir %{_libdir}/cmake/codec2
%{_libdir}/cmake/codec2/codec2-config-relwithdebinfo.cmake
%{_libdir}/cmake/codec2/codec2-config.cmake
%{_libdir}/libcodec2.so
%{_libdir}/pkgconfig/%{name}.pc

%files examples
%license COPYING
%{_datadir}/%{name}

%changelog
