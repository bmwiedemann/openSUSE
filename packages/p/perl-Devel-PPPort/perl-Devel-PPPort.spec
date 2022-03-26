#
# spec file for package perl-Devel-PPPort
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


%define cpan_name Devel-PPPort
Name:           perl-Devel-PPPort
Version:        3.68
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl/Pollution/Portability
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Perl's API has changed over time, gaining new features, new functions,
increasing its flexibility, and reducing the impact on the C namespace
environment (reduced pollution). The header file written by this module,
typically _ppport.h_, attempts to bring some of the newer Perl API features
to older versions of Perl, so that you can worry less about keeping track
of old releases, but users can still reap the benefit.

'Devel::PPPort' contains two functions, 'WriteFile' and 'GetFileContents'.
'WriteFile''s only purpose is to write the _ppport.h_ C header file. This
file contains a series of macros and, if explicitly requested, functions
that allow XS modules to be built using older versions of Perl. Currently,
Perl versions from 5.003 to 5.20 are supported.

'GetFileContents' can be used to retrieve the file contents rather than
writing it out.

This module is used by 'h2xs' to write the file _ppport.h_.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes HACKERS README soak TODO

%changelog
