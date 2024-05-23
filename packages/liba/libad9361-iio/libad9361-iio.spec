#
# spec file for package libad9361-iio
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


%define sover 0
%define libname libad9361
Name:           libad9361-iio
Version:        0.3
Release:        0
Summary:        Library for AD9361
License:        GPL-3.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/analogdevicesinc/libad9361
#Git-Clone:     https://github.com/analogdevicesinc/libad9361-iio.git
Source:         https://github.com/analogdevicesinc/libad9361-iio/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-lib-dir.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  texlive-dot2texi
BuildRequires:  pkgconfig(libiio)

%description
This is a simple library used for userspace, which manages multi-chip sync, on
platforms (FMCOMMS5) where multiple AD9361 devices are used.

%package -n %{libname}-%{sover}
Summary:        Library for AD9361
Group:          Hardware/Other

%description -n %{libname}-%{sover}
This is a simple library used for userspace, which manages multi-chip sync, on
platforms (FMCOMMS5) where multiple AD9361 devices are used.

%package devel
Summary:        Development files for libad9361
Group:          Development/Libraries/Other
Requires:       %{libname}-%{sover} = %{version}

%description devel
This is a simple library used for userspace, which manages multi-chip sync, on
platforms (FMCOMMS5) where multiple AD9361 devices are used.

%package devel-doc
Summary:        Documentation for libad9361-iio
Group:          Documentation/Other
BuildArch:      noarch

%description devel-doc
Documentation for libad9361-iio library.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_SHARED_LINKER_FLAGS=""
%make_build

%install
%cmake_install
%fdupes %{buildroot}

#move docs
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/ad93610-doc/html %{buildroot}%{_docdir}/%{name}

%post -n %{libname}-%{sover} -p /sbin/ldconfig
%postun -n %{libname}-%{sover} -p /sbin/ldconfig

%files -n %{libname}-%{sover}
%license LICENSE
%doc README.md
%{_libdir}/libad9361.so.%{sover}*
%dir %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/html

%files devel
%{_includedir}/ad9361*.h
%{_libdir}/libad9361.so
%{_libdir}/pkgconfig/libad9361.pc

%files devel-doc
%{_docdir}/%{name}/html

%changelog
