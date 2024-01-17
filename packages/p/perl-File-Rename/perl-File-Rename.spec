#
# spec file for package perl-File-Rename
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name File-Rename
Name:           perl-File-Rename
Version:        2.20.0
Release:        0
%define cpan_version 2.02
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for renaming multiple files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RM/RMBARKER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-OPENSUSE
Patch0:         change-command-name.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.36
# needed for tests
BuildRequires:  perl(Pod::Parser)
Provides:       perl(File::Rename) = %{version}
Provides:       perl(File::Rename::Options) = 2.10.0
Provides:       perl(File::Rename::Unicode) = 1.30
%define         __perllib_provides /bin/true
%{perl_requires}

%description
Perl extension for renaming multiple files

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING examples README

%changelog
