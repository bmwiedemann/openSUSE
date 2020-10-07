#
# spec file for package john
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


%define         johndir %{_datadir}/john
%define         jumboversion john-1.9.0-jumbo-1
Name:           john
Version:        1.9.0
Release:        0
Summary:        Utility to detect weak passwords
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://www.openwall.com/john/
Source:         https://www.openwall.com/john/k/%{name}-%{version}.tar.xz
Source1:        https://www.openwall.com/john/k/%{name}-%{version}.tar.xz.sign
Source2:        %{name}.8.gz
Source3:        %{name}-rpmlintrc
Source6:        mailer.8
Source7:        relbench.8
Source8:        https://www.openwall.com/john/k/%{jumboversion}.tar.xz
Source9:        https://www.openwall.com/john/k/%{jumboversion}.tar.xz.sign
# PATCH-FIX-UPSTREAM cl-device.patch gh#openwall/john#4331
Patch0:         cl-device.patch
BuildRequires:  dos2unix
BuildRequires:  gmp-devel
BuildRequires:  libpcap-devel
BuildRequires:  libusb-devel
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(openssl)

%description
John the Ripper is a password cracker (password security auditing
tool). Its primary purpose is to detect weak passwords, and a
number of other hash types are supported to that end.

%prep
%setup -q -a8
cd %{jumboversion} && cp -a ./* ..
cd ..
rm -r %{jumboversion}
%patch0 -p1
# adapt the configs
perl -pi -e "s#Wordlist = (.*)#Wordlist = %{johndir}/password.lst#g" $RPM_BUILD_DIR/%{name}-%{version}/run/john.conf
perl -pi -e 's#^(\#define JOHN_SYSTEMWIDE_EXEC)\s.+$#$1\t\"%{johndir}\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h
perl -pi -e 's#^(\#define CFG_FULL_NAME)\s.+$#$1\t\"%{_sysconfdir}/john.conf\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h
perl -pi -e 's#^(\#define CFG_ALT_NAME)\s.+$#$1\t\"%{_sysconfdir}/john.conf\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h
perl -pi -e 's#^(\#define WORDLIST_NAME)\s.+$#$1\t\"%{johndir}/password.lst\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h
perl -pi -e 's#^(\#define LOG_NAME)\s.+$#$1\t\"%{_localstatedir}/log/john/john.log\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h
perl -pi -e 's#^(\#define JOHN_SYSTEMWIDE_HOME)\s.+$#$1\t\"%{johndir}\"#g' $RPM_BUILD_DIR/%{name}-%{version}/src/params.h

%build
export CFLAGS="%{optflags} -fcommon"
pushd src
%configure --with-systemwide \
           --disable-openmp \
           --enable-fuzz \
           --enable-experimental-code \
           --enable-pkg-config \
%ifarch x86_64
            --enable-simd=avx \
%endif
           --disable-native-tests
%make_build -s clean
%make_build
popd
# fix shebang
sed -i 's|#!%{_bindir}/env perl|#!%{_bindir}/perl|' run/*.pl
sed -i 's|#! %{_bindir}/env perl|#!%{_bindir}/perl|' run/*.pl
sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python|' run/*.py
sed -i 's|#! %{_bindir}/env python|#!%{_bindir}/python|' run/*.py
sed -i 's|#!%{_bindir}/env perl|#!%{_bindir}/perl|' run/relbench

%install
mkdir -p %{buildroot}{%{_bindir},%{johndir},%{johndir}/wordlists,%{_sysconfdir},%{_mandir}/man8}
mkdir -p %{buildroot}%{_localstatedir}/log/john
install -m 755 run/john %{buildroot}%{_bindir}/
install -m 755 run/*.py %{buildroot}%{_bindir}/
install -m 755 run/*.pl %{buildroot}%{_bindir}/
install -m 755 run/un* %{buildroot}%{_bindir}/
install -m 755 run/*2john %{buildroot}%{_bindir}/
install -m 755 run/base64conv %{buildroot}%{_bindir}/
install -m 755 run/relbench %{buildroot}%{_bindir}/
install -m 755 -p run/mailer %{buildroot}%{_bindir}/
install -m 644 -p run/{password.lst,*.chr,d*.conf,h*.conf,k*.conf,r*.conf} %{buildroot}%{johndir}/
install -m 644 -p run/john.conf %{buildroot}%{_sysconfdir}/
touch %{buildroot}%{johndir}/john.local.conf
mkdir -p %{buildroot}%{_datadir}/john/kernels
cp -r run/kernels/* %{buildroot}%{_datadir}/john/kernels/
mkdir -p %{buildroot}%{_datadir}/john/rules
cp -r run/rules/* %{buildroot}%{_datadir}/john/rules/
# handle documentation - makes rpmlint happy
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp README.md  %{buildroot}%{_defaultdocdir}/%{name}/
cp -r doc/* %{buildroot}%{_defaultdocdir}/%{name}/
rm %{buildroot}%{_defaultdocdir}/%{name}/INSTALL
rm %{buildroot}%{_defaultdocdir}/%{name}/README
# install man pages
install -m 644 -p %{SOURCE2} %{buildroot}%{_mandir}/man8/
install -Dm644 %{SOURCE6} %{buildroot}%{_mandir}/man8/mailer.8
install -Dm644 %{SOURCE7} %{buildroot}%{_mandir}/man8/relbench.8
dos2unix %{buildroot}%{_defaultdocdir}/%{name}/README.krb5tgs-17-18-23.md

%files
%doc %{_defaultdocdir}/%{name}/
%{_mandir}/man8/john.8%{?ext_man}
%{_mandir}/man8/mailer.8%{?ext_man}
%{_mandir}/man8/relbench.8%{?ext_man}
%{_bindir}/*
%dir %{johndir}
%dir %{johndir}/kernels/
%{johndir}/kernels/*
%dir %{johndir}/rules/
%{johndir}/rules/*
%dir %{johndir}/wordlists
%attr(644,root,root) %{johndir}/password.lst
%attr(644,root,root) %{johndir}/*.chr
%attr(644,root,root) %{johndir}/d*.conf
%attr(644,root,root) %{johndir}/h*.conf
%attr(644,root,root) %{johndir}/k*.conf
%attr(644,root,root) %{johndir}/r*.conf
%config (noreplace) %{_sysconfdir}/john.conf
%config (noreplace) %{johndir}/john.local.conf
%attr(775,root,users) %dir %{_localstatedir}/log/john

%changelog
