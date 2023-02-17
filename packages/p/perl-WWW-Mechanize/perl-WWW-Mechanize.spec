#
# spec file for package perl-WWW-Mechanize
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


%define cpan_name WWW-Mechanize
Name:           perl-WWW-Mechanize
Version:        2.16
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Handy web browsing in a Perl object
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIMBABQUE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Form) >= 6.08
BuildRequires:  perl(HTML::HeadParser)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTML::TreeBuilder) >= 5
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Daemon) >= 6.12
BuildRequires:  perl(HTTP::Request) >= 1.30
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Memory::Cycle) >= 1.06
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings) >= 1.04
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Taint) >= 1.08
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(URI::file)
Requires:       perl(HTML::Form) >= 6.08
Requires:       perl(HTML::HeadParser)
Requires:       perl(HTML::TokeParser)
Requires:       perl(HTML::TreeBuilder) >= 5
Requires:       perl(HTTP::Cookies)
Requires:       perl(HTTP::Request) >= 1.30
Requires:       perl(HTTP::Request::Common)
Requires:       perl(LWP::UserAgent)
Requires:       perl(URI::URL)
Requires:       perl(URI::file)
Recommends:     perl(Compress::Zlib)
%{perl_requires}

%description
'WWW::Mechanize', or Mech for short, is a Perl module for stateful
programmatic web browsing, used for automating interaction with websites.

Features include:

* All HTTP methods
* High-level hyperlink and HTML form support, without having to parse
  HTML yourself
* SSL support
* Automatic cookies
* Custom HTTP headers
* Automatic handling of redirections
* Proxies
* HTTP authentication

Mech is well suited for use in testing web applications. If you use one of
the Test::*, like Test::HTML::Lint modules, you can check the fetched
content and use that as input to a test call.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes CONTRIBUTORS README.md
%license LICENSE

%changelog
