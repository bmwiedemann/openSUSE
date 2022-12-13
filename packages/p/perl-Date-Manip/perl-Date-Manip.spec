#
# spec file for package perl-Date-Manip
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


%define cpan_name Date-Manip
Name:           perl-Date-Manip
Version:        6.90
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Date manipulation routines
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBECK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.67_01
BuildRequires:  perl(Test::Inter) >= 1.09
%{perl_requires}

%description
Date::Manip is a series of modules designed to make any common date/time
operation easy to do. Operations such as comparing two times, determining a
date a given amount of time from another, or parsing international times
are all easily done. It deals with time as it is used in the Gregorian
calendar (the one currently in use) with full support for time changes due
to daylight saving time.

From the very beginning, the main focus of Date::Manip has been to be able
to do ANY desired date/time operation easily. Many other modules exist
which may do a subset of these operations quicker or more efficiently, but
no other module can do all of the operations available in Date::Manip.

Date::Manip has functionality to work with several fundamental types of
data.

* *dates*

The word date is used extensively here and is somewhat misleading. In
Date::Manip, a date consists of three pieces of information: a calendar
date (year, month, day), a time of day (hour, minute, second), and time
zone information. Calendar dates and times are fully handled. Time zones
are handled as well, but depending on how you use Date::Manip, there may be
some limitations as discussed below.

* *delta*

A delta is an amount of time (i.e. the amount of time between two different
dates). Think of it as the duration of an event or the amount of time
between two dates.

A delta refers only to an amount of time. It includes no information about
a starting or ending date/time. Most people will think of a delta as an
amount of time, but the term 'time' is already used so much in this module
that I didn't want to use it here in order to avoid confusion.

* *recurrence*

A recurring event is something which occurs on a regular recurring basis.

* *holidays* and *events*

Holidays and events are basically named dates or recurrences.

Among other things, Date::Manip allow you to:

* ***

Enter a date in practically any format you choose.

* ***

Compare two dates, entered in widely different formats to determine which
is earlier.

* ***

Extract any information you want from a date using a format string similar
to the Unix date command.

* ***

Determine the amount of time between two dates, or add an amount of time (a
delta) to a date to get a second date.

* ***

Work with dates using international formats (foreign month names, 12/10/95
referring to October rather than December, etc.).

* ***

Convert dates from one timezone to another.

* ***

To find a list of dates where a recurring event happens.

Each of these tasks is trivial (one or two lines at most) with this
package.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples README README.first
%license LICENSE

%changelog
