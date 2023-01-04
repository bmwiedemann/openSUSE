#
# spec file for package perl-Mojolicious
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


%define cpan_name Mojolicious
Name:           perl-Mojolicious
Version:        9.31
Release:        0
License:        Artistic-2.0
Summary:        Real-time web framework
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Socket::IP) >= 0.37
BuildRequires:  perl(Sub::Util) >= 1.41
Requires:       perl(IO::Socket::IP) >= 0.37
Requires:       perl(Sub::Util) >= 1.41
%{perl_requires}

%description
An amazing real-time web framework built on top of the powerful Mojo web
development toolkit. With support for RESTful routes, plugins, commands,
Perl-ish templates, content negotiation, session management, form
validation, testing framework, static file server, 'CGI'/'PSGI' detection,
first class Unicode support and much more for you to discover.

Take a look at our excellent documentation in Mojolicious::Guides!

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
%doc Changes examples README.md
%license LICENSE

%changelog
