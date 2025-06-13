#
# spec file for package perl-ExtUtils-MakeMaker-CPANfile
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


%define cpan_name ExtUtils-MakeMaker-CPANfile
Name:           perl-ExtUtils-MakeMaker-CPANfile
Version:        0.90.0
Release:        0
# 0.09 -> normalize -> 0.90.0
%define cpan_version 0.09
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Cpanfile support for EUMM
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Converter) >= 2.141170
BuildRequires:  perl(Module::CPANfile)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.76
Requires:       perl(CPAN::Meta::Converter) >= 2.141170
Requires:       perl(Module::CPANfile)
Requires:       perl(Test::More) >= 0.88
Requires:       perl(version) >= 0.76
Provides:       perl(ExtUtils::MakeMaker::CPANfile) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
ExtUtils::MakeMaker::CPANfile loads 'cpanfile' in your distribution and
modifies parameters for 'WriteMakefile' in your Makefile.PL. Just use it
instead of ExtUtils::MakeMaker (which should be loaded internally), and
prepare 'cpanfile'.

As of version 0.03, ExtUtils::MakeMaker::CPANfile also removes
WriteMakefile parameters that the installed version of ExtUtils::MakeMaker
doesn't know, to avoid warnings.

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
%doc Changes README.md
%license LICENSE

%changelog
