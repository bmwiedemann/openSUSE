#
# spec file for package perl-DateTime-Format-Natural
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name DateTime-Format-Natural
Name:           perl-DateTime-Format-Natural
Version:        1.16
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parse informal natural language date/time strings
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCHUBIGER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::HiRes)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(Params::Validate) >= 1.15
BuildRequires:  perl(Test::MockTime::HiRes)
BuildRequires:  perl(boolean)
Requires:       perl(Clone)
Requires:       perl(DateTime)
Requires:       perl(DateTime::HiRes)
Requires:       perl(DateTime::TimeZone)
Requires:       perl(List::MoreUtils)
Requires:       perl(Params::Validate) >= 1.15
Requires:       perl(boolean)
Recommends:     perl(Date::Calc)
%{perl_requires}

%description
'DateTime::Format::Natural' parses informal natural language date/time
strings. In addition, parsable date/time substrings may be extracted from
ordinary strings.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README TODO

%changelog
