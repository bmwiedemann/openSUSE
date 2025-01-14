#
# spec file for package perl-Test-Manifest
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


%define cpan_name Test-Manifest
Name:           perl-Test-Manifest
Version:        2.25.0
Release:        0
# 2.025 -> normalize -> 2.25.0
%define cpan_version 2.025
License:        Artistic-2.0
Summary:        Interact with a t/test_manifest file
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(Test::More) >= 1
Provides:       perl(Test::Manifest) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'Test::Harness' assumes that you want to run all of the _.t_ files in the
_t/_ directory in ASCII-betical order during 'make test' or './Build test'
unless you say otherwise. This leads to some interesting naming schemes for
test files to get them in the desired order. These interesting names ossify
when they get into source control, and get even more interesting as more
tests show up.

'Test::Manifest' overrides the default test file order. Instead of running
all of the _t/*.t_ files in ASCII-betical order, it looks in the
_t/test_manifest_ file to find out which tests you want to run and the
order in which you want to run them. It constructs the right value for the
build system to do the right thing.

In _t/test_manifest_, simply list the tests that you want to run. Their
order in the file is the order in which they run. You can comment lines
with a '#', just like in Perl, and 'Test::Manifest' will strip leading and
trailing whitespace from each line. It also checks that the specified file
is actually in the _t/_ directory. If the file does not exist, it does not
put its name in the list of test files to run and it will issue a warning.

Optionally, you can add a number after the test name in test_manifest to
define sets of tests. See 'get_t_files' for more information.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes examples SECURITY.md test_manifest test_manifest_levels test_manifest_with_include
%license LICENSE

%changelog
