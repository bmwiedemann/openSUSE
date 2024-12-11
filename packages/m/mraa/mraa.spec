#
# spec file for package mraa
#
# Copyright (c) 2024 SUSE LLC
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


%define         sover 2
Name:           mraa
Version:        2.2.0
Release:        0
Summary:        Low Level Skeleton Library for IO Communication
License:        MIT
URL:            https://github.com/eclipse/mraa
Source:         https://github.com/eclipse/mraa/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         mraa-i686.patch
%if 0%{?suse_version} > 1500
BuildRequires:  strip-nondeterminism
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(python3)
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
libmraa is a C/C++ library with bindings to Java, Python and JavaScript to
interface with the IO on Galileo, Edison & other platforms, with a
structured and sane API where port names/numbering matches the board that
you are on. Use of libmraa does not tie you to specific hardware with board
detection done at runtime you can create portable code that will work
across the supported platforms.

The intent is to make it easier for developers and sensor manufacturers to
map their sensors & actuators on top of supported hardware and to allow
control of low level communication protocol by high level languages &
constructs.

%package -n lib%{name}%{sover}
Summary:        Low Level Skeleton Library for IO Communication

%description -n lib%{name}%{sover}
libmraa is a C/C++ library with bindings to Java, Python and JavaScript to
interface with the IO on Galileo, Edison & other platforms, with a
structured API where port names/numbering matches the board that
you are on. Use of libmraa does not tie you to specific hardware. With board
detection done at runtime, you can create portable code that will work
across the supported platforms.

This package contains shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}

%description devel
libmraa is a C/C++ library with bindings to Java, Python and JavaScript to
interface with the IO on Galileo, Edison & other platforms, with a
structured API where port names/numbering matches the board that
you are on. Use of libmraa does not tie you to specific hardware. With board
detection done at runtime, you can create portable code that will work
across the supported platforms.

This package contains development files for %{name}.

%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
Requires:       lib%{name}%{sover} = %{version}

%description -n python3-%{name}
libmraa is a C/C++ library with bindings to Java, Python and JavaScript to
interface with the IO on Galileo, Edison & other platforms, with a
structured API where port names/numbering matches the board that
you are on. Use of libmraa does not tie you to specific hardware. With board
detection done at runtime, you can create portable code that will work
across the supported platforms.

This package contains python3 bindings for %{name}.

%package -n java-%{name}
Summary:        Java bindings for %{name}
Requires:       javapackages-tools
Requires:       lib%{name}%{sover} = %{version}

%description -n java-%{name}
libmraa is a C/C++ library with bindings to Java, Python and JavaScript to
interface with the IO on Galileo, Edison & other platforms, with a
structured API where port names/numbering matches the board that
you are on. Use of libmraa does not tie you to specific hardware. With board
detection done at runtime, you can create portable code that will work
across the supported platforms.

This package contains java bindings for %{name}.

%package -n nodejs-%{name}
Summary:        Nodes bindings for %{name}

%description -n nodejs-%{name}
libmraa is a C/C++ library with bindings to Java, Python and JavaScript to
interface with the IO on Galileo, Edison & other platforms, with a
structured API where port names/numbering matches the board that
you are on. Use of libmraa does not tie you to specific hardware. With board
detection done at runtime, you can create portable code that will work
across the supported platforms.

This package contains nodejs bindings for %{name}.

%package examples
Summary:        Examples for %{name}
BuildArch:      noarch

%description examples
libmraa is a C/C++ library with bindings to Java, Python and JavaScript to
interface with the IO on Galileo, Edison & other platforms, with a
structured API where port names/numbering matches the board that
you are on. Use of libmraa does not tie you to specific hardware. With board
detection done at runtime you can create portable code that will work
across the supported platforms.

This package contains examples for %{name}.

%prep
%autosetup

%build
%cmake \
  -DCMAKE_C_FLAGS="%{optflags} -fcommon -DNDEBUG" \
  -DINSTALLTOOLS=yes \
  -DINSTALLGPIOTOOL=yes \
  -DUSBPLAT=yes \
  -DFIRMATA=off \
  -DIMRAA=yes \
  -DFTDI4222=off \
  -DBUILDTESTS=on \
  -DBUILDSWIGPYTHON=on \
  -DBUILDSWIGJAVA=on \
  -DBUILDSWIGNODE=off \
  -Wno-dev
%cmake_build

%install
%cmake_install
install -d %{buildroot}%{_javadir}
mv %{buildroot}%{_prefix}/lib/java/mraa.jar %{buildroot}%{_javadir}/%{name}.jar
%if 0%?have_strip_nondeterminism > 0
strip-nondeterminism %{buildroot}%{_javadir}/%{name}.jar
%endif

%check
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
%ctest

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_bindir}/imraa
%{_bindir}/mraa-gpio
%{_bindir}/mraa-i2c
%{_bindir}/mraa-uart

%files -n lib%{name}%{sover}
%{_libdir}/libmraa.so.%{sover}
%{_libdir}/libmraa.so.%{version}

%files devel
%{_libdir}/libmraa.so
%{_includedir}/%{name}.*
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files -n python3-%{name}
%{python3_sitearch}/%{name}.py
%{python3_sitearch}/_%{name}.so

%files -n java-%{name}
%{_javadir}/%{name}.jar
%{_libdir}/libmraajava.so
%{_libdir}/pkgconfig/mraajava.pc

%files examples
%{_datadir}/%{name}

%changelog
