#
# spec file for package perl-PPIx-QuoteLike
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


%define cpan_name PPIx-QuoteLike
Name:           perl-PPIx-QuoteLike
Version:        0.017
Release:        0
Summary:        Parse Perl string literals and string-literal-like things
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/W/WY/WYANT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PPI::Document) >= 1.117
BuildRequires:  perl(PPI::Dumper) >= 1.117
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(PPI::Document) >= 1.117
Requires:       perl(PPI::Dumper) >= 1.117
Requires:       perl(Readonly)
%{perl_requires}

%description
This Perl class parses Perl string literals and things that are reasonably
like string literals. Its real reason for being is to find interpolated
variables for Perl::Critic policies and similar code.

The parse is fairly straightforward, and a little poking around with
_eg/pqldump_ should show how it normally goes.

But there is at least one quote-like thing that probably needs some
explanation.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
