#
# spec file for package perl-Test-WWW-Mechanize
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Test-WWW-Mechanize
Name:           perl-Test-WWW-Mechanize
Version:        1.60
Release:        0
License:        Artistic-2.0
Summary:        Testing-specific WWW::Mechanize subclass
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Assert::More) >= 1.16
BuildRequires:  perl(HTML::Form)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTTP::Message) >= 6.29
BuildRequires:  perl(HTTP::Server::Simple) >= 0.42
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(LWP) >= 6.02
BuildRequires:  perl(Test::Builder::Tester) >= 1.09
BuildRequires:  perl(Test::LongString) >= 0.15
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(URI::file)
BuildRequires:  perl(WWW::Mechanize) >= 1.68
BuildRequires:  perl(parent)
Requires:       perl(Carp::Assert::More) >= 1.16
Requires:       perl(HTML::Form)
Requires:       perl(HTML::TokeParser)
Requires:       perl(HTTP::Message) >= 6.29
Requires:       perl(LWP) >= 6.02
Requires:       perl(Test::LongString) >= 0.15
Requires:       perl(WWW::Mechanize) >= 1.68
Requires:       perl(parent)
%{perl_requires}

%description
Testing-specific WWW::Mechanize subclass

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README.md

%changelog
