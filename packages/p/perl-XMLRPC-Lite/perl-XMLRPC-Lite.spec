#
# spec file for package perl-XMLRPC-Lite
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-XMLRPC-Lite
Version:        0.717
Release:        0
%define cpan_name XMLRPC-Lite
Summary:        client and server implementation of XML-RPC protocol
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XMLRPC-Lite/
Source:         http://www.cpan.org/authors/id/P/PH/PHRED/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(SOAP::Lite) >= 0.716
BuildRequires:  perl(SOAP::Transport::TCP) >= 0.715
Requires:       perl(SOAP::Lite) >= 0.716
Requires:       perl(SOAP::Transport::TCP) >= 0.715
%{perl_requires}

%description
XMLRPC::Lite is a Perl modules which provides a simple nterface to the
XML-RPC protocol both on client and server side. Based on SOAP::Lite
module, it gives you access to all features and transports available in
that module.

See _t/26-xmlrpc.t_ for client examples and _examples/XMLRPC/*_ for server
implementations.

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
%doc Changes README

%changelog
