#
# spec file for package pam_krb5
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           pam_krb5
BuildRequires:  klogd
BuildRequires:  krb5-client
BuildRequires:  krb5-devel
BuildRequires:  krb5-server
BuildRequires:  libselinux-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
Provides:       pam_krb
# bug437293
%ifarch ppc64
Obsoletes:      pam_krb5-64bit
%endif
#
Version:        2.4.13
Release:        0
Summary:        A Pluggable Authentication Module for Kerberos 5
License:        BSD-3-Clause or LGPL-2.1+
Group:          Productivity/Networking/Security
Url:            https://pagure.io/pam_krb5
Source:         pam_krb5-%{version}.tar.bz2
Source2:        pam_krb5-po.tar.bz2
Source3:        baselibs.conf
Patch1:         pam_krb5-2.3.1-log-choise.dif
Patch3:         pam_krb5-2.3.1-switch-perms-on-refresh.dif
Patch4:         pam_krb5-2.2.3-1-setcred-assume-establish.dif
Patch5:         bug-641008_pam_krb5-2.3.11-setcred-log.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This PAM module supports authentication against a Kerberos KDC. It also
supports updating your Kerberos password.

%prep
%setup -q -n pam_krb5-%{version}
%setup -a 2 -T -D -n pam_krb5-%{version}
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE "         \
./configure --libdir=/%{_lib}    \
            --prefix=/usr        \
            --mandir=%{_mandir}  \
            --with-os-distribution="openSUSE" \
            --with-default-use-shmem="sshd" \
            --with-default-external="sshd sshd-rekey gssftp" \
            --with-default-multiple-ccaches="su su-l" \
            --with-default-no-cred-session="sshd" \
            --enable-default-ccname-template=DIR:/run/user/%%U/krb5cc_XXXXXX
make -j1
make -C po update-po
# does not work in the buildservice
#make check

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
ln -sf pam_krb5.so $RPM_BUILD_ROOT/%_lib/security/pam_krb5afs.so
rm -f $RPM_BUILD_ROOT/%_lib/security/*.la

# Make the paths jive to avoid conflicts on multilib systems.
sed -ri -e 's|/lib(64)?/|/\$LIB/|g' $RPM_BUILD_ROOT/%{_mandir}/man*/pam_krb5*.8*

# Create filelist with translatins
%{find_lang} pam_krb5

%clean
rm -rf $RPM_BUILD_ROOT

%files -f pam_krb5.lang
%defattr(-,root,root,-)
%doc README* COPYING* ChangeLog AUTHORS NEWS
%{_bindir}/*
%attr(555,root,root) /%{_lib}/security/pam_krb5.so
%attr(555,root,root) /%{_lib}/security/pam_krb5afs.so
/%{_lib}/security/pam_krb5
%_mandir/man*/*.*

%changelog
