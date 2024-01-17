#
# spec file for package perl-Data-Peek
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


%define cpan_name Data-Peek
Name:           perl-Data-Peek
Version:        0.52
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Modified and extended debugging facilities
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Test::Warnings)
Requires:       perl(Test::More) >= 0.9
Requires:       perl(Test::Warnings)
Recommends:     perl(Data::Dumper) >= 2.184
Recommends:     perl(Perl::Tidy)
%{perl_requires}

%description
Data::Peek started off as 'DDumper' being a wrapper module over
Data::Dumper, but grew out to be a set of low-level data introspection
utilities that no other module provided yet, using the lowest level of the
perl internals API as possible.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog CONTRIBUTING.md examples README

%changelog
