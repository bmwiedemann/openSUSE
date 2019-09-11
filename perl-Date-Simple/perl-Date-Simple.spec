#
# spec file for package perl-Date-Simple (Version 3.03)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           perl-Date-Simple
Version:        3.03
Release:        1
License:         Artistic-1.0 or GPL-2.0+
%define cpan_name Date-Simple
Summary:        a simple date object
Url:            http://search.cpan.org/dist/Date-Simple/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/I/IZ/IZUT/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
Requires:       perl(Scalar::Util)
Requires:       perl(Test::More)
%{perl_requires}

%description
Dates are complex enough without times and timezones. This module may be
used to create simple date objects. It handles:

* Validation.

  Reject 1999-02-29 but accept 2000-02-29.

* Interval arithmetic.

  How many days were between two given dates? What date comes N days after
  today?

* Day-of-week calculation.

  What day of the week is a given date?

* Transparent date formatting.

  How should a date object be formatted.

It does *not* deal with hours, minutes, seconds, and time zones.

A date is uniquely identified by year, month, and day integers within valid
ranges. This module will not allow the creation of objects for invalid
dates. Attempting to create an invalid date will return undef. Month
numbering starts at 1 for January, unlike in C and Java. Years are 4-digit.

Gregorian dates up to year 9999 are handled correctly, but we rely on
Perl's builtin 'localtime' function when the current date is requested. On
some platforms, 'localtime' may be vulnerable to rollovers such as the Unix
'time_t' wraparound of 18 January 2038.

Overloading is used so you can compare or subtract two dates using standard
numeric operators such as '==', and the sum of a date object and an integer
is another date object.

Date::Simple objects are immutable. After assigning '$date1' to '$date2',
no change to '$date1' can affect '$date2'. This means, for example, that
there is nothing like a 'set_year' operation, and '$date++' assigns a new
object to '$date'.

This module contains various undocumented functions. They may not be
available on all platforms and are likely to change or disappear in future
releases. Please let the author know if you think any of them should be
public.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog COPYING README

%changelog
