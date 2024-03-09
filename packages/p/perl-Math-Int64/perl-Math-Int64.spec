#
# spec file for package perl-Math-Int64
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


%define cpan_name Math-Int64
Name:           perl-Math-Int64
Version:        0.570.0
Release:        0
%define cpan_version 0.57
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Manipulate 64 bits integers in Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
Provides:       perl(Math::Int64) = %{version}
Provides:       perl(Math::Int64::die_on_overflow)
Provides:       perl(Math::Int64::native_if_available)
Provides:       perl(Math::UInt64)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
Requires:       perl-base = %{perl_version}
# MANUAL END

%description
This module adds support for 64 bit integers, signed and unsigned, to Perl.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc c_api.decl Changes examples README.md
%license COPYING

%changelog
