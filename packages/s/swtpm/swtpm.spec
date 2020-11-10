#
# spec file for package swtpm
#
# Copyright (c) 2019 SUSE LLC
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

Name:           swtpm
Version:        0.5.0
Release:        0
Summary:        Software TPM emulator
License:        BSD-3-Clause
Group:          System/Base
Url:            https://github.com/stefanberger/swtpm
Source:         https://github.com/stefanberger/swtpm/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  expect
BuildRequires:  libtool
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel
BuildRequires:  gnutls
BuildRequires:  libgnutls-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libtpms-devel
BuildRequires:  python3-cryptography
BuildRequires:  socat
%if 0%{?suse_version} >= 1500 
BuildRequires:  net-tools-deprecated
%endif
Requires:       trousers
%if 0%{?suse_version} >= 1500 
Requires:       net-tools-deprecated
%endif
Requires:       python3-cryptography
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The SWTPM package provides TPM emulators with different front-end interfaces
to libtpms. TPM emulators provide socket interfaces (TCP/IP) and the Linux
CUSE interface for the creation of multiple native /dev/vtpm* devices.
Those can be the targets of multiple QEMU cuse-tpm instances.

%package        devel
Summary:        Development files for swtpm
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glib2-devel
Requires:       libtpms-devel
Requires:       libopenssl-devel
Requires:       libseccomp-devel

%description    devel
The development files for SWTPM

%prep
%setup -q -n %{name}-%{version}

%build
./autogen.sh
%configure --with-openssl --disable-static \
     --with-tss-user=root --with-tss-group=tss
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/swtpm*
%config %{_sysconfdir}/swtpm*
%dir %{_datadir}/swtpm
%{_datadir}/swtpm/*
%dir %{_libdir}/swtpm
%{_libdir}/swtpm/*.so.*
%{_mandir}/man8/swtpm*
%dir %{python_sitelib}/py_swtpm_localca
%dir %{python_sitelib}/py_swtpm_setup
%pycache_only %{python_sitelib}/py_swtpm_localca/__pycache__
%pycache_only %{python_sitelib}/py_swtpm_setup/__pycache__
%{python_sitelib}/py_swtpm_localca/*.py
%{python_sitelib}/py_swtpm_setup/*.py
%{python_sitelib}/swtpm_localca*
%{python_sitelib}/swtpm_setup*

%files devel
%{_libdir}/swtpm/*.so
%{_libdir}/swtpm/*.la
%dir %{_includedir}/swtpm/
%{_includedir}/swtpm/*
%{_mandir}/man3/swtpm*

%changelog
