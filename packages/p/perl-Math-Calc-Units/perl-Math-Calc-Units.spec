#
# spec file for package perl-Math-Calc-Units
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define         cpan_name Math-Calc-Units

Name:           perl-%cpan_name
Version:        1.07
Release:        0
Summary:        Human-readable unit-aware calculator
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Math-Calc-Units/
Source:         %cpan_name-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       %cpan_name
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
Math::Calc::Units is a simple calculator that keeps track of units. It
currently handles combinations of byte sizes and duration only, although adding
any other multiplicative types is easy. Any unknown type is treated as a unique
user type (with some effort to map English plurals to their singular forms).

The primary intended use is via the ucalc script that prints out all of the
"readable" variants of a value. For example, "3 bytes" will only produce "3
byte", but "3 byte / sec" produces the original along with "180 byte / minute",
"10.55 kilobyte / hour", etc.

%prep
%setup -q -n %cpan_name-%{version}

%build
perl Makefile.PL OPTIMIZE="%{optflags} -Wall"
make

%check
make test

%install
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist

%clean
# clean up the hard disc after build
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Artistic.html COPYING Changes LICENSE MANIFEST README
%{_bindir}/uc*
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Math
%{perl_vendorarch}/auto/Math

%changelog
