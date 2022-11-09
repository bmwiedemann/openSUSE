#
# spec file for package perl-PerlIO-utf8_strict
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


%define cpan_name PerlIO-utf8_strict
Name:           perl-PerlIO-utf8_strict
Version:        0.010
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Fast and correct UTF-8 IO
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         no-return-in-nonvoid-function.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
This module provides a fast and correct UTF-8 PerlIO layer. Unlike perl's
default ':utf8' layer it checks the input for correctness.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

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
%license LICENSE

%changelog
