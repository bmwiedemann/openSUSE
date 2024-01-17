#
# spec file for package perl-List-SomeUtils
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


%define cpan_name List-SomeUtils
Name:           perl-List-SomeUtils
Version:        0.59
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Provide the stuff missing in List::Util
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::SomeUtils::XS) >= 0.54
BuildRequires:  perl(Module::Implementation) >= 0.04
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(List::SomeUtils::XS) >= 0.54
Requires:       perl(Module::Implementation) >= 0.04
%{perl_requires}

%description
*List::SomeUtils* provides some trivial but commonly needed functionality
on lists which is not going to go into List::Util.

All of the below functions are implementable in only a couple of lines of
Perl code. Using the functions from this module however should give
slightly better performance as everything is implemented in C. The
pure-Perl implementation of these functions only serves as a fallback in
case the C portions of this module couldn't be compiled on this machine.

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
