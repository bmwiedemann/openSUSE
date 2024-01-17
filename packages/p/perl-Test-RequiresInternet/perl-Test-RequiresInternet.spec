#
# spec file for package perl-Test-RequiresInternet
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-RequiresInternet
Version:        0.05
Release:        0
%define cpan_name Test-RequiresInternet
Summary:        Easily test network connectivity
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-RequiresInternet/
Source0:        http://www.cpan.org/authors/id/M/MA/MALLEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module is intended to easily test network connectivity before
functional tests begin to non-local Internet resources. It does not require
any modules beyond those supplied in core Perl.

If you do not specify a host/port pair, then the module defaults to using
'www.google.com' on port '80'.

You may optionally specify the port by its name, as in 'http' or 'ldap'. If
you do this, the test module will attempt to look up the port number using
'getservbyname'.

If you do specify a host and port, they must be specified in *pairs*. It is
a fatal error to omit one or the other.

If the environment variable 'NO_NETWORK_TESTING' is set, then the tests
will be skipped without attempting any socket connections.

If the sockets cannot connect to the specified hosts and ports, the
exception is caught, reported and the tests skipped.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
