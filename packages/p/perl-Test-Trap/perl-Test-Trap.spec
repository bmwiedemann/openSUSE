#
# spec file for package perl-Test-Trap
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


%define cpan_name Test-Trap
Name:           perl-Test-Trap
Version:        0.3.5
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Trap exit codes, exceptions, output, etc
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EB/EBHANSSEN/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Tester) >= 0.107
BuildRequires:  perl(version)
Requires:       perl(Data::Dump)
Requires:       perl(Test::Tester) >= 0.107
Requires:       perl(version)
%{perl_requires}

%description
Primarily (but not exclusively) for use in test scripts: A block eval on
steroids, configurable and extensible, but by default trapping (Perl)
STDOUT, STDERR, warnings, exceptions, would-be exit codes, and return
values from boxed blocks of test code.

The values collected by the latest trap can then be queried or tested
through a special trap object.

%prep
%autosetup  -n %{cpan_name}-v%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
