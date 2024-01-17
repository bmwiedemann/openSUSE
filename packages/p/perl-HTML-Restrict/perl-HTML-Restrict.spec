#
# spec file for package perl-HTML-Restrict
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name HTML-Restrict
Name:           perl-HTML-Restrict
Version:        3.0.2
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Strip unwanted HTML tags and attributes
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moo) >= 1.002000
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Type::Tiny) >= 1.002001
BuildRequires:  perl(Types::Standard) >= 1.000001
BuildRequires:  perl(URI)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(version)
Requires:       perl(Data::Dump)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::Parser)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Moo) >= 1.002000
Requires:       perl(Sub::Quote)
Requires:       perl(Type::Tiny) >= 1.002001
Requires:       perl(Types::Standard) >= 1.000001
Requires:       perl(URI)
Requires:       perl(namespace::clean)
Requires:       perl(version)
%{perl_requires}

%description
This module uses HTML::Parser to strip HTML from text in a restrictive
manner. By default all HTML is restricted. You may alter the default
behaviour by supplying your own tag rules.

%prep
%autosetup  -n %{cpan_name}-v%{version}

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
%doc Changes CONTRIBUTORS examples README.md
%license LICENSE

%changelog
