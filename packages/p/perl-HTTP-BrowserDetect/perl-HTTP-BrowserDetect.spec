#
# spec file for package perl-HTTP-BrowserDetect
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


%define cpan_name HTTP-BrowserDetect
Name:           perl-HTTP-BrowserDetect
Version:        3.38
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Determine Web browser, version, and platform from an HTTP user agent string
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(JSON::PP) >= 4.04
BuildRequires:  perl(List::Util) >= 1.49
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Warnings)
%{perl_requires}

%description
The HTTP::BrowserDetect object does a number of tests on an HTTP user agent
string. The results of these tests are available via methods of the object.

For an online demonstration of this module's parsing, you can check out
http://www.browserdetect.org/

This module was originally based upon the JavaScript browser detection code
available at
http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.

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
%doc Changes CONTRIBUTORS examples README.md TODO
%license LICENSE

%changelog
