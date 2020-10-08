#
# spec file for package perl-XML-Writer
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


Name:           perl-XML-Writer
Version:        0.900
Release:        0
#Upstream: SUSE-Public-Domain
%define cpan_name XML-Writer
Summary:        Perl extension for writing XML documents
License:        MIT
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JOSEPHW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
XML::Writer is a helper module for Perl programs that write an XML
document. The module handles all escaping for attribute values and
character data and constructs different types of markup, such as tags,
comments, and processing instructions.

By default, the module performs several well-formedness checks to catch
errors during output. This behaviour can be extremely useful during
development and debugging, but it can be turned off for production-grade
code.

The module can operate either in regular mode in or Namespace processing
mode. In Namespace mode, the module will generate Namespace Declarations
itself, and will perform additional checks on the output.

Additional support is available for a simplified data mode with no mixed
content: newlines are automatically inserted around elements and elements
can optionally be indented based as their nesting level.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples README TODO
%license LICENSE

%changelog
