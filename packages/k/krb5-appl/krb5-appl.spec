#
# spec file for package krb5-appl
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


%define srcRoot krb5-appl-1.0.3/
%define vendorFiles %{_builddir}/%{srcRoot}/vendor-files/
%define krb5docdir  %{_defaultdocdir}/krb5

Name:           krb5-appl
URL:            https://web.mit.edu/kerberos/www/
BuildRequires:  bison
BuildRequires:  krb5-devel
BuildRequires:  libcom_err-devel
BuildRequires:  ncurses-devel
Version:        1.0.3
Release:        0
Summary:        MIT Kerberos5 Implementation--Applications
License:        MIT
Group:          Productivity/Networking/Security
Source0:        krb5-appl-%{version}.tar.bz2
Source1:        vendor-files.tar.bz2
Source2:        README.Source
Source3:        spx.c
Patch1:         krb5-appl-1.0-fix-ftp-var-used-uninitialized.dif
Patch2:         krb5-appl-1.0-fix-var-used-before-value-set.dif
Patch3:         krb5-appl-1.0-fix-path-in-manpages.dif
Patch4:         krb5-appl-1.0.3-libc.patch
Patch5:         krb5-appl-fix-build.patch
# build with gcc14
Patch6:         krb5-appl-gcc14.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Kerberos V5 is a trusted-third-party network authentication system,
which can improve your network's security by eliminating the insecure
practice of clear text passwords.

%package clients
Summary:        MIT Kerberos5 client applications
Group:          Productivity/Networking/Security
Provides:       krb5-apps-clients
Obsoletes:      krb5-apps-clients

%description clients
Kerberos V5 is a trusted-third-party network authentication system,
which can improve your network's security by eliminating the insecure
practice of cleartext passwords. This package includes some kerberos
compatible client applications like ftp, rpc, rlogin, telnet, ...

%package servers
Summary:        MIT Kerberos5 server applications
Group:          Productivity/Networking/Security
Provides:       krb5-apps-servers
Obsoletes:      krb5-apps-servers

%description servers
Kerberos V5 is a trusted-third-party network authentication system,
which can improve your network's security by eliminating the insecure
practice of cleartext passwords. This package includes some kerberos
compatible server applications like ftpd, klogind, telnetd, ...

%prep
%setup -q -n %{srcRoot}
%setup -a 1 -T -D -n %{srcRoot}
if [ -e %{_builddir}/%{srcRoot}/telnet/libtelnet/spx.c ]
then
 echo "spx.c contains potential legal risks."
 exit 1;
else
 cp %{SOURCE3} %{_builddir}/%{srcRoot}/telnet/libtelnet/spx.c
fi

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1

%build
./autogen.sh
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/et -fpie" \
LDFLAGS="-pie " \
./configure \
	--prefix=/usr/lib/mit \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--libexecdir=/usr/lib/mit/sbin \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
        --localstatedir=%{_localstatedir}/lib/kerberos
make %{?jobs:-j%jobs}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_sysconfdir}
for n in ftpd.8 telnetd.8; do
        mv %{buildroot}%{_mandir}/man8/${n} %{buildroot}%{_mandir}/man8/k${n}
done
for n in ftp.1 rlogin.1 rcp.1 rsh.1 telnet.1; do
        mv %{buildroot}%{_mandir}/man1/${n} %{buildroot}%{_mandir}/man1/k${n}
done

# install xinetd files
mkdir -p %{buildroot}%{_sysconfdir}/xinetd.d
install -m 644 %{vendorFiles}/klogin.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/klogin
install -m 644 %{vendorFiles}/eklogin.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/eklogin
install -m 644 %{vendorFiles}/krb5-telnet.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/ktelnet
install -m 644 %{vendorFiles}/kshell.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/kshell

# install doc
install -d -m 755 %{buildroot}/%{krb5docdir}
install -m 644 %{_builddir}/%{srcRoot}/README %{buildroot}/%{krb5docdir}/README.apps
install -m 644 %{_builddir}/%{srcRoot}/NOTICE %{buildroot}/%{krb5docdir}/NOTICE.apps
# cleanup
rm -f  %{buildroot}/usr/share/man/man1/tmac.doc*

%clean
rm -rf %{buildroot}
########################################################
# files sections
########################################################

%files clients
%defattr(-,root,root)
%dir %{krb5docdir}
%dir /usr/lib/mit
%dir /usr/lib/mit/bin
%doc %{krb5docdir}/README.apps
%doc %{krb5docdir}/NOTICE.apps
/usr/lib/mit/bin/ftp
/usr/lib/mit/bin/rlogin
/usr/lib/mit/bin/rcp
/usr/lib/mit/bin/rsh
/usr/lib/mit/bin/telnet
%{_mandir}/man1/kftp.1*
%{_mandir}/man1/krlogin.1*
%{_mandir}/man1/krsh.1*
%{_mandir}/man1/ktelnet.1*
%{_mandir}/man1/krcp.1*

%files servers
%defattr(-,root,root)
%dir %{_sysconfdir}/xinetd.d
%config(noreplace) %{_sysconfdir}/xinetd.d/klogin
%config(noreplace) %{_sysconfdir}/xinetd.d/eklogin
%config(noreplace) %{_sysconfdir}/xinetd.d/kshell
%config(noreplace) %{_sysconfdir}/xinetd.d/ktelnet
%dir /usr/lib/mit
%dir /usr/lib/mit/sbin
/usr/lib/mit/sbin/ftpd
/usr/lib/mit/sbin/klogind
/usr/lib/mit/sbin/kshd
/usr/lib/mit/sbin/telnetd
/usr/lib/mit/sbin/login.krb5
%{_mandir}/man8/kftpd.8*
%{_mandir}/man8/klogind.8*
%{_mandir}/man8/kshd.8*
%{_mandir}/man8/ktelnetd.8*
%{_mandir}/man8/login.krb5.8*

%changelog
