#
# spec file for package upm
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


%define         sover 1
Name:           upm
Version:        2.0.0
Release:        0
Summary:        High-level repository for sensors that use mraa
License:        MIT
Group:          Hardware/Other
URL:            https://github.com/intel-iot-devkit/UPM
Source:         https://github.com/intel-iot-devkit/UPM/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(mraa) >= 2.0.0
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python3)
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
The UPM repository provides software drivers for a wide variety of commonly
used sensors and actuators. These software drivers interact with the
underlying hardware platform (or microcontroller), as well as with the
attached sensors, through calls to MRAA APIs.

%package -n lib%{name}%{sover}
Summary:        High-level repository for sensors that use mraa
Group:          System/Libraries

%description -n lib%{name}%{sover}
The UPM repository provides software drivers for a wide variety of commonly
used sensors and actuators. These software drivers interact with the
underlying hardware platform (or microcontroller), as well as with the
attached sensors, through calls to MRAA APIs.

This package contains shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
The UPM repository provides software drivers for a wide variety of commonly
used sensors and actuators. These software drivers interact with the
underlying hardware platform (or microcontroller), as well as with the
attached sensors, through calls to MRAA APIs.

Programmers can access the interfaces for each sensor by including the
sensor’s corresponding header file and instantiating the associated sensor
class. In the typical use case, a constructor initializes the sensor based
on parameters that identify the sensor, the I/O protocol used and the pin
location of the sensor.

This package contains development files for %{name}.

%package -n python2-%{name}
Summary:        Python bindings for %{name}
Group:          Development/Languages/Python
Requires:       lib%{name}%{sover} = %{version}
Provides:       python-%{name} = %{version}
Obsoletes:      python-%{name} < %{version}

%description -n python2-%{name}
The UPM repository provides software drivers for a wide variety of commonly
used sensors and actuators. These software drivers interact with the
underlying hardware platform (or microcontroller), as well as with the
attached sensors, through calls to MRAA APIs.

This package contains python bindings for %{name}.

%package -n python3-%{name}
Summary:        Python bindings for %{name}
Group:          Development/Languages/Python
Requires:       lib%{name}%{sover} = %{version}

%description -n python3-%{name}
The UPM repository provides software drivers for a wide variety of commonly
used sensors and actuators. These software drivers interact with the
underlying hardware platform (or microcontroller), as well as with the
attached sensors, through calls to MRAA APIs.

This package contains python3 bindings for %{name}.

%package -n nodejs-%{name}
Summary:        Nodejs bindings for %{name}
Group:          Development/Languages/Other
%requires_ge    nodejs6

%description -n nodejs-%{name}
The UPM repository provides software drivers for a wide variety of commonly
used sensors and actuators. These software drivers interact with the
underlying hardware platform (or microcontroller), as well as with the
attached sensors, through calls to MRAA APIs.

This package contains nodejs bindings for %{name}.

%prep
%setup -q
# remove CC BY-NC-SA 3.0 licenced images
rm -rf docs/images

%build
%define __builder ninja
%define _lto_cflags %{nil}
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DCMAKE_EXE_LINKER_FLAGS="" \
  -DCMAKE_MODULE_LINKER_FLAGS="" \
  -DBUILDSWIGNODE=off \
  -DBUILDFTI=on \
  -Wno-dev
%make_jobs

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/upm

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}*.so.%{sover}*

%files devel
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}*

%files -n python2-%{name}
%{python_sitearch}/*

%files -n python3-%{name}
%{python3_sitearch}/*

%changelog
