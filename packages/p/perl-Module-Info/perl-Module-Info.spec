#
# spec file for package perl-Module-Info
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Module-Info
Name:           perl-Module-Info
Version:        0.390.0
Release:        0
# 0.39 -> normalize -> 0.390.0
%define cpan_version 0.39
License:        SUSE-Public-Domain
Summary:        Information about Perl modules
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Utils) >= 0.27
Requires:       perl(B::Utils) >= 0.27
Provides:       perl(B::Module::Info) = %{version}
Provides:       perl(Module::Info)
Provides:       perl(Module::Info::Safe)
Provides:       perl(Module::Info::Unsafe)
Provides:       perl(Module::Info::_version)
%undefine       __perllib_provides
%{perl_requires}

%description
Module::Info gives you information about Perl modules *without actually
loading the module*. It actually isn't specific to modules and should work
on any perl code.

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
%doc Changes README

%changelog
