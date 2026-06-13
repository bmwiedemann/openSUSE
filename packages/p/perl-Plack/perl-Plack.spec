#
# spec file for package perl-Plack
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Plack
Name:           perl-Plack
Version:        1.0054
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Apache::LogFormat::Compiler) >= 0.330
BuildRequires:  perl(Cookie::Baker) >= 0.70
BuildRequires:  perl(Devel::StackTrace) >= 1.230
BuildRequires:  perl(Devel::StackTrace::AsHTML) >= 0.110
BuildRequires:  perl(File::ShareDir) >= 1.0
BuildRequires:  perl(File::ShareDir::Install) >= 0.60
BuildRequires:  perl(Filesys::Notify::Simple)
BuildRequires:  perl(HTTP::Entity::Parser) >= 0.250
BuildRequires:  perl(HTTP::Headers::Fast) >= 0.180
BuildRequires:  perl(HTTP::Message) >= 5.814
BuildRequires:  perl(HTTP::Tiny) >= 0.034
BuildRequires:  perl(Hash::MultiValue) >= 0.50
BuildRequires:  perl(Pod::Usage) >= 1.36
BuildRequires:  perl(Stream::Buffered) >= 0.20
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP) >= 2.150
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.590
BuildRequires:  perl(WWW::Form::UrlEncoded) >= 0.230
BuildRequires:  perl(parent)
Requires:       perl(Apache::LogFormat::Compiler) >= 0.330
Requires:       perl(Cookie::Baker) >= 0.70
Requires:       perl(Devel::StackTrace) >= 1.230
Requires:       perl(Devel::StackTrace::AsHTML) >= 0.110
Requires:       perl(File::ShareDir) >= 1.0
Requires:       perl(Filesys::Notify::Simple)
Requires:       perl(HTTP::Entity::Parser) >= 0.250
Requires:       perl(HTTP::Headers::Fast) >= 0.180
Requires:       perl(HTTP::Message) >= 5.814
Requires:       perl(HTTP::Tiny) >= 0.034
Requires:       perl(Hash::MultiValue) >= 0.50
Requires:       perl(Pod::Usage) >= 1.36
Requires:       perl(Stream::Buffered) >= 0.20
Requires:       perl(Test::TCP) >= 2.150
Requires:       perl(Try::Tiny)
Requires:       perl(URI) >= 1.590
Requires:       perl(WWW::Form::UrlEncoded) >= 0.230
Requires:       perl(parent)
%{perl_requires}

%description
Plack is a set of tools for using the PSGI stack. It contains middleware
components, a reference server and utilities for Web application
frameworks. Plack is like Ruby's Rack or Python's Paste for WSGI.

See PSGI for the PSGI specification and PSGI::FAQ to know what PSGI and
Plack are and why we need them.

%prep
%autosetup -n %{cpan_name}-%{version} -p1

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
%doc Changes README
%license LICENSE

%changelog
