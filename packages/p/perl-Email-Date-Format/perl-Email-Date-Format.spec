#
# spec file for package perl-Email-Date-Format
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define cpan_name Email-Date-Format
Name:           perl-Email-Date-Format
Version:        1.005
Release:        0
Summary:        Produce RFC 2822 date strings
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source:         https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Patch0:         fix-time-local.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod) >= 1.41
Requires:       perl(Exporter) >= 5.57
Requires:       perl(Time::Local)
Requires:       perl(strict)
Requires:       perl(warnings)
BuildArch:      noarch
%{perl_requires}

%description
This module provides a simple means for generating an RFC 2822 compliant
datetime string. (In case you care, they're not RFC 822 dates, because they
use a four digit year, which is not allowed in RFC 822.)

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%license LICENSE
%doc Changes README

%changelog
