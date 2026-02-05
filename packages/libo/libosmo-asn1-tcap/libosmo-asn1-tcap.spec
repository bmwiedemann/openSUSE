#
# spec file for package libosmo-asn1-tcap
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define _lto_cflags %nil
Name:           libosmo-asn1-tcap
%define lname   libosmo-asn1-tcap1
Version:        0.2.1
Release:        0
Summary:        ASN.1 library for parsing the TCAP protocol (SS7)
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://gitea.osmocom.org/ss7-in-c/libosmo-asn1-tcap
Source:         https://github.com/osmocom/libosmo-asn1-tcap/archive/refs/tags/%version.tar.gz
Patch1:         build.patch
BuildRequires:  automake
BuildRequires:  libtool >= 2
BuildRequires:  pkg-config >= 0.20

%description
A TCAP message decoding library.

%package -n %lname
Summary:        ASN.1 library for TCAP protocol (SS7)
Group:          System/Libraries

%description -n %lname
A TCAP message decoding library.

%package devel
Summary:        Header files for the Osmocom ASN.1-TCAP library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Header files for a TCP message decoding library.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fiv
# bugzilla.opensuse.org/795968 for rationale
%configure --includedir="%_includedir/%name" \
	--enable-shared --disable-static
%make_build

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete

#%check
# TS fails to build (because it tries to reference a static archive that does not exist)
# and also fails to build when pointed at the shared library because of symbols marked hidden

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/libosmo-asn1-tcap.so.*

%files devel
%_includedir/%name/
%_libdir/libosmo-asn1-tcap.so
%_libdir/pkgconfig/libosmo-asn1-tcap.pc

%changelog
