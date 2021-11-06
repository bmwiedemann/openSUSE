#
# spec file for package perl-RPC-XML
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name RPC-XML
Name:           perl-RPC-XML
Version:        0.82
Release:        0
Summary:        Set of classes for core data, message and XML handling
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJRAY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         RPC-XML-0.77-fixtest.dif
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.56
BuildRequires:  perl(HTTP::Daemon) >= 6.12
BuildRequires:  perl(HTTP::Message) >= 6.26
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(LWP) >= 6.51
BuildRequires:  perl(Module::Load) >= 0.36
BuildRequires:  perl(Scalar::Util) >= 1.55
BuildRequires:  perl(Test::More) >= 1.302183
BuildRequires:  perl(XML::Parser) >= 2.46
Requires:       perl(HTTP::Daemon) >= 6.12
Requires:       perl(HTTP::Message) >= 6.26
Requires:       perl(LWP) >= 6.51
Requires:       perl(Module::Load) >= 0.36
Requires:       perl(Scalar::Util) >= 1.55
Requires:       perl(XML::Parser) >= 2.46
Recommends:     perl(DateTime) >= 1.54
Recommends:     perl(DateTime::Format::ISO8601) >= 0.15
Recommends:     perl(XML::LibXML) >= 2.0206
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(HTTP::Daemon)
# MANUAL END

%description
The *RPC::XML* package is an implementation of the *XML-RPC* standard. The
package as a whole provides classes for data, for clients, for servers and
for parsers (based on the XML::Parser and XML::LibXML packages from CPAN).

This module provides a set of classes for creating values to pass to the
constructors for requests and responses. These are lightweight objects,
most of which are implemented as blessed scalar references so as to
associate specific type information with the value. Classes are also
provided for requests, responses and faults (errors).

This module does not actually provide any transport implementation or
server basis. For these, see RPC::XML::Client and RPC::XML::Server,
respectively.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog ChangeLog.xml README README.apache2

%changelog
