#
# spec file for package john
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           john
Version:        1.8.0
Release:        0
Summary:        Detects Weak Passwords
License:        GPL-2.0+
Group:          Productivity/Security
Url:            http://www.openwall.com/john/
Source:         http://www.openwall.com/john/j/%{name}-%{version}.tar.xz
Source1:        http://www.openwall.com/john/j/%{name}-%{version}.tar.xz.sign
Source2:        %{name}.8.gz
Source3:        %{name}-rpmlintrc
Source6:        mailer.8
Source7:        relbench.8
%define         jumboversion john-1.7.9-jumbo-7
Source8:        %{jumboversion}.tar.bz2
Source9:        %{jumboversion}.tar.bz2.sign
Patch0:         john-1.7.9-powerpc_BE_need_rhash_u32_swap_copy.patch
Patch1:         ppc64le.patch
# PATCH-FIX-UPSTREAM https://github.com/magnumripper/JohnTheRipper/pull/2560
Patch2:         reproducible.patch
BuildRequires:  pkgconfig(openssl)
BuildConflicts: pkgconfig(openssl) >= 1.1
%if 0%{?suse_version} == 1110 
BuildRequires:  xz
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define         johndir /var/lib/john
%define cflags CFLAGS="-c %{optflags} -DJOHN_SYSTEMWIDE=1 -finline-limit=2000 --param inline-unit-growth=2000" LDFLAGS="-lcrypto"
%ifarch x86_64
%define cflags CFLAGS="-c %{optflags} -DJOHN_SYSTEMWIDE=1" LDFLAGS="-lcrypto"
%endif

%description
John the Ripper is a fast password cracker (password security auditing
tool). Its primary purpose is to detect weak Unix passwords, but a
number of other hash types are supported as well.

%prep
%setup -q -a8
%patch0 -p1
%patch2 -p1
cd %{jumboversion} && cp -a ./* ..
cd ..
rm -r %{jumboversion}
%patch1 -p1
# adapt the configs
perl -pi -e "s#Wordlist = (.*)#Wordlist = %{johndir}/password.lst#g" $RPM_BUILD_DIR/%{name}-%{version}/run/john.conf
perl -pi -e 's#^(\#define JOHN_SYSTEMWIDE_EXEC)\s.+$#$1\t\"%{johndir}\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h
perl -pi -e 's#^(\#define CFG_FULL_NAME)\s.+$#$1\t\"%{_sysconfdir}/john.conf\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h
perl -pi -e 's#^(\#define CFG_ALT_NAME)\s.+$#$1\t\"%{_sysconfdir}/john.conf\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h
perl -pi -e 's#^(\#define WORDLIST_NAME)\s.+$#$1\t\"%{johndir}/password.lst\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h
perl -pi -e 's#^(\#define LOG_NAME)\s.+$#$1\t\"/var/log/john.log\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h
perl -pi -e 's#^(\#define JOHN_SYSTEMWIDE_HOME)\s.+$#$1\t\"%{johndir}\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h

%build
%ifarch alpha
		TARGET=linux-alpha
%endif
%ifarch ia64
		TARGET=linux-ia64
%endif
%ifarch %ix86
%ifnarch i386 i486
		TARGET=linux-x86-mmx
%endif
%endif
%ifarch ppc
		TARGET=linux-ppc32
%endif
%ifarch ppc64 ppc64le
		TARGET=linux-ppc64
%endif
%ifarch sparc sparcv9
		TARGET=linux-sparc
%endif
%ifarch sparc64
		TARGET=solaris-sparc64-gcc
%endif
%ifarch x86_64
		TARGET=linux-x86-64
%endif
%ifarch %arm aarch64 m68k
		TARGET=generic
%endif
%ifarch %ix86
if test -z "$TARGET"; then
    TARGET=linux-x86-any
fi
%endif
export TARGET
pushd src
make clean $TARGET %{cflags} LDFLAGS='-lcrypto -lm -lz -lssl'
popd

%check
pushd src
make check
popd

%install
mkdir -p %{buildroot}{%{_bindir},%johndir,%{_sysconfdir},%{_mandir}/man8}
install -m 755 run/john %{buildroot}%{_bindir}/
cp -r run/un* %{buildroot}%{_bindir}/
install -m755 run/relbench %{buildroot}%{_bindir}/
install -m 644 -p run/{password.lst,*.chr,d*.conf,*local.conf} %{buildroot}%johndir/
install -m 644 -p run/john.conf %{buildroot}%{_sysconfdir}/
install -m 755 -p run/mailer %{buildroot}%{_bindir}/
# handle documentation - makes rpmlint happy
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp README-jumbo doc/* %{buildroot}%{_defaultdocdir}/%{name}/
rm %{buildroot}%{_defaultdocdir}/%{name}/INSTALL
# install man pages
install -m 644 -p %{SOURCE2} %{buildroot}%{_mandir}/man8/
install -Dm644 %{SOURCE6} %{buildroot}%{_mandir}/man8/mailer.8
install -Dm644 %{SOURCE7} %{buildroot}%{_mandir}/man8/relbench.8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}/
%doc %{_mandir}/man8/john.8*
%doc %{_mandir}/man8/mailer.8*
%doc %{_mandir}/man8/relbench.8*
%{_bindir}/un*
%{_bindir}/relbench
%dir %{johndir}
%attr(750,root,wheel) %{_bindir}/john
%{_bindir}/mailer
%attr(644,root,root) %johndir/password.lst
%attr(644,root,root) %johndir/*.chr
%attr(644,root,root) %johndir/d*.conf
%attr(644,root,root) %johndir/*local.conf
%config (noreplace) %{_sysconfdir}/john.conf

%changelog
