#
# spec file for package opie
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


Name:           opie
Summary:        Support for One-Time Passwords
License:        SUSE-Innernet-2.0
Group:          Productivity/Security
Version:        2.4
Release:        0
URL:            http://www.inner.net/opie
%define name_pam         pam_opie
%define version_pam	 0.21
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name_pam}-%{version_pam}.tar.bz2
Source2:        baselibs.conf
Patch0:         %{name}-%{version}.diff
Patch1:         %{name_pam}-%{version_pam}.diff
Patch2:         %{name}-%{version}.newseed.diff 
Patch3:         uint4_def.patch
Patch4:         %name-2.4-bison.patch
Patch5:         %name-2.4-nonvoid.patch
Patch6:         %name-2.4-decl.diff
Patch7:         %name-2.4-nul-overflow.patch
Patch8:         %name-2.4-cxx.patch
Patch9:         %name-2.4-undef.patch
Patch10:        %name-2.4-noroot.patch
Patch11:        %{name}-%{version}_array-subscript.patch
Patch12:        %{name_pam}-%{version_pam}_array-subscript.patch
Patch13:        %name-2.4-getline.patch
Patch14:        %name-2.4-fclose.patch
Patch15:        %name-2.4-implicit.patch
Patch16:        opielogin-setuid-CVE-2011-2490.patch
Patch17:        opiesu-overflow-CVE-2011-2489.patch
Patch18:        opie-fix-autoconf.patch
Patch19:        opie-2.4-DESTDIR.patch
Patch20:        opie-2.4-pie.patch
Patch21:        opie-fix-indendation.patch
#!BuildIgnore: opie
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  pam-devel
Provides:       pam_opie
Requires(post): permissions

%description
OPIE stands for One-time Passwords In Everything. One-time passwords
can be used to foil password sniffers because they cannot be reused by
the attacker.

This package provides a PAM module and several utility programs that
let you use one-time passwords for authentication.

%prep
%setup -q -n %{name}-%{version} -a 1
%patch0 -p1
%patch2 -p1
%patch3
%patch4
%patch5
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9
%patch19 -p1
%patch10 -p1
%patch11
pushd %{name_pam}
%patch1 -p0
%patch12
popd
%patch13
%patch14
%patch15 -p1
%patch16
%patch17
%patch18
%patch20 -p1
%patch21 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
# build opie
export CFLAGS="%{optflags} -fno-strict-aliasing"
export SUID_CFLAGS="-fPIC" SUID_LDFLAGS="-pie"
autoreconf -i -f
%configure --enable-insecure-override
make %{?_smp_mflags}

# build pam_opie
cd %{name_pam}
make %{?_smp_mflags}

%install
# install opie
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/%{_mandir}/man1/
#
%make_install CHOWN=/bin/echo
install -m 644 -D opie.h %{buildroot}/%{_includedir}/opie.h
install -m 644 -D libopie/libopie.a %{buildroot}/%{_libdir}/libopie.a
mv %{name_pam}/README ./README.PAM
# install pam_opie
cd %{name_pam}
make FAKEROOT="%{buildroot}" \
     SECUREDIR=/%{_lib}/security install

%verifyscript
%verify_permissions /usr/bin/opiepasswd

%post
%set_permissions /usr/bin/opiepasswd

%files
%dir /etc/opielocks
%attr(0600,root,root) %config(noreplace) /etc/opiekeys
/usr/bin/opieftpd
/usr/bin/opiegen
/usr/bin/opieinfo
/usr/bin/opiekey
/usr/bin/opielogin
%verify(not mode) /usr/bin/opiepasswd
# packaged without setuid-root, because of bad code quality (bsc#882035)
%verify(not mode) %attr(0755,root,root) /usr/bin/opiesu
/usr/bin/otp-md4
/usr/bin/otp-md5
/%{_lib}/security/pam_opie.so
/%{_includedir}/opie.h
/%{_libdir}/libopie.a
%doc BUG-REPORT COPYRIGHT.NRL License.TIN README README.PAM
%doc %{_mandir}/man*/*

%changelog
