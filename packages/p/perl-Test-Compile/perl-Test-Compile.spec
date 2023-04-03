#
# spec file for package perl-Test-Compile
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


%define cpan_name Test-Compile
Name:           perl-Test-Compile
Version:        3.2.0
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Assert that your Perl files compile OK
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EG/EGILES/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter) >= 5.68
BuildRequires:  perl(Module::Build) >= 0.380000
BuildRequires:  perl(parent) >= 0.225
BuildRequires:  perl(version) >= 0.77
Requires:       perl(Exporter) >= 5.68
Requires:       perl(parent) >= 0.225
%{perl_requires}

%description
'Test::Compile' lets you check the whether your perl modules and scripts
compile properly, results are reported in standard 'Test::Simple' fashion.

The basic usage - as shown above, will locate your perl files and test that
they all compile.

Module authors can (and probably should) include the following in a
_t/00-compile.t_ file and have 'Test::Compile' automatically find and check
all Perl files in a module distribution:

    #!perl
    use strict;
    use warnings;
    use Test::Compile qw();

    my $test = Test::Compile->new();
    $test->all_files_ok();
    $test->done_testing();

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
%license LICENSE

%changelog
