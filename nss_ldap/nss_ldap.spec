#
# spec file for package nss_ldap
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nss_ldap
Version:        265
Release:        0
Summary:        NSS LDAP Module
License:        LGPL-2.1+
Group:          Productivity/Networking/LDAP/Clients
Url:            http://www.padl.com/OSS/nss_ldap.html
Source:         %{name}-%{version}.tar.gz
Source1:        README.SUSE
Source2:        baselibs.conf
Source3:        ldap.conf
Patch0:         0000-nss_ldap.dif
Patch1:         0001-group-utf8.dif
Patch2:         0002-nss_ldap-ldapconn-leak-bug418.dif
Patch3:         0003-nss_ldap-getent-retry.dif
Patch4:         0004-nss_ldap-getent-skip-invalid-uidgidnumber.dif
# Upstream issue with glibc-2.16 http://bugzilla.padl.com/show_bug.cgi?id=445
Patch5:         0005-nss_ldap-265-glibc-2.16.patch
# Fix also issue with threads on glibc-2.16 http://bugzilla.padl.com/show_bug.cgi?id=446
Patch6:         0006-nss_ldap-265-pthread.patch
# SIGPIPE handling atfork
Patch7:         0007-bnc#842120.dif
# reverse ipv6 host lookups fail when ldap is used
Patch8:         0008-bnc#866763.dif
Patch9:         0009-fix-for-BUG-412-don-t-close-nested-contexts.patch
Patch10:        0010-initialize-context-in-_nss_ldap_getbyname.patch
Patch11:        0011-When-invoked-via-glibc-the-input-buffer-is-enlarged.patch
# PATCH-FIX-TO-UPSTREAM -- is not opensuse specific
Patch12:        reproducible.patch
Patch13:        nss_ldap-perl-5.26.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  db-devel
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  openldap2-devel
Requires(pre):  %{_bindir}/grep
Requires(pre):  /bin/mktemp
Requires(pre):  coreutils
Requires(pre):  sed

%description
Nss_ldap is a glibc NSS module that allows X.500 and LDAP directory
servers to be used as a primary source of aliases, ethers, groups,
hosts, networks, protocol, users, RPCs, services, and shadow passwords
(instead of or in addition to using flat files or NIS).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5
%patch6
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
cp -v %{SOURCE1} .

%build
autoreconf -fiv
CPPFLAGS="-I/usr/include/sasl -DINET6"
%configure \
  --enable-rfc2307bis \
	--enable-paged-results \
  --enable-configurable-krb5-ccname-gssapi \
	--x-libraries=%{_prefix}/X11R6/%{_lib}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_lib}
mkdir -p %{buildroot}%{_libdir}
install -m 755 nss_ldap.so %{buildroot}/%{_lib}/libnss_ldap.so.2
install -d 755 %{buildroot}/%{_sysconfdir}/
install -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/
make DESTDIR=%{buildroot} install-man

%pre
# If we have a /etc/ldap.conf.rpmsave, and no /etc/ldap.conf,
# backup the rpmsave file and use that later instead of our
# own version. This fixes the problem that the file was moved
# from pwdutils to nss_ldap and else the changes would go lost.
if [ ! -e %{_sysconfdir}/ldap.conf -a -f %{_sysconfdir}/ldap.conf.rpmsave ]; then
   cp -p %{_sysconfdir}/ldap.conf.rpmsave %{_sysconfdir}/...ldap.conf.pwdutils
fi

%post
/sbin/ldconfig
# If we backuped ldap.conf, move now the backup in place
test -f %{_sysconfdir}/...ldap.conf.pwdutils && mv %{_sysconfdir}/...ldap.conf.pwdutils %{_sysconfdir}/ldap.conf ||:

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/ldap.conf
%doc ANNOUNCE AUTHORS COPYING ChangeLog NEWS README README.SUSE nsswitch.ldap ldap.conf doc/README.paged
/%{_lib}/libnss_ldap.so.2
%{_mandir}/man5/nss_ldap.5*

%changelog
