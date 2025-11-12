#
# spec file for package perl-Test-Fatal
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


%define cpan_name Test-Fatal
Name:           perl-Test-Fatal
Version:        0.18.0
Release:        0
# 0.018 -> normalize -> 0.18.0
%define cpan_version 0.018
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Incredibly simple helpers for testing code with exceptions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Test::More) >= 0.65
BuildRequires:  perl(Try::Tiny) >= 0.70
Requires:       perl(Try::Tiny) >= 0.70
Provides:       perl(Test::Fatal) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Test::Fatal is an alternative to the popular Test::Exception. It does much
less, but should allow greater flexibility in testing exception-throwing
code with about the same amount of typing.

It exports one routine by default: 'exception'.

*Achtung!* 'exception' intentionally does not manipulate the call stack.
User-written test functions that use 'exception' must be careful to avoid
false positives if exceptions use stack traces that show arguments. For a
more magical approach involving globally overriding 'caller', see
Test::Exception.

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
%doc Changes examples README
%license LICENSE

%changelog
