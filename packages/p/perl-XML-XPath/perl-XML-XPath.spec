#
# spec file for package perl-XML-XPath
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name XML-XPath
Name:           perl-XML-XPath
Version:        1.480.0
Release:        0
# 1.48 -> normalize -> 1.480.0
%define cpan_version 1.48
License:        Artistic-2.0
Summary:        Parse and evaluate XPath statements
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Path::Tiny) >= 0.76
BuildRequires:  perl(Scalar::Util) >= 1.45
BuildRequires:  perl(XML::Parser) >= 2.230
Requires:       perl(Scalar::Util) >= 1.45
Requires:       perl(XML::Parser) >= 2.230
Provides:       perl(XML::XPath) = %{version}
Provides:       perl(XML::XPath::Boolean) = %{version}
Provides:       perl(XML::XPath::Builder) = %{version}
Provides:       perl(XML::XPath::Expr) = %{version}
Provides:       perl(XML::XPath::Function) = %{version}
Provides:       perl(XML::XPath::Literal) = %{version}
Provides:       perl(XML::XPath::LocationPath) = %{version}
Provides:       perl(XML::XPath::Node) = %{version}
Provides:       perl(XML::XPath::Node::Attribute) = %{version}
Provides:       perl(XML::XPath::Node::AttributeImpl) = %{version}
Provides:       perl(XML::XPath::Node::Comment) = %{version}
Provides:       perl(XML::XPath::Node::Element) = %{version}
Provides:       perl(XML::XPath::Node::Namespace) = %{version}
Provides:       perl(XML::XPath::Node::PI) = %{version}
Provides:       perl(XML::XPath::Node::Text) = %{version}
Provides:       perl(XML::XPath::NodeSet) = %{version}
Provides:       perl(XML::XPath::Number) = %{version}
Provides:       perl(XML::XPath::Parser) = %{version}
Provides:       perl(XML::XPath::PerlSAX) = %{version}
Provides:       perl(XML::XPath::Root) = %{version}
Provides:       perl(XML::XPath::Step) = %{version}
Provides:       perl(XML::XPath::Variable) = %{version}
Provides:       perl(XML::XPath::XMLParser) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module aims to comply exactly to the XPath specification at
http://www.w3.org/TR/xpath and yet allow extensions to be added in the form
of functions.Modules such as XSLT and XPointer may need to do this as they
support functionality beyond XPath.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples README TODO
%license LICENSE

%changelog
