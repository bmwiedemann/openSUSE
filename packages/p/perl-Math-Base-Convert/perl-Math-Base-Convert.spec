#
# spec file for package perl-Math-Base-Convert
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Math-Base-Convert
Version:        0.11
Release:        0
%define cpan_name Math-Base-Convert
Summary:        Very Fast Base to Base Conversion
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Math-Base-Convert/
Source0:        http://www.cpan.org/authors/id/M/MI/MIKER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         reproducible.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provides fast functions and methods to convert between
arbitrary number bases from 2 (binary) thru 65535.

This module is pure Perl, has no external dependencies, and is backward
compatible with old versions of Perl 5.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc bitmaps Changes README recurse2txt

%changelog
