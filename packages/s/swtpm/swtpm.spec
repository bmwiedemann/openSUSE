#
# spec file for package swtpm
#
# Copyright (c) 2021 SUSE LLC
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


# Scripts in this package are python3
%define skip_python2 1

Name:           swtpm
Version:        0.5.2
Release:        0
Summary:        Software TPM emulator
License:        BSD-3-Clause
Group:          System/Base
URL:            https://github.com/stefanberger/swtpm
Source:         https://github.com/stefanberger/swtpm/archive/v%{version}.tar.gz
Patch0:         swtpm-rename_deprecated_libtasn1_types.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  expect
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel
BuildRequires:  gnutls
BuildRequires:  iproute2
BuildRequires:  libgnutls-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libtool
BuildRequires:  libtpms-devel
BuildRequires:  python3-cryptography
BuildRequires:  socat
Requires:       iproute2
Requires:       python3-cryptography
Requires:       trousers
Requires:       user(tss)
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
Requires:       libopenssl-devel
Requires:       libseccomp-devel
Requires:       libtpms-devel

%description    devel
The development files for SWTPM

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build

# Fix rpmlint env-script-interpreter error
sed -i -e "s|^#!/usr/bin/env |#!/usr/bin/|" \
  %_builddir/%buildsubdir/src/swtpm_setup/swtpm_setup.in \
  %_builddir/%buildsubdir/src/swtpm_setup/py_swtpm_setup/swtpm_setup.py \
  %_builddir/%buildsubdir/samples/swtpm-create-tpmca \
  %_builddir/%buildsubdir/samples/swtpm-create-user-config-files.in \
  %_builddir/%buildsubdir/samples/swtpm-localca.in \
  %_builddir/%buildsubdir/samples/py_swtpm_localca/swtpm_localca.py

./autogen.sh
%configure --with-openssl --disable-static \
     --with-tss-user=root --with-tss-group=tss
make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}%{_localstatedir}/lib/swtpm-localca

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc CHANGES README TODO
%license LICENSE
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
%dir %attr(0750,tss,root) %{_localstatedir}/lib/swtpm-localca

%files devel
%{_libdir}/swtpm/*.so
%{_libdir}/swtpm/*.la
%dir %{_includedir}/swtpm/
%{_includedir}/swtpm/*
%{_mandir}/man3/swtpm*

%changelog
