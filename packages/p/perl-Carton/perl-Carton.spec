#
# spec file for package perl-Carton
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


%define cpan_name Carton
Name:           perl-Carton
Version:        1.0.35
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl module dependency manager (aka Bundler for Perl)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta) >= 2.120921
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121000
BuildRequires:  perl(Class::Tiny) >= 1.001
BuildRequires:  perl(Getopt::Long) >= 2.39
BuildRequires:  perl(JSON::PP) >= 2.27300
BuildRequires:  perl(Menlo::CLI::Compat) >= 1.9018
BuildRequires:  perl(Module::CPANfile) >= 0.9031
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Path::Tiny) >= 0.033
BuildRequires:  perl(Try::Tiny) >= 0.09
BuildRequires:  perl(parent) >= 0.223
BuildRequires:  perl(version) >= 0.77
Requires:       perl(CPAN::Meta) >= 2.120921
Requires:       perl(CPAN::Meta::Requirements) >= 2.121000
Requires:       perl(Class::Tiny) >= 1.001
Requires:       perl(Getopt::Long) >= 2.39
Requires:       perl(JSON::PP) >= 2.27300
Requires:       perl(Menlo::CLI::Compat) >= 1.9018
Requires:       perl(Module::CPANfile) >= 0.9031
Requires:       perl(Module::CoreList)
Requires:       perl(Path::Tiny) >= 0.033
Requires:       perl(Try::Tiny) >= 0.09
Requires:       perl(parent) >= 0.223
Recommends:     perl(App::FatPacker) >= 0.009018
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
%autosetup  -n %{cpan_name}-v%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
