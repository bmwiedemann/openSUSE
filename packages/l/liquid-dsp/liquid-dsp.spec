#
# spec file for package liquid-dsp
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define use_build_checks 0
%define libname libliquid

Name:           liquid-dsp
Version:        1.6.0
Release:        0
Summary:        Digital signal processing library for software-defined radios
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://liquidsdr.org
#Git-Clone:     https://github.com/jgaeddert/liquid-dsp.git
Source:         https://github.com/jgaeddert/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fftw3)
%ifarch x86_64 aarch64
BuildRequires:  pkgconfig(libfec)
%endif

%description
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP modules
that do no rely on external dependencies or cumbersome frameworks.

%package -n %{libname}
Summary:        Digital signal processing library for software-defined radios
Group:          Development/Libraries/C and C++

%description -n %{libname}
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP modules
that do no rely on external dependencies or cumbersome frameworks.

%package -n %{libname}-devel
Summary:        Development files for the liquid-dsp library
Group:          Development/Libraries/C and C++
Requires:       libliquid = %{version}

%description -n %{libname}-devel
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP modules
that do no rely on external dependencies or cumbersome frameworks.

This subpackage contains libraries and header files for developing
applications that want to make use of libliquid.

%prep
%setup -q
rm scripts/ax_ext.m4 # avoid CPU-detection on build machine (boo#1100677)

%build
./bootstrap.sh
%configure -disable-static
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/libliquid.a*

# fix library executable flag
chmod a+x %{buildroot}/%{_libdir}/libliquid.so.1.6

%post    -n %{libname} -p /sbin/ldconfig
%postun  -n %{libname} -p /sbin/ldconfig

%check
%if 0%{?use_build_checks}
make %{?_smp_mflags} check
%endif

%files -n %{libname}
%license LICENSE
%doc HISTORY README.md TROUBLESHOOTING
%{_libdir}/%{libname}.so.*

%files -n %{libname}-devel
%dir %{_includedir}/liquid
%{_includedir}/liquid/liquid.h
%{_libdir}/%{libname}.so

%changelog
