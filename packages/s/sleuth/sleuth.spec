#
# spec file for package sleuth
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sleuth
BuildRequires:  apache2-devel
BuildRequires:  libapr-util1-devel
BuildRequires:  pcre-devel
Version:        1.4.4
Release:        0
Requires:       perl-Net-DNS
Source:         %{name}-%{version}.tar.bz2
Patch:          %{name}-%{version}.diff
Url:            ftp://atrey.karlin.mff.cuni.cz/pub/local/mj/net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Perl script for easy checking (DNS, common errors and etc.)
License:        GPL-2.0+
Group:          Productivity/Networking/DNS/Utilities
BuildArch:      noarch
%define apache_serverroot %(/usr/sbin/apxs2 -q datadir 2>/dev/null || apxs -q PREFIX)

%description
Sleuth is a perl script designed for easy checking of DNS zones for
common errors and also for processing of secondary name service
requests. It was written after examination of at least a dozen of
utilities claiming to do this job, finding that all of them are either
unable to discover most zone bugs or too ugly to maintain. Sleuth also
lists the corresponding RFC references with most of its error messages,
so that the people upset with their zones being buggy can simply look
up what is exactly going wrong and how to fix it.

%prep
%setup -q -n %{name}-%{version}
%patch -p1

%build
make 

%install
rm -rf $RPM_BUILD_ROOT;
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc
make DESTDIR=$RPM_BUILD_ROOT install 
install -d $RPM_BUILD_ROOT%{apache_serverroot}/cgi-bin
install -m 755 check.cgi $RPM_BUILD_ROOT%{apache_serverroot}/cgi-bin
install -m 644 check.conf $RPM_BUILD_ROOT%{apache_serverroot}/cgi-bin

%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%doc README THANKS README.SUSE
/usr/bin/*
%attr(755,root,root) %{apache_serverroot}/cgi-bin/check.cgi
%attr(644,root,root) %{apache_serverroot}/cgi-bin/check.conf
%config /etc/*

%changelog
