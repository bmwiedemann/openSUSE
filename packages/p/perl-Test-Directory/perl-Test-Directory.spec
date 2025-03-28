#
# spec file for package perl-Test-Directory
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


%define cpan_name Test-Directory
Name:           perl-Test-Directory
Version:        0.052
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for maintaining test directories
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SANBEG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Exception)
%{perl_requires}

%description
Testing code can involve making sure that files are created and deleted as
expected. Doing this manually can be error prone, as it's easy to forget a
file, or miss that some unexpected file was added. This module simplifies
maintaining test directories by tracking their status as they are modified
or tested with this API, making it simple to test both individual files, as
well as to verify that there are no missing or unknown files.

The idea is to use this API to create a temporary directory and populate an
initial set of files. Then, whenever something in the directory is changes,
use the test methods to verify that the change happened as expected. At any
time, it is simple to verify that the contents of the directory are exactly
as expected.

Test::Directory implements an object-oriented interface for managing test
directories. It tracks which files it knows about (by creating or testing
them via its API), and can report if any files were missing or unexpectedly
added.

There are two flavors of methods for interacting with the directory.
_Utility_ methods simply return a value (i.e. the number of files/errors)
with no output, while the _Test_ functions use Test::Builder to produce the
approriate test results and diagnostics for the test harness.

The directory will be automatically cleaned up when the object goes out of
scope; see the _clean_ method below for details.

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

%changelog
