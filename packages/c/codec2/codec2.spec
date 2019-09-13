#
# spec file for package codec2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libname lib%{name}-0_8
Name:           codec2
Version:        0.8.1
Release:        0
Summary:        Low bit rate speech codec
# octave and asterisk directories contain GPL-2.0 licensed code but its not
# used build, only used in examples subpackage.
License:        LGPL-2.1-only
Group:          Productivity/Hamradio/Other
URL:            http://rowetel.com/codec2.html
Source:         https://hobbes1069.fedorapeople.org/freetel/codec2/codec2-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Source2:        baselibs.conf
Patch0:         codec2-no_return_random.patch
Patch1:         codec2-licensed-stuff.patch
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
%setup -q
%patch0 -p1
%patch1 -p0

%build
%cmake \
  -DINSTALL_EXAMPLES=TRUE \
  -DUNITTEST=TRUE \
  -Wno-dev
%make_jobs

%install
%cmake_install

# Create and install pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/codec2.pc << EOF
prefix=%{_prefix}
exec_prefix=\${prefix}
includedir=\${prefix}/include/%{name}
libdir=\${exec_prefix}/%{_lib}

Name:           codec2
Version:        %{version}
License:        GPL-2.0 and LGPL-2.1
Description: Low bit rate speech codec for two-way radio
Cflags: -I\${includedir}
Libs: -L\${libdir} -l%{name}
EOF

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license COPYING
%doc README README_fdmdv.txt
%{_bindir}/c2dec
%{_bindir}/c2demo
%{_bindir}/c2enc
%{_bindir}/c2sim
%{_bindir}/drs232
%{_bindir}/drs232_ldpc
%{_bindir}/fdmdv_demod
%{_bindir}/fdmdv_get_test_bits
%{_bindir}/fdmdv_interleave
%{_bindir}/fdmdv_mod
%{_bindir}/fdmdv_put_test_bits
%{_bindir}/fec_dec
%{_bindir}/fec_enc
%{_bindir}/fsk_mod
%{_bindir}/fm_demod
%{_bindir}/insert_errors

%files -n %{libname}
%{_libdir}/libcodec2.so.*

%files devel
%{_includedir}/*
%{_libdir}/libcodec2.so
%{_libdir}/pkgconfig/%{name}.pc

%files examples
%{_datadir}/%{name}/

%changelog
