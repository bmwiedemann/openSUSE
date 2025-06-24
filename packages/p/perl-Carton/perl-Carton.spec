#
# spec file for package perl-Carton
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


%define cpan_name Carton
Name:           perl-Carton
Version:        1.0.35
Release:        0
# v1.0.35 -> normalize -> 1.0.35
%define cpan_version v1.0.35
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl module dependency manager (aka Bundler for Perl)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta) >= 2.120921
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(Class::Tiny) >= 1.1
BuildRequires:  perl(Getopt::Long) >= 2.39
BuildRequires:  perl(JSON::PP) >= 2.27
BuildRequires:  perl(Menlo::CLI::Compat) >= 1.901.800
BuildRequires:  perl(Module::CPANfile) >= 0.903.100
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Path::Tiny) >= 0.33
BuildRequires:  perl(Try::Tiny) >= 0.90
BuildRequires:  perl(parent) >= 0.223
BuildRequires:  perl(version) >= 0.77
Requires:       perl(CPAN::Meta) >= 2.120921
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(Class::Tiny) >= 1.1
Requires:       perl(Getopt::Long) >= 2.39
Requires:       perl(JSON::PP) >= 2.27
Requires:       perl(Menlo::CLI::Compat) >= 1.901.800
Requires:       perl(Module::CPANfile) >= 0.903.100
Requires:       perl(Module::CoreList)
Requires:       perl(Path::Tiny) >= 0.33
Requires:       perl(Try::Tiny) >= 0.90
Requires:       perl(parent) >= 0.223
Recommends:     perl(App::FatPacker) >= 0.9.18
Recommends:     perl(File::pushd)
%{perl_requires}

%description
carton is a command line tool to track the Perl module dependencies for
your Perl application. Dependencies are declared using cpanfile format, and
the managed dependencies are tracked in a _cpanfile.snapshot_ file, which
is meant to be version controlled, and the snapshot file allows other
developers of your application will have the exact same versions of the
modules.

For 'cpanfile' syntax, see cpanfile documentation.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
