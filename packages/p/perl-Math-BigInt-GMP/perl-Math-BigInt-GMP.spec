#
# spec file for package perl-Math-BigInt-GMP
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Math-BigInt-GMP
Version:        1.6006
Release:        0
%define cpan_name Math-BigInt-GMP
Summary:        Backend Library for Math::Bigint Etc. Based On Gmp
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Math::BigInt) >= 1.999812
BuildRequires:  perl(Test::More) >= 0.82
Requires:       perl(Math::BigInt) >= 1.999812
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gmp-devel
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# Version check does not work for perl packages before 5.22
%if 0%{?suse_version} <= 1320
BuildRequires:  perl-Math-BigInt >= 1.999714
Requires:       perl-Math-BigInt >= 1.999714
%endif
# MANUAL END

%description
Math::BigInt::GMP is a replacement library for Math::BigInt::Calc that
reimplements some of the Math::BigInt::Calc functions in XS. It can be used
via:

    use Math::BigInt lib => 'GMP';

This package contains a replacement (drop-in) module for Math::BigInt's core,
Math::BigInt::Calc.pm.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc BUGS CHANGES CREDITS README TODO
%license LICENSE

%changelog
