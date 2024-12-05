#
# spec file for package swtpm
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?suse_version} > 01500
%bcond_without use_selinux
%else
%bcond_with use_selinux
%endif

# Scripts in this package are python3
%define skip_python2 1
# SELinux
%define selinuxtype targeted
%define modulename1 swtpm
%define modulename2 swtpm_svirt
%define modulename3 swtpmcuse
Name:           swtpm
Version:        0.10.0
Release:        0
Summary:        Software TPM emulator
License:        BSD-3-Clause
Group:          System/Base
URL:            https://github.com/stefanberger/swtpm
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source100:      swtpm-rpmlintrc
Patch0:         swtpm-fix-build.patch
# 19-09-24 cahu bsc#1229131
# this can be removed once swtpm upstream sorts out their custom selinux module
# see: https://github.com/stefanberger/swtpm/issues/885
# there were a couple changes in the selinux-policy libvirt handling
# which causes the logfile in /var/log/swtpm/libvirt/qemu/*.log to be labeled
# virt_log_t instead of var_log_t.
# this patch allows swtpm_t to open the virt_log_t
Patch1:         1229131-fix-swtpm-selinux-policy-mismatch.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  expect
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel
BuildRequires:  gmp-devel
BuildRequires:  gnutls
BuildRequires:  iproute2
BuildRequires:  libgnutls-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libtool
BuildRequires:  libtpms-devel
BuildRequires:  pkgconfig
%if %{with use_selinux}
BuildRequires:  selinux-policy-devel
BuildRequires:  selinux-policy-targeted
%endif
BuildRequires:  socat
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(systemd)
# Required for certtool, which is used by swtpm-localca
Requires:       gnutls
Requires:       iproute2
%if %{with use_selinux}
Requires:       (%{name}-selinux if selinux-policy-base)
%endif
Requires(pre):  user(tss)

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

%if %{with use_selinux}
%package        selinux
Summary:        SELinux module for the Software TPM emulator
Group:          System/Management
Requires:       %{name} = %{version}
BuildArch:      noarch
%{selinux_requires}

%description    selinux
This package provides the SELinux module for the Software TPM emulator.
%endif

%prep
%autosetup -p1

%build
mkdir m4
autoreconf -fiv
# configure looks for semodule on PATH
export PATH="$PATH:%{_sbindir}"
%configure --with-openssl --disable-static \
     --with-tss-user=root --with-tss-group=tss \
%if %{with use_selinux}
     --with-selinux
%else

%endif
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%if %{with use_selinux}
mkdir %{buildroot}%{_datadir}/selinux/packages/targeted
mv %{buildroot}%{_datadir}/selinux/packages/*.pp %{buildroot}%{_datadir}/selinux/packages/targeted
%endif
mkdir -p %{buildroot}%{_localstatedir}/lib/swtpm-localca
sed -e 's|#!/usr/bin/env |#!/usr/bin/|g' -i %{buildroot}%{_datadir}/swtpm/swtpm-create-tpmca
sed -e 's|#!/usr/bin/env |#!/usr/bin/|g' -i %{buildroot}%{_datadir}/swtpm/swtpm-create-user-config-files

%check
# fix check-local
# https://bugzilla.suse.com/show_bug.cgi?id=1204556#c9
sed -i "s@\(-L\./\.libs\)@\1 -Wl,--no-as-needed@" src/Makefile
%make_build check
rm -fr %{buildroot}%{_libexecdir}/installed-tests

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%if %{with use_selinux}
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/targeted/%{modulename1}.pp
%selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/targeted/%{modulename2}.pp
%selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/targeted/%{modulename3}.pp

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 %{modulename1}
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 %{modulename2}
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 %{modulename3}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}
%endif

%files
%doc CHANGES README TODO
%license LICENSE
%{_bindir}/swtpm*
%config %{_sysconfdir}/swtpm*
%{_datadir}/swtpm
%dir %{_libdir}/swtpm
%{_libdir}/swtpm/*.so.*
%{_mandir}/man5/swtpm*%{?ext_man}
%{_mandir}/man8/swtpm*%{?ext_man}
%dir %attr(0750,tss,root) %{_localstatedir}/lib/swtpm-localca

%files devel
%{_libdir}/swtpm/*.so
%{_includedir}/swtpm
%{_mandir}/man3/swtpm*%{?ext_man}

%if %{with use_selinux}
%files selinux
%{_datadir}/selinux/packages/targeted/*.pp
%ghost %verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename1}
%ghost %verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename2}
%ghost %verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename3}
%endif

%changelog
