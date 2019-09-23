#
# spec file for package perl-RPC-XML
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-RPC-XML
Version:        0.80
Release:        0
%define cpan_name RPC-XML
Summary:        Set of classes for core data, message and XML handling
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJRAY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         RPC-XML-0.77-fixtest.dif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(LWP) >= 5.834
BuildRequires:  perl(Module::Load) >= 0.24
BuildRequires:  perl(Scalar::Util) >= 1.33
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(XML::Parser) >= 2.31
Requires:       perl(LWP) >= 5.834
Requires:       perl(Module::Load) >= 0.24
Requires:       perl(Scalar::Util) >= 1.33
Requires:       perl(Test::More) >= 0.94
Requires:       perl(XML::Parser) >= 2.31
Recommends:     perl(Compress::Raw::Zlib) >= 2.063
Recommends:     perl(DateTime) >= 0.70
Recommends:     perl(DateTime::Format::ISO8601) >= 0.07
Recommends:     perl(XML::LibXML) >= 1.85
%{perl_requires}

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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog ChangeLog.xml README README.apache2

%changelog
