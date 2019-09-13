#
# spec file for package perl-DateTime-Calendar-Mayan
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-DateTime-Calendar-Mayan
%define real_name DateTime-Calendar-Mayan
Summary:        The Mayan Long Count, Haab, and Tzolkin calendars
Url:            http://search.cpan.org/perldoc?DateTime::Calendar::Mayan
Group:          Development/Libraries/Perl
License:        Artistic-1.0
Version:        0.0601
Release:        2
Source:         %{real_name}-%{version}.tar.gz
Patch1:         DateTime-Calendar-Mayan-Makefile.patch
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Params::Validate)
Requires:       perl(DateTime)
Requires:       perl(Params::Validate)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
An implementation of the Mayan Long Count, Haab, and Tzolkin calendars as
defined in "Calendrical Calculations The Millennium Edition". Supplemented by
"Frequently Asked Questions about Calendars".

Author:
-------
    Joshua Hoblitt <jhoblitt@cpan.org>


%prep
%setup -q -n %{real_name}-%{version}
%patch1 -p0

%build
perl Makefile.PL 
make %{?jobs:-j%jobs}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.files 
%defattr(-, root, root)
%doc Changes README MANIFEST

%changelog
