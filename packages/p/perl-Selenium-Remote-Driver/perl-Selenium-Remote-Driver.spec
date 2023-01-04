#
# spec file for package perl-Selenium-Remote-Driver
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


%define cpan_name Selenium-Remote-Driver
Name:           perl-Selenium-Remote-Driver
Version:        1.48
Release:        0
License:        Apache-2.0
Summary:        Perl Client for Selenium Remote Driver
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TE/TEODESIAN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# MANUAL
#BuildArch:     noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Clone)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IO::Uncompress::Unzip) >= 2.030
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moo) >= 1.005
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::MockModule) >= v0.13.0
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(namespace::clean)
Requires:       perl(Archive::Zip)
Requires:       perl(Clone)
Requires:       perl(File::Which)
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Response)
Requires:       perl(IO::String)
Requires:       perl(IO::Uncompress::Unzip) >= 2.030
Requires:       perl(JSON)
Requires:       perl(LWP::UserAgent)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Moo) >= 1.005
Requires:       perl(Moo::Role)
Requires:       perl(Sub::Install)
Requires:       perl(Test::LongString)
Requires:       perl(Try::Tiny)
Requires:       perl(XML::Simple)
Requires:       perl(namespace::clean)
%{perl_requires}
# MANUAL BEGIN
Requires:       lsof
# MANUAL END

%description
Selenium is a test tool that allows you to write automated web application
UI tests in any programming language against any HTTP website using any
mainstream JavaScript-enabled browser. This module is an implementation of
the client for the Remote driver that Selenium provides. You can find
bindings for other languages at this location:

https://www.seleniumhq.org/download/

This module sends commands directly to the Server using HTTP. Using this
module together with the Selenium Server, you can automatically control any
supported browser. To use this module, you need to have already downloaded
and started the Selenium Server (Selenium Server is a Java application).

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's,!/bin/env perl,/usr/bin/perl,' driver-example.pl
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README README.md TAGS
%license LICENSE

%changelog
