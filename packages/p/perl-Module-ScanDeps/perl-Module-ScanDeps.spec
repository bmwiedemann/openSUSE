#
# spec file for package perl-Module-ScanDeps
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Module-ScanDeps
Name:           perl-Module-ScanDeps
Version:        1.31
Release:        0
Summary:        Recursively scan Perl code for dependencies
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(version)
Requires:       perl(Module::Metadata)
Requires:       perl(version)
%{perl_requires}

%description
This module scans potential modules used by perl programs, and returns a
hash reference; its keys are the module names as appears in '%INC' (e.g.
'Test/More.pm'); the values are hash references with this structure:

    {
        file    => '/usr/local/lib/perl5/5.8.0/Test/More.pm',
        key     => 'Test/More.pm',
        type    => 'module',    # or 'autoload', 'data', 'shared'
        used_by => [ 'Test/Simple.pm', ... ],
        uses    => [ 'Test/Other.pm', ... ],
    }

One function, 'scan_deps', is exported by default. Other functions such as
('scan_line', 'scan_chunk', 'add_deps', 'path_to_inc_name') are exported
upon request.

Users of *App::Packer* may also use this module as the dependency-checking
frontend, by tweaking their _p2e.pl_ like below:

    use Module::ScanDeps;
    ...
    my $packer = App::Packer->new( frontend => 'Module::ScanDeps' );
    ...

Please see App::Packer::Frontend for detailed explanation on the structure
returned by 'get_files'.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc AUTHORS Changes README
%license LICENSE

%changelog
