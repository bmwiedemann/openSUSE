#
# spec file for package perl-Module-Build-Prereqs-FromCPANfile
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


%define cpan_name Module-Build-Prereqs-FromCPANfile
Name:           perl-Module-Build-Prereqs-FromCPANfile
Version:        0.20.0
Release:        0
# 0.02 -> normalize -> 0.20.0
%define cpan_version 0.02
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Construct prereq parameters of Module::Build from cpanfile
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOSHIOITO/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.132830
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Module::CPANfile) >= 1.0000
BuildRequires:  perl(version) >= 0.80
Requires:       perl(CPAN::Meta::Prereqs) >= 2.132830
Requires:       perl(Module::CPANfile) >= 1.0000
Requires:       perl(version) >= 0.80
Provides:       perl(Module::Build::Prereqs::FromCPANfile) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Module::Build) >= 0.4004
%{perl_requires}

%description
This simple module reads cpanfile and converts its content into valid
prereq parameters for 'new()' method of Module::Build.

Currently it does not support "optional features" specification (See
cpanfile/feature).

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
