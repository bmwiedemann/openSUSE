#
# spec file for package perl-Memory-Usage
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


%define cpan_name Memory-Usage
Name:           perl-Memory-Usage
Version:        0.201.0
Release:        0
# 0.201 -> normalize -> 0.201.0
%define cpan_version 0.201
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tools to determine actual memory usage
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DONEILL/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
Provides:       perl(Memory::Usage) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module lets you attempt to measure, from your operating system's
perspective, how much memory a process is using at any given time.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes README

%changelog
