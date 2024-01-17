#
# spec file for package librtas-doc
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2.0.5
Release:        0
Summary:        Documents for librtas
License:        LGPL-2.1-or-later
Group:          Documentation/Other
URL:            https://github.com/ibm-power-utilities/librtas
Source0:        https://github.com/ibm-power-utilities/librtas/archive/v%{version}.tar.gz#/librtas-%{version}.tar.gz
Source2:        activate-firmware-regress
Source3:        vpdupdate-regress
Patch0:         librtas.fix_doc_path.patch
Patch1:         0001-librtas-expose-low-level-RTAS-call-APIs-internally.patch
Patch2:         0002-librtas-move-VPD-code-into-separate-module.patch
Patch3:         0003-librtas-move-system-parameter-code-to-separate-modul.patch
Patch4:         0004-librtas-vendor-papr-miscdev.h.patch
Patch5:         0005-librtas-vpd-prefer-dev-papr-vpd-when-available.patch
Patch6:         0006-librtas-sysparm-prefer-dev-papr-sysparm-when-availab.patch
Patch7:         link-lpthread.patch
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
