#
# spec file for package perl-Data-Integer
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


%define cpan_name Data-Integer
Name:           perl-Data-Integer
Version:        0.7.0
Release:        0
# 0.007 -> normalize -> 0.7.0
%define cpan_version 0.007
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Details of the native integer data type
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(parent)
Requires:       perl(parent)
Provides:       perl(Data::Integer) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module is about the native integer numerical data type. A native
integer is one of the types of datum that can appear in the numeric part of
a Perl scalar. This module supplies constants describing the native integer
type.

There are actually two native integer representations: signed and unsigned.
Both are handled by this module.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README SECURITY.md

%changelog
