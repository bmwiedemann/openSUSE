#
# spec file for package perl-CGI-Session
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-CGI-Session
Version:        4.48
Release:        0
#Upstream: Artistic-1.0
%define cpan_name CGI-Session
Summary:        Persistent Session Data in Cgi Applications
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CGI-Session/
Source0:        http://www.cpan.org/authors/id/M/MA/MARKSTOS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI) >= 3.26
BuildRequires:  perl(Module::Build) >= 0.380000
Requires:       perl(CGI) >= 3.26
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
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README

%changelog
