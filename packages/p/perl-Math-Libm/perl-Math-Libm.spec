#
# spec file for package perl-Math-Libm
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Math-Libm
Version:        1.00
Release:        0
%define cpan_name Math-Libm
Summary:        Perl extension for the C math library, libm
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Math-Libm/
Source:         http://www.cpan.org/authors/id/D/DS/DSLEWART/%{cpan_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/hroncok/RPMAdditionalSources/master/Math-Libm-license.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module is a translation of the C _math.h_ file. It exports the
following selected constants and functions.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist
cp %{S:1} .

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README Math-Libm-license.txt

%changelog
