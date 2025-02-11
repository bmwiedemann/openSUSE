#
# spec file for package perl-Text-Iconv
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


%define cpan_name Text-Iconv
Name:           perl-Text-Iconv
Version:        1.700.0
Release:        0
# 1.7 -> normalize -> 1.700.0
%define cpan_version 1.7
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl interface to iconv() codeset conversion function
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MP/MPIOTR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Text::Iconv) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The *Text::Iconv* module provides a Perl interface to the iconv() function
as defined by the Single UNIX Specification.

The convert() method converts the encoding of characters in the input
string from the _fromcode_ codeset to the _tocode_ codeset, and returns the
result.

Settings of _fromcode_ and _tocode_ and their permitted combinations are
implementation-dependent. Valid values are specified in the system
documentation; the iconv(1) utility should also provide a *-l* option that
lists all supported codesets.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README

%changelog
