#
# spec file for package liquid-dsp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           liquid-dsp
Version:        1.3.2
Release:        0
Summary:        Digital signal processing library for software-defined radios
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://liquidsdr.org
#Git-Clone:     https://github.com/jgaeddert/liquid-dsp.git
Source:         https://github.com/jgaeddert/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         liquid-dsp-fix-destdir.diff
Patch1:         reproducible.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fftw3)
%ifnarch %{arm}
BuildRequires:  pkgconfig(libfec)
%endif

%description
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP modules
that do no rely on external dependencies or cumbersome frameworks.

%package -n libliquid-devel
Summary:        Development files for the liquid-dsp library
Group:          Development/Libraries/C and C++

%description -n libliquid-devel
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP modules
that do no rely on external dependencies or cumbersome frameworks.

This subpackage contains libraries and header files for developing
applications that want to make use of libliquid.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}/%{_libdir}/libliquid.a

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
%if 0%{?use_build_checks}
make %{?_smp_mflags} check
%endif

%files -n libliquid-devel
%license LICENSE
%doc HISTORY README.md TROUBLESHOOTING
%dir %{_includedir}/liquid
%{_includedir}/liquid/liquid.h
%{_libdir}/libliquid.so

%changelog
