#
# spec file for package zita-convolver
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 4
Name:           zita-convolver
Version:        4.0.3
Release:        0
Summary:        A partitioned convolution engine library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://kokkinizita.linuxaudio.org/linuxaudio/
Source:         https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fftw3f)

%description
Convolution engine based on FFT convolution and using non-uniform partition
sizes: small ones at the start of the IR and building up to the most efficient
size further on. It can perform zero-delay processing with moderate CPU load.

Main features:
  * Any matrix of convolutions between up to up 64 inputs and 64 outputs, as
    long as your CPU(s) can handle it.
  * Allows trading off CPU load to processing delay, and remains efficient even
    when configured for zero delay.
  * Sparse and diagonal matrices are handled as efficiently as dense ones.
    No CPU cycles or memory resources are wasted on empty cells in the matrix,
    nor on empty partitions if IRs are of different length.

%package -n lib%{name}%{sover}
Summary:        A partitioned convolution engine library
Group:          System/Libraries

%description -n lib%{name}%{sover}
Convolution engine based on FFT convolution and using non-uniform partition
sizes: small ones at the start of the IR and building up to the most efficient
size further on. It can perform zero-delay processing with moderate CPU load.

Main features:
  * Any matrix of convolutions between up to up 64 inputs and 64 outputs, as
    long as your CPU(s) can handle it.
  * Allows trading off CPU load to processing delay, and remains efficient even
    when configured for zero delay.
  * Sparse and diagonal matrices are handled as efficiently as dense ones.
    No CPU cycles or memory resources are wasted on empty cells in the matrix,
    nor on empty partitions if IRs are of different length.

%package -n %{name}-devel
Summary:        Development files for zita-convolver
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
Requires:       pkgconfig(fftw3f)

%description -n %{name}-devel
Development package for zita-convolver, a partitioned convolution engine
library.

%prep
%setup -q
sed -i 's,ldconfig,,' source/Makefile

%build
make -C source %{?_smp_mflags} CXXFLAGS="%{optflags} -fPIC"

%install
%make_install -C source PREFIX=%{_prefix} LIBDIR=%{_prefix}/%{_lib}

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license COPYING
%{_libdir}/lib%{name}.so.*

%files -n %{name}-devel
%doc README
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
