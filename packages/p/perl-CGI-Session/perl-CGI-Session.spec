#
# spec file for package perl-CGI-Session
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


%define cpan_name CGI-Session
Name:           perl-CGI-Session
Version:        4.480.0
Release:        0
# 4.48 -> normalize -> 4.480.0
%define cpan_version 4.48
#Upstream: Artistic-1.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Persistent session data in CGI applications
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKSTOS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI) >= 3.260
BuildRequires:  perl(Module::Build) >= 0.38
Requires:       perl(CGI) >= 3.260
Provides:       perl(CGI::Session) = %{version}
Provides:       perl(CGI::Session::Driver) = 4.430.0
Provides:       perl(CGI::Session::Driver::DBI) = 4.430.0
Provides:       perl(CGI::Session::Driver::db_file) = 4.430.0
Provides:       perl(CGI::Session::Driver::file) = 4.430.0
Provides:       perl(CGI::Session::Driver::mysql) = 4.430.0
Provides:       perl(CGI::Session::Driver::postgresql) = 4.430.0
Provides:       perl(CGI::Session::Driver::sqlite) = 4.430.0
Provides:       perl(CGI::Session::ErrorHandler) = 4.430.0
Provides:       perl(CGI::Session::ID::incr) = 4.430.0
Provides:       perl(CGI::Session::ID::md5) = 4.430.0
Provides:       perl(CGI::Session::ID::static) = 4.440.0
Provides:       perl(CGI::Session::Serialize::default) = 4.430.0
Provides:       perl(CGI::Session::Serialize::freezethaw) = 4.430.0
Provides:       perl(CGI::Session::Serialize::storable) = 4.430.0
Provides:       perl(CGI::Session::Test::Default) = 4.470.0
Provides:       perl(CGI::Session::Test::SimpleObjectClass)
Provides:       perl(CGI::Session::Tutorial) = 4.430.0
Provides:       perl(OverloadedClass)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
# DB tests need a running database and the following
# variables set to proceed: DBI_DSN/DBI_USER/DBI_PASS
# Disabled by not installing the perl modules for now, as
# this needs to be done for all backends during build which
# increases the dependencies of the package
# running SQLite tests should be enough for now
BuildRequires:  perl-DBD-SQLite
BuildRequires:  perl(CGI::Simple)
BuildRequires:  perl(FreezeThaw)
# MANUAL END

%description
CGI::Session provides an easy, reliable and modular session management
system across HTTP requests.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes examples README

%changelog
