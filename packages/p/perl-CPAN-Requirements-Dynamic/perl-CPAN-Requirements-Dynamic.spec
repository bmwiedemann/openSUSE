#
# spec file for package perl-CPAN-Requirements-Dynamic
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


%define cpan_name CPAN-Requirements-Dynamic
Name:           perl-CPAN-Requirements-Dynamic
Version:        0.1.0
Release:        0
# 0.001 -> normalize -> 0.1.0
%define cpan_version 0.001
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Dynamic prerequisites in meta files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(CPAN::Meta::Requirements::Range)
BuildRequires:  perl(ExtUtils::Config)
BuildRequires:  perl(ExtUtils::HasCompiler)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Perl::OSType)
Requires:       perl(CPAN::Meta::Prereqs)
Requires:       perl(CPAN::Meta::Requirements::Range)
Requires:       perl(ExtUtils::Config)
Requires:       perl(ExtUtils::HasCompiler)
Requires:       perl(IPC::Cmd)
Requires:       perl(Module::Metadata)
Requires:       perl(Parse::CPAN::Meta)
Requires:       perl(Perl::OSType)
Provides:       perl(CPAN::Requirements::Dynamic) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module implements a format for describing dynamic prerequisites of a
distribution.

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
%license LICENSE

%changelog
