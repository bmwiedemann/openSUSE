#
# spec file for package perl-HTTP-CookieJar
#
# Copyright (c) 2021 SUSE LLC
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


Name:           perl-HTTP-CookieJar
Version:        0.010
Release:        0
%define cpan_name HTTP-CookieJar
Summary:        Minimalist HTTP user agent cookie jar
License:        Apache-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(parent)
#BuildRequires:  perl(Time::Local) >= 1.1901
BuildRequires:  perl(URI)
Requires:       perl(HTTP::Date)
Requires:       perl(parent)
#Requires:       perl(Time::Local) >= 1.1901
Recommends:     perl(Mozilla::PublicSuffix)
%{perl_requires}
# MANUAL BEGIN
# ATTENTION: Manual fix because of perl versioning vs. rpm
# Time::Local started to use only 2 digits for the minor version
# In perl, 1.1901 equals v1.190.1 and 1.28 v.1.280
BuildRequires:  perl(Time::Local) >= 1.28
Requires:       perl(Time::Local) >= 1.28
# MANUAL END

%description
This module implements a minimalist HTTP user agent cookie jar in
conformance with at http://tools.ietf.org/html/rfc6265.

Unlike the commonly used HTTP::Cookies module, this module does not require
use of HTTP::Request and HTTP::Response objects. An LWP-compatible adapter
is available as HTTP::CookieJar::LWP.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING.mkdn README
%license LICENSE

%changelog
