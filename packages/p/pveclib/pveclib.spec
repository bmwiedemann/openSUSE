#
# spec file for package pveclib
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           pveclib
Version:        1.0.4
Release:        0
Summary:        Power Vector Library
License:        Apache-2.0

Url:            https://github.com/open-power-sdk/pveclib
Source:         https://github.com/open-power-sdk/pveclib/archive/v%{version}.tar.gz
ExclusiveArch:  ppc64le
BuildRequires:  glibc-devel doxygen graphviz fdupes

# Link the tests against the shared library.
Patch1: test-shared-library.diff

%description
See description for libpvec1

%package -n libpvec1
Summary: Power Vector Library

%description -n libpvec1
Functions leveraging the PowerISA Vector Facilities: Vector Multimedia
Extension (VMX aka Altivec) and Vector Scalar Extension (VSX).

This package contains the runtime files for pveclib.

%package -n libpvec-devel
Summary: Development files for pveclib
Requires: libpvec1 = %{version}

%description -n libpvec-devel
This package contains the development files for pveclib.

%prep
%autosetup -p1

%build
# Set the install path of the documentation to %%{_docdir}/libpvec-devel
# in the configure step, otherwise, the documentation gets installed
# directly under %%{_docdir}, instead of under a subdirectory. Also,
# disable the static libraries.
%configure --docdir=%{_docdir}/libpvec-devel --disable-static
%make_build

%check
make %{?_smp_mflags} check

%install
%make_install
# Remove .la files as recommended by openSUSE's library packaging guidelines:
# https://en.opensuse.org/openSUSE:Shared_library_packaging_policy#Best_Practices
find %{buildroot} -type f -name "*.la" -delete
# Upstream build rules produce .so* files for libpvecstatic, even
# thought they are not supposed to be installed. Remove them.
find %{buildroot} -type f -name "libpvecstatic.so*" -delete
find %{buildroot} -type l -name "libpvecstatic.so*" -delete
# By default, upstream installs the license file under:
# $(datadir)/licenses/pveclib, which would make sense if it were
# installed in the pveclib package. However, the pveclib package has
# been made empty, thus not generated, so move the license file to
# libpvec-devel.
mv %{buildroot}/%{_datadir}/licenses/pveclib %{buildroot}/%{_datadir}/licenses/libpvec-devel
# Convert identical files into hardlinks.
%fdupes %{buildroot}/%{_prefix}

%post -n libpvec1 -p /sbin/ldconfig
%postun -n libpvec1 -p /sbin/ldconfig

%files -n libpvec1
%{_libdir}/libpvec.so.*
# Distribute a copy of the LICENSE with the runtime package to fulfill
# the requirement in section 4, first item, of the Apache 2.0 license.
%license LICENSE

%files -n libpvec-devel
%{_libdir}/libpvec.so
%{_includedir}/pveclib
%doc %{_docdir}/libpvec-devel/
%license LICENSE

%changelog

