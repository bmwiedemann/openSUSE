#
# spec file for package perl-Time-Moment
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Time-Moment
Version:        0.44
Release:        0
%define cpan_name Time-Moment
Summary:        Represents a date and time of day with an offset from UTC
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Time-Moment/
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.18
BuildRequires:  perl(Test::Fatal) >= 0.006
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Number::Delta) >= 1.060000
BuildRequires:  perl(Test::Requires)
%{perl_requires}

%description
'Time::Moment' is an immutable object representing a date and time of day
with an offset from UTC in the ISO 8601 calendar system.

Time is measured in nanoseconds since '0001-01-01T00Z'. In 'Time:Moment'
leap seconds are ignored. It is assumed that there are exactly
'86,400,000,000,000' nanoseconds per day. 'Time::Moment' can represent all
epoch integers from '-62,135,596,800' to '253,402,300,799'; this range
suffices to measure times to nanosecond precision for any instant that is
within '0001-01-01T00:00:00Z' to '9999-12-31T23:59:59Z'.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
