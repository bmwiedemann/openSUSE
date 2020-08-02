#
# spec file for package perl-DateTime-Format-SQLite
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


Name:           perl-DateTime-Format-SQLite
Version:        0.11
Release:        0
%define cpan_name DateTime-Format-SQLite
Summary:        Parse and format SQLite dates and times
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DateTime-Format-SQLite/
Source:         http://www.cpan.org/modules/by-module/DateTime/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime) >= 0.1
BuildRequires:  perl(DateTime::Format::Builder) >= 0.6
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(DateTime) >= 0.1
Requires:       perl(DateTime::Format::Builder) >= 0.6
%{perl_requires}

%description
This module understands the formats used by SQLite for its 'date',
'datetime' and 'time' functions. It can be used to parse these formats in
order to create the DateTime manpage objects, and it can take a DateTime
object and produce a timestring accepted by SQLite.

*NOTE:* SQLite does not have real date/time types but stores everything as
strings. This module deals with the date/time strings as
understood/returned by SQLite's 'date', 'time', 'datetime', 'julianday' and
'strftime' SQL functions. You will usually want to store your dates in one
of these formats.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
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
%doc Changes LICENSE README

%changelog
