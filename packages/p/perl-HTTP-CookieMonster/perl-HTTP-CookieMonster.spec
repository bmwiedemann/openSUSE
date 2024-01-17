#
# spec file for package perl-HTTP-CookieMonster
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


Name:           perl-HTTP-CookieMonster
Version:        0.11
Release:        0
%define cpan_name HTTP-CookieMonster
Summary:        Easy read/write access to your jar of HTTP::Cookies
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(Moo) >= 1.000003
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(URI::Escape)
Requires:       perl(HTTP::Cookies)
Requires:       perl(Moo) >= 1.000003
Requires:       perl(Safe::Isa)
Requires:       perl(Sub::Exporter)
Requires:       perl(URI::Escape)
%{perl_requires}

%description
This module was created because messing around with HTTP::Cookies is
non-trivial. HTTP::Cookies a very useful module, but using it is not always
as easy and clean as it could be. For instance, if you want to find a
particular cookie, you can't just ask for it by name.

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
%doc Changes CONTRIBUTORS examples README.md
%license LICENSE

%changelog
