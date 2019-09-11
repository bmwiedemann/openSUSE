#
# spec file for package perl-Lingua-Stem-Snowball
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

%bcond_with test

Name:           perl-Lingua-Stem-Snowball
%define cpan_name Lingua-Stem-Snowball
Summary:        Perl interface to Snowball stemmers
Version:        0.952
Release:        1
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Lingua-Stem-Snowball/
#Source:         http://www.cpan.org/modules/by-module/Lingua/Lingua-Stem-Snowball-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl(Module::Build)
BuildRequires:  perl-macros
%if %{with test}
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
%endif
#

%description
Stemming reduces related words to a common root form -- for instance,
"horse", "horses", and "horsing" all become "hors". Most commonly, stemming
is deployed as part of a search application, allowing searches for a given
term to match documents which contain other forms of that term.

Authors:
--------
    Oleg Bartunov, <oleg at sai dot msu dot su>
    Teodor Sigaev, <teodor at stack dot net>
    Marvin Humphrey <marvin at rectangular dot com>

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%check
./Build test

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changes README

%changelog
