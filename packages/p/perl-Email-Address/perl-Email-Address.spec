#
# spec file for package perl-Email-Address
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


%define cpan_name Email-Address
Name:           perl-Email-Address
Version:        1.913
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        RFC 2822 Address Parsing and Creation
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Test::More) >= 0.96
%{perl_requires}

%description
This class implements a regex-based RFC 2822 parser that locates email
addresses in strings and returns a list of 'Email::Address' objects found.
Alternatively you may construct objects manually. The goal of this software
is to be correct, and very very fast.

Version 1.909 and earlier of this module had vulnerabilies (at
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-7686) and (at
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12558) which
allowed specially constructed email to cause a denial of service. The
reported vulnerabilities and some other pathalogical cases (meaning they
really shouldn't occur in normal email) have been addressed in version
1.910 and newer. If you're running version 1.909 or older, you should
update!

Alternatively, you could switch to *Email::Address::XS* which has a
backward compatible API. *Why not just use that?*

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
