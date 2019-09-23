#
# spec file for package perl-SOAP-Lite
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


#Upstream: Artistic-1.0 or GPL-1.0+
%define cpan_name SOAP-Lite
Name:           perl-SOAP-Lite
Version:        1.27
Release:        0
Summary:        Perl's Web Services Toolkit
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND CC-BY-ND-2.0
Group:          Development/Libraries/Perl
URL:            http://search.cpan.org/dist/SOAP-Lite/
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl-SOAP-Lite-1.27-usr-bin-env.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::SessionData) >= 1.03
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Tools)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
%if 0%{?suse_version} >= 1550
BuildRequires:  perl(Test::MockObject)
%endif
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Parser) >= 2.23
BuildRequires:  perl(XML::Parser::Lite) >= 0.715
BuildRequires:  perl(constant)
Requires:       perl(Class::Inspector)
Requires:       perl(Compress::Zlib)
Requires:       perl(IO::SessionData) >= 1.03
Requires:       perl(IO::Socket::SSL)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent)
Requires:       perl(MIME::Base64)
Requires:       perl(Scalar::Util)
Requires:       perl(Task::Weaken)
Requires:       perl(URI)
Requires:       perl(URI::Escape)
Requires:       perl(XML::Parser) >= 2.23
Requires:       perl(XML::Parser::Lite) >= 0.715
Requires:       perl(constant)
Recommends:     perl(Apache)
Recommends:     perl(DIME::Tools) >= 0.03
Recommends:     perl(FCGI)
Recommends:     perl(HTTP::Daemon)
Recommends:     perl(MIME::Tools)
BuildArch:      noarch
%{perl_requires}

%description
SOAP::Lite is a collection of Perl modules which provides a simple and
lightweight interface to the Simple Object Access Protocol (SOAP) both on
client and server side.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes Debian_CPANTS.txt examples HACKING README ReleaseNotes.txt
%license LICENSE

%changelog
