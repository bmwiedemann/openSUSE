#
# spec file for package librtas-doc
#
# Copyright (c) 2025 SUSE LLC
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


Name:           librtas-doc
Version:        2.0.6
Release:        0
Summary:        Documents for librtas
License:        LGPL-2.1-or-later
Group:          Documentation/Other
URL:            https://github.com/ibm-power-utilities/librtas
Source0:        https://github.com/ibm-power-utilities/librtas/archive/v%{version}.tar.gz#/librtas-%{version}.tar.gz
Source2:        activate-firmware-regress
Source3:        vpdupdate-regress
Patch0:         librtas.fix_doc_path.patch
Patch7:         0001-librtas-Move-platform-dump-rtas-call-code-to-separat.patch
Patch8:         0002-librtas-platform-dump-prefer-dev-papr-platform-dump-.patch
Patch9:         0003-librtas-move-get-set-indices-RTAS-calls-code-to-sepa.patch
Patch10:        0004-librtas-Add-kernel-uapi-header-papr-indices.h.patch
Patch11:        0005-librtas-Use-dev-papr-indices-when-available-for-ibm-.patch
Patch12:        0006-librtas-Use-dev-papr-indices-when-available-for-get-.patch
Patch13:        0007-librtas-Use-dev-papr-indices-when-available-for-set-.patch
Patch14:        0008-librtas-Move-physical-attestation-rtas-call-code-to-.patch
Patch15:        0009-librtas-Use-kernel-interface-when-available-for-ibm-.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
ExclusiveArch:  ppc ppc64 ppc64le

%description
This package provides librtas documentation

%prep
%autosetup -p1 -n librtas-%{version}

%build
./autogen.sh
%configure
make -O V=1 VERBOSE=1 CFLAGS="%{optflags} -fPIC -g -I $PWD/librtasevent_src" LIB_DIR="%{_libdir}" %{?_smp_mflags}

%install
rm -rf doc/*/latex
make install DESTDIR=%{buildroot} LIB_DIR="%{_libdir}"
rm -rf %{buildroot}/%{_libdir}
rm -rf %{buildroot}/%{_includedir}
%fdupes %{buildroot}/%{_docdir}

%files
%doc %{_docdir}/librtas

%changelog
