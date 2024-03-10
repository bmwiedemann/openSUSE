#
# spec file for package perl-Pod-Parser
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


%define cpan_name Pod-Parser
Name:           perl-Pod-Parser
Version:        1.670.0
Release:        0
%define cpan_version 1.67
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Modules for parsing/translating POD format documents
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAREKR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Pod::Cache)
Provides:       perl(Pod::Cache::Item)
Provides:       perl(Pod::Find) = %{version}
Provides:       perl(Pod::Hyperlink)
Provides:       perl(Pod::InputObjects) = %{version}
Provides:       perl(Pod::InputSource)
Provides:       perl(Pod::InteriorSequence)
Provides:       perl(Pod::List)
Provides:       perl(Pod::Paragraph)
Provides:       perl(Pod::ParseTree)
Provides:       perl(Pod::ParseUtils) = %{version}
Provides:       perl(Pod::Parser) = %{version}
Provides:       perl(Pod::PlainText) = 2.07
Provides:       perl(Pod::Select) = %{version}
%define         __perllib_provides /bin/true
%{perl_requires}

%description
*NOTE: This module is considered legacy; modern Perl releases (5.31.1 and
higher) are going to remove Pod-Parser from core and use Pod::Simple for
all things POD.*

*Pod::Parser* is a base class for creating POD filters and translators. It
handles most of the effort involved with parsing the POD sections from an
input stream, leaving subclasses free to be concerned only with performing
the actual translation of text.

*Pod::Parser* parses PODs, and makes method calls to handle the various
components of the POD. Subclasses of *Pod::Parser* override these methods
to translate the POD into whatever output format they desire.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc ANNOUNCE CHANGES README TODO

%changelog
