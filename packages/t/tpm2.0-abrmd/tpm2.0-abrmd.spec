#
# spec file for package tpm2.0-abrmd
#
# Copyright (c) 2022 SUSE LLC
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


%global selinuxtype targeted
%global modulename tabrmd
# the auto activation is not whitelisted for <= SLE12-SP3
%if 0%{?sle_version} > 120300 || 0%{?is_opensuse}
%define install_dbus_files 1
%endif
# selinux only for Tumbleweed for now
%if 0%{?suse_version} >= 1550 && 0%{?is_opensuse}
%bcond_without selinux
%else
%bcond_with selinux
%endif
Name:           tpm2.0-abrmd
Version:        3.0.0
Release:        0
Summary:        Intel's TCG Software Stack Access Broker & Resource Manager for TPM 2.0 chips
License:        BSD-2-Clause
Group:          Productivity/Security
URL:            https://github.com/tpm2-software/tpm2-abrmd
Source0:        https://github.com/tpm2-software/tpm2-abrmd/releases/download/%{version}/tpm2-abrmd-%{version}.tar.gz
Source1:        https://github.com/tpm2-software/tpm2-abrmd/releases/download/%{version}/tpm2-abrmd-%{version}.tar.gz.asc
# curl https://github.com/williamcroberts.gpg > tpm2-abrmd.keyring
Source2:        tpm2-abrmd.keyring
Source3:        tpm2.0-abrmd.rpmlintrc
Source4:        README.SUSE
Patch0:         harden_tpm2-abrmd.service.patch
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  checkpolicy
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  policycoreutils
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(tss2-sys)
Requires:       libtss2-tcti-device0
Requires:       libtss2-tcti-tabrmd0
Requires:       tpm2-0-tss
Requires(pre):  user(tss)
%if %{with selinux}
BuildRequires:  selinux-policy-devel
BuildRequires:  selinux-policy-targeted
BuildRequires:  pkgconfig(systemd)
Requires:       (%{name}-selinux if selinux-policy-base)
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

%if %{with selinux}
%package selinux
Summary:        SELinux module for the Access Broker & Resource Manager for TPM 2.0 chips
Group:          System/Management
Requires:       tpm2.0-abrmd = %{version}
BuildArch:      noarch
%{selinux_requires}

%description selinux
This package provides the SELinux module for the Access Broker & Resource Manager for TPM 2.0 chips.
%endif

%package -n libtss2-tcti-tabrmd0
Summary:        Client interface library for tpm2-abrmd
Group:          System/Libraries

%description -n libtss2-tcti-tabrmd0
This library allows to interact with the tpm2-abrmd daemon. It is intended for
use with the SAPI library (libtss2-sys) like any other TCTI.

%post -n libtss2-tcti-tabrmd0 -p /sbin/ldconfig
%postun -n libtss2-tcti-tabrmd0 -p /sbin/ldconfig

%prep
%autosetup -n tpm2-abrmd-%{version} -p1

%build
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="$LDFLAGS -pie"
%configure \
    --disable-static \
    %{?with_selinux: --with-sepolicy=yes} \
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-dbuspolicydir=%{_datadir}/dbus-1/system.d
%make_build PTHREAD_LDFLAGS=-pthread

%install
%make_install
# don't package libtool files as is best practice
find %{buildroot} -type f -name "*.la" -delete -print
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rctpm2-abrmd
# don't install the systemd preset, our presets are handled by
# systemd-presets-* packages
rm %{buildroot}%{_prefix}/lib*/systemd/system-preset/tpm2-abrmd.preset
cp %{SOURCE4} .
%if ! 0%{?install_dbus_files}
rm %{buildroot}/%{_sysconfdir}/dbus-1/system.d/tpm2-abrmd.conf
rm %{buildroot}/%{_datadir}/dbus-1/system-services/com.intel.tss2.Tabrmd.service
%endif
%if %{with selinux}
mkdir %{buildroot}%{_datadir}/selinux/packages/targeted
mv %{buildroot}%{_datadir}/selinux/packages/tab* %{buildroot}%{_datadir}/selinux/packages/targeted
%endif

%pre
%service_add_pre tpm2-abrmd.service

%post
%service_add_post tpm2-abrmd.service

%postun
%service_del_postun tpm2-abrmd.service

%preun
%service_del_preun tpm2-abrmd.service

%if %{with selinux}
%pre selinux
%{selinux_relabel_pre -s %{selinuxtype}}

%post selinux
%{selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/targeted/%{modulename}.pp.bz2}

%postun selinux
if [ $1 -eq 0 ]; then
    %{selinux_modules_uninstall -s %{selinuxtype} -p 200 %{modulename}}
fi

%posttrans selinux
%{selinux_relabel_post -s %{selinuxtype}}
%endif

%files
%doc *.md README.SUSE
%license LICENSE
%{_mandir}/man7/tss2-*
%{_mandir}/man8/tpm2-*
%{_sbindir}/tpm2-abrmd
%{_sbindir}/rctpm2-abrmd
%{_unitdir}/tpm2-abrmd.service
%if 0%{?install_dbus_files}
# the auto activation is not whitelisted for <= SLE12-SP3
%{_datadir}/dbus-1/system.d/tpm2-abrmd.conf
%{_datadir}/dbus-1/system-services/com.intel.tss2.Tabrmd.service
%endif

%if %{with selinux}
%files selinux
%{_datadir}/selinux/packages/targeted/tabrmd.pp.bz2
%ghost %verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%endif

%files devel
%{_includedir}/tss2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/Tss2*
%if %{with selinux}
%{_datadir}/selinux/devel/include/contrib/tabrmd.if
%endif

%files -n libtss2-tcti-tabrmd0
%{_libdir}/libtss2-tcti-tabrmd.so.*

%changelog
