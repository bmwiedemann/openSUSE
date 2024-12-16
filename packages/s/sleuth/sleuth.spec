#
# spec file for package sleuth
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


Name:           sleuth
Version:        1.4.4
Release:        0
Summary:        Perl script for easy checking (DNS, common errors and etc.)
License:        GPL-2.0-or-later
Group:          Productivity/Networking/DNS/Utilities
URL:            ftp://atrey.karlin.mff.cuni.cz/pub/local/mj/net/
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}.diff
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  libapr-util1-devel
BuildRequires:  pcre-devel
Requires:       perl-Net-DNS
BuildArch:      noarch

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
%autosetup -p1

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT;
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
%make_install
install -d %{buildroot}%{apache_serverroot}/cgi-bin
install -m 755 check.cgi %{buildroot}%{apache_serverroot}/cgi-bin
install -m 644 check.conf %{buildroot}%{apache_serverroot}/cgi-bin

%files
%doc README THANKS README.SUSE
%{_bindir}/*
%dir %{apache_serverroot}/cgi-bin/
%attr(755,root,root) %{apache_serverroot}/cgi-bin/check.cgi
%attr(644,root,root) %{apache_serverroot}/cgi-bin/check.conf
%config %{_sysconfdir}/*

%changelog
