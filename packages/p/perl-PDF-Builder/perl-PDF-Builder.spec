#
# spec file for package perl-PDF-Builder
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


%define cpan_name PDF-Builder
Name:           perl-PDF-Builder
Version:        3.025
Release:        0
License:        LGPL-2.1-or-later
Summary:        Facilitates the creation and modification of PDF files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMPERRY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Zlib) >= 1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.66
BuildRequires:  perl(Font::TTF) >= 1.04
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle) >= 1
Requires:       perl(Compress::Zlib) >= 1
Requires:       perl(Font::TTF) >= 1.04
%{perl_requires}

%description
Facilitates the creation and modification of PDF files

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
%doc Changes CONTRIBUTING.md docs examples README.md
%license LICENSE

%changelog
