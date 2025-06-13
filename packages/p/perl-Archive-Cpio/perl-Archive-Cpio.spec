#
# spec file for package perl-Archive-Cpio
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


%define cpan_name Archive-Cpio
Name:           perl-Archive-Cpio
Version:        0.100.0
Release:        0
# 0.10 -> normalize -> 0.100.0
%define cpan_version 0.10
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Module for manipulations of cpio archives
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PI/PIXEL/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        LICENSE
Source2:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Archive::Cpio) = %{version}
Provides:       perl(Archive::Cpio::Common)
Provides:       perl(Archive::Cpio::File)
Provides:       perl(Archive::Cpio::FileHandle_with_pushback)
Provides:       perl(Archive::Cpio::NewAscii)
Provides:       perl(Archive::Cpio::ODC)
Provides:       perl(Archive::Cpio::OldBinary)
%undefine       __perllib_provides
%{perl_requires}

%description
Archive::Cpio provides a few functions to read and write cpio files.

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
%doc Changes

%changelog
