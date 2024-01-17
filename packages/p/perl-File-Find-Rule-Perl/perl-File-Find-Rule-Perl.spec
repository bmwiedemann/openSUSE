#
# spec file for package perl-File-Find-Rule-Perl
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


%define cpan_name File-Find-Rule-Perl
Name:           perl-File-Find-Rule-Perl
Version:        1.16
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Common rules for searching for Perl things
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Find::Rule) >= 0.20
BuildRequires:  perl(Params::Util) >= 0.38
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.38
Requires:       perl(File::Find::Rule) >= 0.20
Requires:       perl(Params::Util) >= 0.38
Requires:       perl(Parse::CPAN::Meta) >= 1.38
%{perl_requires}

%description
I write a lot of things that muck with Perl files. And it always annoyed me
that finding "perl files" requires a moderately complex File::Find::Rule
pattern.

*File::Find::Rule::Perl* provides methods for finding various types
Perl-related files, or replicating search queries run on a distribution in
various parts of the CPAN ecosystem.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
# MANUAL no testing (broken within build env)
#make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes

%changelog
