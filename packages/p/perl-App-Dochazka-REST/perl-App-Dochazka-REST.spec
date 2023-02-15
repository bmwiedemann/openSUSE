#
# spec file for package perl-App-Dochazka-REST
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name App-Dochazka-REST
Name:           perl-App-Dochazka-REST
Version:        0.559
Release:        0
Summary:        Dochazka REST server
License:        BSD-3-Clause
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        App-Dochazka-REST-0.559.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::CELL) >= 0.215
BuildRequires:  perl(App::Dochazka::Common) >= 0.205
BuildRequires:  perl(Authen::Passphrase::SaltedDigest) >= 0.008
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Connector) >= 0.47
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Date::Holidays::CZ) >= 0.12
BuildRequires:  perl(File::ShareDir) >= 1
BuildRequires:  perl(File::ShareDir::Install) >= 0.11
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Mason)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate) >= 1.06
BuildRequires:  perl(Path::Router) >= 0.12
BuildRequires:  perl(Plack::Middleware::Session)
BuildRequires:  perl(Plack::Middleware::StackTrace)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Pod::Simple::HTML)
BuildRequires:  perl(Test::Deep::NoTest)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::JSON)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Web::MREST) >= 0.287
BuildRequires:  perl(Web::MREST::CLI) >= 0.276
BuildRequires:  perl(Web::Machine) >= 0.15
Requires:       perl(App::CELL) >= 0.215
Requires:       perl(App::Dochazka::Common) >= 0.207
Requires:       perl(Authen::Passphrase::SaltedDigest) >= 0.008
Requires:       perl(DBD::Pg)
Requires:       perl(DBI)
Requires:       perl(DBIx::Connector) >= 0.47
Requires:       perl(Date::Calc)
Requires:       perl(Date::Holidays::CZ) >= 0.12
Requires:       perl(File::ShareDir) >= 1
Requires:       perl(JSON)
Requires:       perl(Mason)
Requires:       perl(Params::Validate) >= 1.06
Requires:       perl(Path::Router) >= 0.12
Requires:       perl(Plack::Middleware::Session)
Requires:       perl(Plack::Middleware::StackTrace)
Requires:       perl(Plack::Runner)
Requires:       perl(Pod::Simple::HTML)
Requires:       perl(Test::Deep::NoTest)
Requires:       perl(Try::Tiny)
Requires:       perl(Web::MREST) >= 0.287
Requires:       perl(Web::MREST::CLI) >= 0.276
Requires:       perl(Web::Machine) >= 0.15
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  systemd
BuildRequires:  perl(Starman)
Requires:       perl(Starman)
Requires(pre): /usr/sbin/groupadd
Requires(pre): /usr/sbin/useradd
%{?systemd_requires}

%pre
getent group dochazka-rest >/dev/null || groupadd -r dochazka-rest
getent passwd dochazka-rest >/dev/null || useradd -r -g dochazka-rest -d %{_localstatedir}/lib/dochazka-rest -s /sbin/nologin -c "user for dochazka REST" dochazka-rest
%service_add_pre dochazka-rest.service

%preun
%service_del_preun dochazka-rest.service

%postun
%service_del_postun dochazka-rest.service

%post
%service_add_post dochazka-rest.service
# MANUAL END

%description
This distribution, App::Dochazka::REST, including all the modules in
'lib/', the scripts in 'bin/', and the configuration files in 'config/',
constitutes the REST server (API) component of Dochazka, the open-source
Attendance/Time Tracking (ATT) system.

Dochazka as a whole aims to be a convenient, open-source ATT solution.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
# MANUAL BEGIN
install -dm0755 %{buildroot}%{_sysconfdir}/dochazka-rest
install -m0640 ext/REST_SiteConfig.pm.example %{buildroot}%{_sysconfdir}/dochazka-rest/REST_SiteConfig.pm
install -m0640 ext/REST_SiteConfig.pm.example %{buildroot}%{_sysconfdir}/dochazka-rest/REST_SiteConfig.pm.example
install -dm0755 %{buildroot}%{_localstatedir}/lib/dochazka-rest
install -dm0755 %{buildroot}%{_localstatedir}/log/dochazka
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
ln -sf service %{buildroot}%{_sbindir}/rcdochazka-rest
install -m0644 ext/systemd/dochazka-rest.service %{buildroot}%{_unitdir}/dochazka-rest.service

echo "%dir %{_sysconfdir}/dochazka-rest" >> %{name}.files
echo "%config(noreplace) %attr(0640,dochazka-rest,dochazka-rest) %{_sysconfdir}/dochazka-rest/REST_SiteConfig.pm" >> %{name}.files
echo "%config %attr(0640,dochazka-rest,dochazka-rest) %{_sysconfdir}/dochazka-rest/REST_SiteConfig.pm.example" >> %{name}.files
echo "%attr(0750,dochazka-rest,dochazka-rest) %dir %{_localstatedir}/lib/dochazka-rest" >> %{name}.files
echo "%attr(0750,dochazka-rest,dochazka-rest) %dir %{_localstatedir}/log/dochazka" >> %{name}.files
echo "%{_sbindir}/rcdochazka-rest" >> %{name}.files
echo "%{_unitdir}/dochazka-rest.service" >> %{name}.files
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.rst run-tests.sh version.plx WISHLIST
%license LICENSE

%changelog
