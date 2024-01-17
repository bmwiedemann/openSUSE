#
# spec file for package libacars
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


%define sover   1
%define libname libacars%{sover}
Name:           libacars
Version:        1.3.1
Release:        0
Summary:        A library for decoding various ACARS message payloads
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/szpajder/libacars
#Git-Clone:     https://github.com/szpajder/libacars.git
Source:         https://github.com/szpajder/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
libacars is a library for decoding various ACARS message payloads.

%package -n %{libname}
Summary:        A library for decoding various ACARS message payloads
Group:          System/Libraries

%description -n %{libname}
libacars is a library for decoding various ACARS message payloads.

%package devel
Summary:        Development files for libacars
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libacars is a library for decoding various ACARS message payloads.

This subpackage contains libraries and header files for developing
applications that want to make use of libacars.

%package -n acars-examples
Summary:        Example applications for libacars
Group:          Productivity/Hamradio/Other

%description -n acars-examples
Example applications for for libacars:

 * decode_arinc.c - decodes ARINC-622 messages supplied at the
   command line or from a file.
 * adsc_get_position - illustrates how to extract position-related
   fields from decoded ADS-C message.
 * cpdlc_get_position - illustrates how to extract position-related
   fields from CPDLC position reports.
 * media_advisory - decodes Media Advisory messages (ACARS label SA
   reports)

%prep
%setup -q

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DCMAKE_SHARED_LINKER_FLAGS=""
%make_jobs

%install
%cmake_install
rm -rf %{buildroot}/%{_datadir}/doc

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_libdir}/libacars.so.%{sover}*

%files devel
%doc doc/API_REFERENCE.md doc/API_REFERENCE.md
%{_includedir}/libacars
%{_libdir}/libacars.so
%{_libdir}/pkgconfig/libacars.pc

%files -n acars-examples
%{_bindir}/adsc_get_position
%{_bindir}/cpdlc_get_position
%{_bindir}/decode_acars_apps
%{_bindir}/media_advisory

%changelog
