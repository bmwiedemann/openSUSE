#
# spec file for package perl-Devel-Symdump
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Devel-Symdump
Name:           perl-Devel-Symdump
Version:        2.180.0
Release:        0
# 2.18 -> normalize -> 2.180.0
%define cpan_version 2.18
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Dump symbol names or the symbol table
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Zlib)
Requires:       perl(Compress::Zlib)
Provides:       perl(Devel::Symdump) = %{version}
Provides:       perl(Devel::Symdump::Export)
%undefine       __perllib_provides
%{perl_requires}

%description
This little package serves to access the symbol table of perl.

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
