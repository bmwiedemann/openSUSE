#
# spec file for package perl-File-Rename
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


%define cpan_name File-Rename
Name:           perl-File-Rename
Version:        1.31
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for renaming multiple files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RM/RMBARKER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-OPENSUSE
Patch0:         change-command-name.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.400000
%{perl_requires}

%description
* 'rename( FILES, CODE [, VERBOSE])'

rename FILES using CODE, if FILES is empty read list of files from stdin

* 'rename_files( CODE, VERBOSE, FILES)'

rename FILES using CODE

* 'rename_list( CODE, VERBOSE, HANDLE [, FILENAME])'

rename a list of file read from HANDLE, using CODE

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING examples README

%changelog
