#
# spec file for package perl-Path-Tiny
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Path-Tiny
Name:           perl-Path-Tiny
Version:        0.142
Release:        0
License:        Apache-2.0
Summary:        File path utility
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA) >= 5.45
BuildRequires:  perl(File::Path) >= 2.070000
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Digest::SHA) >= 5.45
Requires:       perl(File::Path) >= 2.070000
Requires:       perl(File::Temp) >= 0.19
Recommends:     perl(Unicode::UTF8) >= 0.58
%{perl_requires}

%description
This module provides a small, fast utility for working with file paths. It
is friendlier to use than File::Spec and provides easy access to functions
from several other core file handling modules. It aims to be smaller and
faster than many alternatives on CPAN, while helping people do many common
things in consistent and less error-prone ways.

Path::Tiny does not try to work for anything except Unix-like and Win32
platforms. Even then, it might break if you try something particularly
obscure or tortuous. (Quick! What does this mean:
'///../../..//./././a//b/.././c/././'? And how does it differ on Win32?)

All paths are forced to have Unix-style forward slashes. Stringifying the
object gives you back the path (after some clean up).

File input/output methods 'flock' handles before reading or writing, as
appropriate (if supported by the platform and/or filesystem).

The '*_utf8' methods ('slurp_utf8', 'lines_utf8', etc.) operate in raw
mode. On Windows, that means they will not have CRLF translation from the
':crlf' IO layer. Installing Unicode::UTF8 0.58 or later will speed up
'*_utf8' situations in many cases and is highly recommended. Alternatively,
installing PerlIO::utf8_strict 0.003 or later will be used in place of the
default ':encoding(UTF-8)'.

This module depends heavily on PerlIO layers for correct operation and thus
requires Perl 5.008001 or later.

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
%doc Changes CONTRIBUTING.mkdn README
%license LICENSE

%changelog
