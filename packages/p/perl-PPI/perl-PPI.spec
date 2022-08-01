#
# spec file for package perl-PPI
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


%define cpan_name PPI
Name:           perl-PPI
Version:        1.276
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parse, Analyze and Manipulate Perl (without perl)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Inspector) >= 1.22
BuildRequires:  perl(Clone) >= 0.30
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(Storable) >= 2.17
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Object) >= 0.07
BuildRequires:  perl(Test::SubCalls) >= 1.07
Requires:       perl(Clone) >= 0.30
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(Storable) >= 2.17
Requires:       perl(Task::Weaken)
%{perl_requires}

%description
Parse, Analyze and Manipulate Perl (without perl)

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
%doc Changes dev_notes.txt README
%license LICENSE

%changelog
