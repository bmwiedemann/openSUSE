#
# spec file for package perl-Devel-PPPort
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Devel-PPPort
Version:        3.62
Release:        0
%define cpan_name Devel-PPPort
Summary:        Perl/Pollution/Portability
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes HACKERS README soak TODO

%changelog
