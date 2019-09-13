#
# spec file for package libtpms
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


%define lname libtpms0
Name:           libtpms
Version:        0.7.0
Release:        0
Summary:        Library providing Trusted Platform Module (TPM) functionality
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/stefanberger/libtpms
Source0:        https://github.com/stefanberger/libtpms/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  mozilla-nspr-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

%description
A library providing TPM functionality for VMs. Targeted for integration
into Qemu.

%package -n %{lname}
Summary:        Library providing Trusted Platform Module (TPM) functionality
Group:          Development/Libraries/C and C++

%description -n %{lname}
A library providing TPM functionality for VMs. Targeted for integration
into Qemu.

%package        devel
Summary:        Include files for libtpms
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       libopenssl-devel
Requires:       mozilla-nspr-devel

%description   devel
Libtpms header files and documentation.

%prep
%setup -q -n libtpms-%{version}

%build
./bootstrap.sh
%configure \
	--with-tpm2 \
	--with-openssl	\
        --disable-static

make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
install -d -m 0755 %{buildroot}%{_libdir}
install -d -m 0755 %{buildroot}%{_includedir}/libtpms
install -d -m 0755 %{buildroot}%{_mandir}/man3

%make_install

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%doc README CHANGES
%license LICENSE
%{_libdir}/%{name}.so.%{version}
%{_libdir}/%{name}.so.0

%files devel
%{_libdir}/%{name}.so
%{_libdir}/%{name}.la
%dir %{_includedir}/%{name}
%attr(644, root, root) %{_libdir}/pkgconfig/*.pc
%attr(644, root, root) %{_includedir}/%{name}/*.h
%attr(644, root, root) %{_mandir}/man3/*

%changelog
