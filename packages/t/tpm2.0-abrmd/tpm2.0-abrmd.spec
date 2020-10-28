#
# spec file for package tpm2.0-abrmd
#
# Copyright (c) 2020 SUSE LLC
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


Name:           tpm2.0-abrmd
Version:        2.3.3
Release:        0
Summary:        Intel's TCG Software Stack Access Broker & Resource Manager for TPM 2.0 chips
License:        BSD-2-Clause
Group:          Productivity/Security
URL:            https://github.com/tpm2-software/tpm2-abrmd
Source0:        https://github.com/tpm2-software/tpm2-abrmd/releases/download/%{version}/tpm2-abrmd-%{version}.tar.gz
Source1:        tpm2.0-abrmd.rpmlintrc
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(tss2-sys)
Requires(pre):  shadow
Recommends:     libtss2-tcti-device0
Recommends:     libtss2-tcti-tabrmd0
Requires:       tpm2-0-tss
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# the auto activation is not whitelisted for <= SLE12-SP3
%if 0%{?sle_version} > 120300 || 0%{?is_opensuse}
%define install_dbus_files 1
%endif

%description
The tpm2.0-abrmd package provides the TPM2 Access Broker & Resource Manager.
This is a daemon service that coordinates requests to the TPM2 chip via
Intel's TPM 2.0 software stack.

%package devel
Summary:        Development headers the Access Broker & Resource Manager for TPM 2.0 chips
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libtss2-tcti-tabrmd0 = %{version}
Requires:       tpm2.0-abrmd = %{version}

%description devel
This package provides the development files for the Access Broker & Resource
Manager for coordinating access to TPM 2.0 chips.

%package -n libtss2-tcti-tabrmd0
Summary:        Client interface library for tpm2-abrmd
Group:          System/Libraries

%description -n libtss2-tcti-tabrmd0
This library allows to interact with the tpm2-abrmd daemon. It is intended for
use with the SAPI library (libtss2-sys) like any other TCTI.

%post -n libtss2-tcti-tabrmd0 -p /sbin/ldconfig
%postun -n libtss2-tcti-tabrmd0 -p /sbin/ldconfig

%prep
%setup -q -n tpm2-abrmd-%{version}

%build
export CFLAGS="%optflags -fPIE"
export LDFLAGS="-pie -fPIE"
# workaround for the bug that upstream commit
# b4036908dd067f8eadc9d53b1a2a39032aed109d fixes
export GDBUS_CODEGEN="/usr/bin/gdbus-codegen"
%configure --disable-static --with-systemdsystemunitdir=%{_unitdir}
make %{?_smp_mflags} PTHREAD_LDFLAGS=-pthread

# TODO: add the tss user again
%install
%make_install
# don't package libtool files as is best practice
find %{buildroot} -type f -name "*.la" -delete -print
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rctpm2-abrmd
# don't install the systemd preset, our presets are handled by
# systemd-presets-* packages
rm %{buildroot}/usr/lib*/systemd/system-preset/tpm2-abrmd.preset
%if ! 0%{?install_dbus_files}
rm %{buildroot}/%{_sysconfdir}/dbus-1/system.d/tpm2-abrmd.conf
rm %{buildroot}/%{_datadir}/dbus-1/system-services/com.intel.tss2.Tabrmd.service
%endif

%pre
%service_add_pre tpm2-abrmd.service

%post
%service_add_post tpm2-abrmd.service

%postun
%service_del_postun tpm2-abrmd.service

%preun
%service_del_preun tpm2-abrmd.service

%files
%defattr(-,root,root)
%doc *.md LICENSE
%{_mandir}/man7/tss2-*
%{_mandir}/man8/tpm2-*
%{_sbindir}/tpm2-abrmd
%{_sbindir}/rctpm2-abrmd
%{_unitdir}/tpm2-abrmd.service
%if 0%{?install_dbus_files}
# the auto activation is not whitelisted for <= SLE12-SP3
%config %{_sysconfdir}/dbus-1/system.d/tpm2-abrmd.conf
%{_datadir}/dbus-1/system-services/com.intel.tss2.Tabrmd.service
%endif

%files devel
%defattr(-,root,root)
%{_includedir}/tss2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/Tss2*

%files -n libtss2-tcti-tabrmd0
%defattr(-,root,root)
%{_libdir}/libtss2-tcti-tabrmd.so.*

%changelog
