#
# spec file for package perl-Test-CheckGitStatus
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


%define cpan_name Test-CheckGitStatus
Name:           perl-Test-CheckGitStatus
Version:        0.1.0
Release:        0
License:        MIT
Summary:        Check git status after every test
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(File::Which)
Requires:       perl(Test::More) >= 0.98
%{perl_requires}

%description
This module can be used to check if your git directory has any modified or
untracked files. You can use it in your unit tests, and it will check the
status after each test file.

By default it will not run the check, as this would be annoying during
development.

%prep
%autosetup  -n %{cpan_name}-v%{version} -p1

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
