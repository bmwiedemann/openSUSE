#
# spec file for package perl-Data-Binary
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Data-Binary
Name:           perl-Data-Binary
Version:        0.01
Release:        0
License:        Artistic-2.0
Summary:        Simple detection of binary versus text in strings
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SN/SNKWATT/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This simple module provides string equivalents to the -T / -B operators.
Since these only work on file names and file handles, this module provides
the same functions but on strings.

Note that the actual implementation is currently different, basically
because the -T / -B functions are in C/XS, and this module is written in
pure Perl. For now, anyway.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc changes.txt README readme.txt

%changelog
