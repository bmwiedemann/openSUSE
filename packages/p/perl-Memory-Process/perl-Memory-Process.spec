#
# spec file for package perl-Memory-Process
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


%define cpan_name Memory-Process
Name:           perl-Memory-Process
Version:        0.60.0
Release:        0
# 0.06 -> normalize -> 0.60.0
%define cpan_version 0.06
License:        BSD-3-Clause
Summary:        Memory process reporting
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKIM/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(Memory::Usage)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(Memory::Usage)
Requires:       perl(Readonly)
Provides:       perl(Memory::Process) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Memory process reporting.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README
%license LICENSE

%changelog
