#
# spec file for package libacars2
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2019-2025, Martin Hauke <mardnh@gmx.de>
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


%define sover   2
%define libname libacars-2-%{sover}
Name:           libacars2
Version:        2.2.1
Release:        0
Summary:        A library for decoding various ACARS message payloads
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/szpajder/libacars
#Git-Clone:     https://github.com/szpajder/libacars.git
Source:         https://github.com/szpajder/libacars/archive/v%{version}.tar.gz#/libacars-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib) >= 1.2

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

%package -n acars2-examples
Summary:        Example applications for libacars
Group:          Productivity/Hamradio/Other
Conflicts:      acars-examples

%description -n acars2-examples
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
%autosetup -n libacars-%{version}

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DCMAKE_SHARED_LINKER_FLAGS=""

%install
%cmake_install
rm -rf %{buildroot}/%{_datadir}/doc

%check
%ctest

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_libdir}/libacars-2.so.%{sover}*

%files devel
%license LICENSE.md
%doc doc/API_REFERENCE.md
%{_includedir}/libacars-2
%{_libdir}/libacars-2.so
%{_libdir}/pkgconfig/libacars-2.pc

%files -n acars2-examples
%license LICENSE.md
%{_bindir}/adsc_get_position
%{_bindir}/cpdlc_get_position
%{_bindir}/decode_acars_apps

%changelog
