#
# spec file for package odp
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


# ODP does not promise backwards compatibility between releases, so we
# just enforce major:minor:point as version number.
%define maj 122
%define min 0
%define point 0
%define lname libodp-%{maj}_%{min}_%{point}
Name:           odp
Version:        1.22.0.0
Release:        0
Summary:        OpenDataPlane Reference implementation
License:        BSD-3-Clause
URL:            https://www.opendataplane.org
Source0:        https://git.linaro.org/lng/odp.git/snapshot/odp-%{version}.tar.gz
Patch0:         configure-suppress-pointer-to-packed-structure-warni.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  libconfig-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
Conflicts:      odp-any
Provides:       odp-any = %{version}
ExclusiveArch:  aarch64 x86_64 ppc64 ppc64le

%description
The OpenDataPlane reference implementation library, development files
and examples for the ThunderX platform.

%package -n %{lname}
Summary:        OpenDataPlane Reference implementation
Conflicts:      %{lname}-any
Provides:       %{lname}-any = %{version}
Provides:       odp-libs = %{version}
Obsoletes:      odp-libs < 1.12

%description -n %{lname}
Reference implementation for OpenDataPlane (ODP).
The ODP project is a set of APIs for the networking data plane.

%package devel
Summary:        Development files for the OpenDataPlane reference implementation
Requires:       %{lname} = %{version}-%{release}
Requires:       libopenssl-devel
Conflicts:      odp-any-devel
Provides:       odp-any-devel = %{version}

%description devel
This package contains the development files for the OpenDataPlane
reference implementation.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"
./bootstrap
%configure \
  --disable-static \
  --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name 'libodp*.la' |xargs rm -f
rm -f %{buildroot}%{_bindir}/odp_*
rm -rf %{buildroot}%{_sysconfdir}/odp

%files -n %{lname}
%license LICENSE
%doc README CHANGELOG
%{_libdir}/libodp*.so.*

%files devel
%{_includedir}/odp*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%changelog
