#
# spec file for package perl-App-Rad
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


%define cpan_name App-Rad
Name:           perl-App-Rad
Version:        1.50.0
Release:        0
# 1.05 -> normalize -> 1.50.0
%define cpan_version 1.05
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Framework to facilitate creation of command line applications
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GARU/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Getopt::Long) >= 2.36
Requires:       perl(Getopt::Long) >= 2.36
Provides:       perl(App::Rad) = %{version}
Provides:       perl(App::Rad::Config)
Provides:       perl(App::Rad::Exclude) = 0.10.0
Provides:       perl(App::Rad::Help) = 0.30.0
Provides:       perl(App::Rad::Include) = 0.10.0
%undefine       __perllib_provides
%{perl_requires}

%description
App::Rad is a framework for developing
command-line applications. It can transform Perl _one-liners_
into subroutines than can be called by the user of your
program.

It also provides an interface for common command-line
tasks.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
