#
# spec file for package perl-Data-Random
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


%define cpan_name Data-Random
Name:           perl-Data-Random
Version:        0.140.0
Release:        0
# 0.14 -> normalize -> 0.140.0
%define cpan_version 0.14
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl module to generate random data
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BA/BAREFOOT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::ShareDir::Install) >= 0.60
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::Piece) >= 1.16
Requires:       perl(Time::Piece) >= 1.16
Provides:       perl(Data::Random) = %{version}
Provides:       perl(Data::Random::WordList) = %{version}
%undefine       __perllib_provides
Recommends:     perl(GD)
%{perl_requires}

%description
A module used to generate random data. Useful mostly for test programs.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
# MANUAL END

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
