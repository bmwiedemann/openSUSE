#
# spec file for package perl-Test-MockDateTime
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


Name:           perl-Test-MockDateTime
Version:        0.02
Release:        0
%define cpan_name Test-MockDateTime
Summary:        Mock Datetime->Now Calls During Tests
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-MockDateTime/
Source0:        http://www.cpan.org/authors/id/W/WK/WKI/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime) >= 1
BuildRequires:  perl(DateTime::Format::DateParse) >= 0.05
BuildRequires:  perl(ok) >= 0.11
Requires:       perl-base = %{perl_version}
Requires:       perl(DateTime) >= 1
Requires:       perl(DateTime::Format::DateParse) >= 0.05
Requires:       perl(ok) >= 0.11

%{perl_requires}

%description
Getting the current time sometimes is not very helpful for testing
scenarios. Instead, if you could obtain a known value during the runtime of
a testcase will make your results predictable.

Why another Date Mocker? I wanted something simple with a very concise
usage pattern and a mocked date should only exist and stay constant inside
a scope. After leaving the scope the current time should be back. This lead
to this tiny module.

This simple module allows faking a given date and time for the runtime of a
subsequent code block. By default the 'on' keyword is exported into the
namespace of the test file. The date to get mocked must be in a format that
is recognized by DateTime::Format::DateParse.

    on '2013-01-02 03:04:05', sub { ... };

is basically the same as

    {
        my $now = DateTime::Format::DateParse->parse_datetime(
            '2013-01-02 03:04:05'
        );
        
        local *DateTime::now = sub { $now->clone };
        
        ... everything from code block above
    }

A drawback when relying on this module is that you must know that the
module you are testing uses 'DateTime->now' to obtain the current time.
=cut

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

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README README.md

%changelog
