#
# spec file for package lib3270
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) <2008> <Banco do Brasil S.A.>
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


Name:           lib3270
Version:        5.5.0+git20250123
Release:        0
Summary:        TN3270 Access library
License:        LGPL-3.0-only
Group:          System/Libraries
URL:            https://github.com/PerryWerneck/lib3270
Source:         %{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  meson

%description
TN3270 access library, originally designed as part of the pw3270 application.

For more details, see https://softwarepublico.gov.br/social/pw3270/ .

%define MAJOR_VERSION %(echo %{version} | cut -d. -f1)
%define MINOR_VERSION %(echo %{version} | cut -d. -f2 | cut -d+ -f1)
%define _libvrs %{MAJOR_VERSION}_%{MINOR_VERSION}

%package -n %{name}-%{_libvrs}
Summary:        TN3270 Access library
Group:          Development/Libraries/C and C++

%description -n %{name}-%{_libvrs}
TN3270 access library, originally designed as part of the pw3270 application.

For more details, see https://softwarepublico.gov.br/social/pw3270/ .

%package devel
Summary:        TN3270 Access library development files
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{_libvrs} = %{version}

%description devel
Header files for the TN3270 access library.

%lang_package -n %{name}-%{_libvrs}

%prep
%autosetup
%meson

%build
%meson_build

%install
%meson_install

%find_lang lib3270-%{MAJOR_VERSION}.%{MINOR_VERSION} langfiles

%fdupes %{buildroot}/%{_prefix}

%files -n %{name}-%{_libvrs}

# https://en.opensuse.org/openSUSE:Packaging_for_Leap#RPM_Distro_Version_Macros
%if 0%{?sle_version} > 120200
%doc AUTHORS README.md
%license LICENSE
%else
%doc LICENSE AUTHORS README.md
%endif
%{_libdir}/*.so.%{MAJOR_VERSION}.%{MINOR_VERSION}

%files devel
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/*.h
%{_includedir}/lib3270

%{_libdir}/pkgconfig/*.pc

%files -n %{name}-%{_libvrs}-lang -f langfiles

%post -n %{name}-%{_libvrs} -p /sbin/ldconfig
%postun -n %{name}-%{_libvrs} -p /sbin/ldconfig

%changelog
