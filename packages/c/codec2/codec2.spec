#
# spec file for package codec2
#
# Copyright (c) 2022 SUSE LLC
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


%define libname lib%{name}-1_0
Name:           codec2
Version:        1.0.5
Release:        0
Summary:        Low bit rate speech codec
# octave and asterisk directories contain GPL-2.0 licensed code but its not
# used build, only used in examples subpackage.
License:        LGPL-2.1-only
Group:          Productivity/Hamradio/Other
URL:            https://rowetel.com/codec2.html
Source:         https://github.com/drowe67/codec2/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source2:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(speexdsp)

%description
Codec 2 is a speech codec designed for communications quality speech
between 700 and 3200 bit/s.

%package -n %{libname}
Summary:        Low bit rate speech codec
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n %{libname}
Codec 2 is a speech codec designed for communications quality speech
between 700 and 3200 bit/s.

%package devel
Summary:        Development library for codec2
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Codec 2 is a speech codec designed for communications quality speech
between 700 and 3200 bit/s.

%package examples
Summary:        Example code for Codec 2
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Productivity/Hamradio/Other
Requires:       %{name}-devel = %{version}
BuildArch:      noarch

%description examples
Example code for Codec 2, including test voices and matlab/octave files.

%prep
%autosetup

%build
%cmake \
  -DINSTALL_EXAMPLES=TRUE \
  -DUNITTEST=FALSE
%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc README*
%{_libdir}/libcodec2.so.*

%files devel
%{_includedir}/*
%dir %{_libdir}/cmake/codec2
%{_libdir}/cmake/codec2/codec2-config-relwithdebinfo.cmake
%{_libdir}/cmake/codec2/codec2-config.cmake
%{_libdir}/libcodec2.so
%{_libdir}/pkgconfig/%{name}.pc

%files examples
%{_datadir}/%{name}/

%changelog
