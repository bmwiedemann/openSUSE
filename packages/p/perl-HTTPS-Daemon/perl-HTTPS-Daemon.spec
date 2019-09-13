#
# spec file for package perl-HTTPS-Daemon (Version 1.04)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-HTTPS-Daemon
BuildRequires:  perl-IO-Socket-SSL
BuildRequires:  perl-macros
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Requires:       perl-IO-Socket-SSL perl-libwww-perl
AutoReqProv:    on
Summary:        a simple http server class with SSL support
Version:        1.04
Release:        54
Source:         HTTP-Daemon-SSL-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
HTTP::Daemon::SSL is a descendant of HTTP::Daemon that uses SSL sockets
(via IO::Socket::SSL) instead of cleartext sockets.  It also handles
SSL-specific problems, such as dealing with HTTP clients that attempt
to connect to it without using SSL.

%prep
%setup -n HTTP-Daemon-SSL-%{version}
# ---------------------------------------------------------------------------

%build
perl Makefile.PL
make %{?_smp_mflags}
rm -rf certs/.svn
#make test
# ---------------------------------------------------------------------------

%install
make DESTDIR=$RPM_BUILD_ROOT \
	 INSTALLMAN3DIR=$RPM_BUILD_ROOT/%{_mandir}/man3 \
	 install_vendor
%perl_process_packlist

%files
%defattr(-,root,root)
%{perl_vendorlib}/HTTP
%{perl_vendorarch}/auto/HTTP
%doc BUGS Changes MANIFEST README
%doc %{_mandir}/man3/*
%doc certs

%changelog
