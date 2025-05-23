#
# spec file for package perl-File-Copy-Recursive
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


%define cpan_name File-Copy-Recursive
Name:           perl-File-Copy-Recursive
Version:        0.450.0
Release:        0
# 0.45 -> normalize -> 0.450.0
%define cpan_version 0.45
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for recursively copying files and directories
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMUEY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)
Provides:       perl(File::Copy::Recursive) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module copies and moves directories recursively (or single files,
well... singley) to an optional depth and attempts to preserve each file or
directory's mode.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README README.md

%changelog
