#
# spec file for package perl-Data-Peek
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Data-Peek
Version:        0.48
Release:        0
%define cpan_name Data-Peek
Summary:        Collection of low-level debug facilities
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Test::NoWarnings)
Recommends:     perl(Data::Dumper) >= 2.167
Recommends:     perl(Perl::Tidy)
Recommends:     perl(Test::More) >= 1.302125
%{perl_requires}

%description
Data::Peek started off as 'DDumper' being a wrapper module over
Data::Dumper, but grew out to be a set of low-level data introspection
utilities that no other module provided yet, using the lowest level of the
perl internals API as possible.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog CONTRIBUTING.md examples README

%changelog
