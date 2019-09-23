#
# spec file for package perl-Time-Clock
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


Name:           perl-Time-Clock
Version:        1.03
Release:        0
%define cpan_name Time-Clock
Summary:        Twenty-four hour clock object with nanosecond precision.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Time-Clock/
Source:         http://www.cpan.org/authors/id/J/JS/JSIRACUSA/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
A the Time::Clock manpage object is a twenty-four hour clock with
nanosecond precision and wrap-around. It is a clock only; it has absolutely
no concept of dates. Vagaries of date/time such as leap seconds and
daylight savings time are unsupported.

When a the Time::Clock manpage object hits 23:59:59.999999999 and at least
one more nanosecond is added, it will wrap around to 00:00:00.000000000.
This works in reverse when time is subtracted.

the Time::Clock manpage objects automatically stringify to a user-definable
format.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes

%changelog
