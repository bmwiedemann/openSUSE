#
# spec file for package perl-App-Dochazka-WWW
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-App-Dochazka-WWW
Version:        0.155
Release:        0
%define cpan_name App-Dochazka-WWW
Summary:        Dochazka Attendance & Time Tracking system web client
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
URL:            http://search.cpan.org/dist/App-Dochazka-WWW/
Source0:        App-Dochazka-WWW-0.155.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::CELL) >= 0.196
BuildRequires:  perl(App::MFILE::WWW) >= 0.164
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Module::Build) >= 0.370000
BuildRequires:  perl(Params::Validate) >= 1.06
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Test::Fatal)
Requires:       perl(App::CELL) >= 0.196
Requires:       perl(App::MFILE::WWW) >= 0.164
Requires:       perl(File::ShareDir) >= 1.00
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkgconfig(systemd)
Requires(pre): /usr/sbin/groupadd
Requires(pre): /usr/sbin/useradd
%{?systemd_ordering}

%pre
getent group dochazka-www >/dev/null || groupadd -r dochazka-www
getent passwd dochazka-www >/dev/null || useradd -r -g dochazka-www -d %{_localstatedir}/lib/dochazka-www -s /sbin/nologin -c "user for dochazka WWW" dochazka-www
%service_add_pre dochazka-www.service

%preun
%service_del_preun dochazka-www.service

%postun
%service_del_postun dochazka-www.service

%post
%service_add_post dochazka-www.service
# MANUAL END

%description
This is the web client of the Dochazka Attendance & Time Tracking system.
For more information see the App::Dochazka::REST manpage and the
App::MFILE::WWW manpage.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
# MANUAL BEGIN
install -dm0755 %{buildroot}%{_sysconfdir}/dochazka-www
install -m0640 ext/WWW_SiteConfig.pm.example %{buildroot}%{_sysconfdir}/dochazka-www/WWW_SiteConfig.pm
install -m0640 ext/WWW_SiteConfig.pm.example %{buildroot}%{_sysconfdir}/dochazka-www/WWW_SiteConfig.pm.example
install -dm0755 %{buildroot}%{_localstatedir}/lib/dochazka-www
install -dm0755 %{buildroot}%{_localstatedir}/log/dochazka-www
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
ln -sf service %{buildroot}%{_sbindir}/rcdochazka-www
install -m0644 ext/systemd/dochazka-www.service %{buildroot}%{_unitdir}/dochazka-www.service

echo "%dir %{_sysconfdir}/dochazka-www" >> %{name}.files
echo "%config(noreplace) %attr(0640,dochazka-www,dochazka-www) %{_sysconfdir}/dochazka-www/WWW_SiteConfig.pm" >> %{name}.files
echo "%config %attr(0640,dochazka-www,dochazka-www) %{_sysconfdir}/dochazka-www/WWW_SiteConfig.pm.example" >> %{name}.files
echo "%attr(0750,dochazka-www,dochazka-www) %dir %{_localstatedir}/lib/dochazka-www" >> %{name}.files
echo "%attr(0750,dochazka-www,dochazka-www) %dir %{_localstatedir}/log/dochazka-www" >> %{name}.files
echo "%{_sbindir}/rcdochazka-www" >> %{name}.files
echo "%{_unitdir}/dochazka-www.service" >> %{name}.files
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes ext LICENSE README.rst share

%changelog
