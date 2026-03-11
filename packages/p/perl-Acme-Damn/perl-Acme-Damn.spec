#
# spec file for package perl-Acme-Damn
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Acme-Damn
Name:           perl-Acme-Damn
Version:        0.90.0
Release:        0
# 0.09 -> normalize -> 0.90.0
%define cpan_version 0.09
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        'Unbless' Perl objects
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRTASTIC/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Exception)
Provides:       perl(Acme::Damn) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
*Acme::Damn* provides a single routine, *damn()*, which takes a blessed
reference (a Perl object), and _unblesses_ it, to return the original
reference.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README

%changelog
