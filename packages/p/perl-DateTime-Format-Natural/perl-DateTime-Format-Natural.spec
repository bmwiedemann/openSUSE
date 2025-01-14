#
# spec file for package perl-DateTime-Format-Natural
#
# Copyright (c) 2025 SUSE LLC
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
Version:        1.190.0
Release:        0
# 1.19 -> normalize -> 1.190.0
%define cpan_version 1.19
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parse informal natural language date/time strings
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCHUBIGER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::HiRes)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(Params::Validate) >= 1.15
BuildRequires:  perl(Test::MockTime::HiRes)
BuildRequires:  perl(boolean)
Requires:       perl(Clone)
Requires:       perl(DateTime)
Requires:       perl(DateTime::HiRes)
Requires:       perl(DateTime::TimeZone)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Params::Validate) >= 1.15
Requires:       perl(boolean)
Provides:       perl(DateTime::Format::Natural) = %{version}
Provides:       perl(DateTime::Format::Natural::Calc) = 1.46
Provides:       perl(DateTime::Format::Natural::Compat) = 0.07
Provides:       perl(DateTime::Format::Natural::Duration) = 0.07
Provides:       perl(DateTime::Format::Natural::Duration::Checks) = 0.05
Provides:       perl(DateTime::Format::Natural::Expand) = 0.04
Provides:       perl(DateTime::Format::Natural::Extract) = 0.13
Provides:       perl(DateTime::Format::Natural::Formatted) = 0.12
Provides:       perl(DateTime::Format::Natural::Helpers) = 0.06
Provides:       perl(DateTime::Format::Natural::Lang::Base) = 1.08
Provides:       perl(DateTime::Format::Natural::Lang::EN) = 1.72
Provides:       perl(DateTime::Format::Natural::Rewrite) = 0.08
Provides:       perl(DateTime::Format::Natural::Test) = 0.130.0
Provides:       perl(DateTime::Format::Natural::Utils) = 0.08
Provides:       perl(DateTime::Format::Natural::Wrappers) = 0.03
%undefine       __perllib_provides
Recommends:     perl(Date::Calc)
%{perl_requires}

%description
'DateTime::Format::Natural' parses informal natural language date/time
strings. In addition, parsable date/time substrings may be extracted from
ordinary strings.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README TODO

%changelog
