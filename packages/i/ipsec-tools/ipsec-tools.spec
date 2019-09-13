#
# spec file for package ipsec-tools
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           ipsec-tools
Version:        0.8.2
Release:        0
Summary:        IPsec Utilities
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
Url:            http://ipsec-tools.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/ipsec-tools/ipsec-tools-%{version}.tar.bz2
Source2:        sysconfig.racoon
Source3:        setkey.conf.sample
Source4:        racoon.pam
Source5:        racoon.service
Source6:        racoon-setkey.service
Patch0:         racoon.conf_macros.patch
Patch1:         racoon.psk.patch
Patch2:         ipsec-tools-0.7.3-linkerflag.patch
Patch3:         ipsec-tools-0.8.0-nodevel.patch
Patch4:         ipsec-tools-0.8.0-certasn1txtbroken.patch
Patch5:         racoon-fips-rsa.patch
Patch6:         racoon-no-md5.patch
Patch7:         ipsec-tools-openssl1.1.patch
Patch8:         avoid-dos-with-fragment-out-of-order.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  linux-glibc-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel
BuildRequires:  pam
BuildRequires:  pam-devel
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(systemd)
Requires(post): %fillup_prereq
Provides:       racoon
%{?systemd_requires}

%description
This is the IPsec-Tools package.  This package is needed to really make
use of the IPsec functionality in the version 2.5 and 2.6 Linux
kernels.  This package builds:
  - libipsec, a PFKeyV2 library
  - setkey, a program to directly manipulate policies and SAs
  - racoon, an IKEv1 keying daemon
These sources can be found at the IPsec-Tools home page at:
http://ipsec-tools.sourceforge.net/

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
if pkg-config --atleast-version=1.1.0 libssl; then
%patch7 -p1
fi
%patch8

./bootstrap
sed -i 's|-Werror||g' configure

%build
%configure \
	--disable-shared \
	--libexecdir=%{_libdir} \
	--sysconfdir=%{_sysconfdir}/racoon \
	--sharedstatedir=/run \
	--localstatedir=/run \
	--with-kernel-headers="%{_prefix}/include" \
	--enable-dpd \
	--enable-hybrid \
	--enable-frag \
	--enable-natt=yes \
	--enable-gssapi=yes \
	--enable-stats=yes \
	--enable-adminport \
	--with-libpam \
	--enable-security-context=yes \
	--with-libldap
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pam.d/racoon
install -d %{buildroot}%{_sysconfdir}/racoon/cert
# unify the permissions of psk.txt - fdupes is sensitive on permissions now (bnc#784670)
chmod 0600 src/racoon/samples/psk.txt
install -m 0600 src/racoon/samples/psk.txt %{buildroot}%{_sysconfdir}/racoon/
install -m 0644 src/racoon/samples/racoon.conf %{buildroot}%{_sysconfdir}/racoon/
cp -v $RPM_SOURCE_DIR/setkey.conf.sample %{buildroot}%{_sysconfdir}/racoon/setkey.conf
mkdir -p %{buildroot}%{_fillupdir}
install -m 644 $RPM_SOURCE_DIR/sysconfig.racoon %{buildroot}%{_fillupdir}/
# manage doc
mkdir -p %{buildroot}%{_docdir}/%{name}/examples/{setkey,racoon}
cp -rv src/racoon/samples %{buildroot}%{_docdir}/%{name}/examples/racoon
cp -v src/setkey/sample* %{buildroot}%{_docdir}/%{name}/examples/setkey
for i in ChangeLog NEWS README; do
	install -D -m 0644 $i %{buildroot}%{_docdir}/%{name}/
done
# systemd magic
install -d %{buildroot}%{_tmpfilesdir}
echo 'd /run/racoon 0700 root root -' > %{buildroot}%{_tmpfilesdir}/racoon.conf
install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/racoon.service
install -D -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/racoon-setkey.service
ln -s service %{buildroot}%{_sbindir}/rcracoon
ln -s service %{buildroot}%{_sbindir}/rcracoon-setkey

# do not fdupe the whole tree, otherwise it might symlink /etc config files into /usr
%fdupes -s %{buildroot}/usr

%pre
%service_add_pre racoon.service racoon-setkey.service

%post
%{fillup_only -n racoon}
%tmpfiles_create %{_tmpfilesdir}/racoon.conf
%service_add_post racoon.service racoon-setkey.service

%preun
%service_del_preun racoon.service racoon-setkey.service

%postun
%service_del_postun racoon.service racoon-setkey.service

%files
%defattr(-,root,root)
%{_unitdir}/*.service
%{_sbindir}/rcracoon
%{_sbindir}/rcracoon-setkey
%{_tmpfilesdir}/racoon.conf
%doc %{_docdir}/%{name}/
%config(noreplace) %{_sysconfdir}/racoon/psk.txt
%config(noreplace) %{_sysconfdir}/racoon/racoon.conf
%config(noreplace) %{_sysconfdir}/racoon/setkey.conf
%config %{_sysconfdir}/pam.d/racoon
%dir %{_sysconfdir}/racoon
%dir %{_sysconfdir}/racoon/cert
%{_sbindir}/racoon
%{_sbindir}/racoonctl
%{_sbindir}/setkey
%{_sbindir}/plainrsa-gen
%{_fillupdir}/sysconfig.racoon
%{_mandir}/man*/*
%ghost /run/racoon

%changelog
