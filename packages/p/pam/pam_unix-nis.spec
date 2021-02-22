#
# spec file for package pam
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


%if !0%{?usrmerged}
%define libdir /%{_lib}
%define sbindir /sbin
%define pamdir /%{_lib}/security
%else
%define libdir %{_libdir}
%define sbindir %{_sbindir}
# moving this to /usr needs fixing
# several packages short of
# https://github.com/linux-pam/linux-pam/issues/256
%define pamdir %{_libdir}/security
%endif

#
%define enable_selinux 1
%define libpam_so_version 0.85.1
%define libpam_misc_so_version 0.82.1
%define libpamc_so_version 0.82.1
%if ! %{defined _distconfdir}
  %define _distconfdir %{_sysconfdir}
  %define config_noreplace 1
%endif
Name:           pam_unix-nis
#
Version:        1.5.1
Release:        0
Summary:        PAM module for standard UNIX and NIS authentication
License:        GPL-2.0-or-later OR BSD-3-Clause
Group:          System/Libraries
URL:            http://www.linux-pam.org/
Source:         Linux-PAM-%{version}.tar.xz
Source9:        baselibs.conf
Patch:          Makefile-pam_unix-nis.diff
BuildRequires:  pam-devel
%if 0%{?suse_version} > 1320
BuildRequires:  pkgconfig(libeconf)
BuildRequires:  pkgconfig(libnsl)
BuildRequires:  pkgconfig(libtirpc)
%endif
%if %{enable_selinux}
BuildRequires:  libselinux-devel
%endif
Provides:       pam:/%{_lib}/security/pam_unix.so
Provides:       pam_unix.so
Conflicts:      pam_unix

%description
This package contains the pam_unix module, which does the standard
UNIX authentication against the passwd and shadow database. This
module has NIS support.

%prep
%setup -q -n Linux-PAM-%{version}
%patch -p1

%build
export CFLAGS="%{optflags} -DNDEBUG"
%configure \
	--includedir=%{_includedir}/security \
	--docdir=%{_docdir}/pam \
	--htmldir=%{_docdir}/pam/html \
	--pdfdir=%{_docdir}/pam/pdf \
%if !0%{?usrmerged}
	--sbindir=/sbin \
	--libdir=/%{_lib} \
%endif
	--enable-isadir=../..%{pamdir} \
	--enable-securedir=%{pamdir} \
	--enable-vendordir=%{_distconfdir} \
	--enable-tally2 --enable-cracklib
make -C modules/pam_unix

%install
mkdir -p %{buildroot}%{pamdir}
install -m 755 modules/pam_unix/.libs/pam_unix.so %{buildroot}%{pamdir}/
for x in pam_unix_auth pam_unix_acct pam_unix_passwd pam_unix_session; do
  ln -f %{buildroot}%{pamdir}/pam_unix.so %{buildroot}%{pamdir}/$x.so
done

%files
%license COPYING
%{pamdir}/pam_unix.so
%{pamdir}/pam_unix_acct.so
%{pamdir}/pam_unix_auth.so
%{pamdir}/pam_unix_passwd.so
%{pamdir}/pam_unix_session.so

%changelog
