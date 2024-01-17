#
# spec file for package perl-Test-File-Contents
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


%define cpan_name Test-File-Contents
Name:           perl-Test-File-Contents
Version:        0.242
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Test routines for examining the contents of files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Builder) >= 0.70
BuildRequires:  perl(Test::More) >= 0.70
BuildRequires:  perl(Text::Diff) >= 0.35
Requires:       perl(Test::Builder) >= 0.70
Requires:       perl(Text::Diff) >= 0.35
%{perl_requires}

%description
Got an app that generates files? Then you need to test those files to make
sure that their contents are correct. This module makes that easy. Use its
test functions to make sure that the contents of files are exactly what you
expect them to be.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
