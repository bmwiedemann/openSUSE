#
# spec file for package perl-App-Spec
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name App-Spec
Name:           perl-App-Spec
Version:        0.15.0
Release:        0
# v0.15.0 -> normalize -> 0.15.0
%define cpan_version v0.15.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Specification for commandline app
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Text::Table)
BuildRequires:  perl(YAML::PP) >= 0.15.0
Requires:       perl(List::MoreUtils)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Module::Runtime)
Requires:       perl(Moo)
Requires:       perl(Moo::Role)
Requires:       perl(Ref::Util)
Requires:       perl(Text::Table)
Requires:       perl(YAML::PP) >= 0.15.0
%{perl_requires}

%description
Specification for commandline app

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CONTRIBUTING.md examples README README.md
%license LICENSE

%changelog
