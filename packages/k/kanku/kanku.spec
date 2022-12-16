#
# spec file for package kanku
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


%define kanku_user   kankurun
%define kanku_group  kanku
%define kanku_vardir /var/lib/kanku/

Name:           kanku
# Version gets set by obs-service-tar_scm
Version:        0.13.0
Release:        0
License:        GPL-3.0-only
Summary:        Development and continuous integration
URL:            https://github.com/M0ses/kanku
Group:          Productivity/Networking/Web/Utilities
Source:         %{name}-%{version}.tar.xz
BuildArch:      noarch
# Build only for supported arch. See 'etc/templates/default-vm.tt2.$ARCH'
ExclusiveArch:  aarch64 x86_64 %{ix86}
BuildRequires:  fdupes
BuildRequires:  perl-macros
BuildRequires:  systemd-rpm-macros

# perl requires for %check
BuildRequires:  perl(Const::Fast)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Fixtures)
BuildRequires:  perl(DBIx::Class::Migration)
BuildRequires:  perl(Dancer2)
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(Dancer2::Plugin::Auth::Extensible)
BuildRequires:  perl(Dancer2::Plugin::Auth::Extensible::Provider::DBIC)
BuildRequires:  perl(Dancer2::Plugin::DBIC)
BuildRequires:  perl(Dancer2::Plugin::REST)
BuildRequires:  perl(Dancer2::Plugin::WebSocket)
BuildRequires:  perl(Expect)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::LibMagic)
BuildRequires:  perl(IO::Interactive)
BuildRequires:  perl(IO::Uncompress::UnXz)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::App)
BuildRequires:  perl(MooseX::Singleton)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(Net::OBS::Client)
BuildRequires:  perl(Net::SSH2)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Sys::Virt)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Plugin::Filter::ANSIColor)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(XML::Structured)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(YAML::PP)
# DBD::SQLite is also provided by perl-DBD-SQLite-Amalgamation
# but perl-DBD-SQLite-Amalgamation is breaks with SQL syntax errors
# at job_histroy_sub table
BuildRequires:  perl-DBD-SQLite
BuildRequires:  desktop-file-utils
BuildRequires:  libvirt-daemon
BuildRequires:  shared-mime-info
BuildRequires:  perl(Archive::Cpio)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Mail::Sendmail)
BuildRequires:  perl(Net::AMQP::RabbitMQ)
BuildRequires:  perl(UUID)

Requires:       kanku-cli = %{version}
Requires:       kanku-dispatcher = %{version}
Requires:       kanku-scheduler = %{version}
Requires:       kanku-triggerd = %{version}
Requires:       kanku-web = %{version}
Requires:       kanku-worker = %{version}

%description
kanku is a utility for integration of kiwi images built
by the Open Build Service (OBS) in a development and testing workflow.

It provides a framework for automation of setups,
e.g. to prepare development environments or run simple tests.

%prep
%autosetup -p1

%build
/bin/true

%install
%make_install DOCDIR=%{_defaultdocdir}/kanku/
%fdupes %{buildroot}/opt/kanku/share
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rckanku-web
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rckanku-worker
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rckanku-dispatcher
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rckanku-scheduler
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rckanku-triggerd

%check
# FIXME
#prove -Ilib t/000_use.t

%files
%exclude /etc
%exclude /usr

%package common
Summary:        Common files for kanku

Recommends:     apache2
Recommends:     osc
Recommends:     perl(IO::Uncompress::UnXz)
Recommends:     perl(YAML::PP::LibYAML)
Requires:       libvirt-daemon-config-network
Requires:       libvirt-daemon-config-nwfilter
Requires:       libvirt-daemon-qemu
Requires:       perl-Plack
Requires:       sudo
Requires:       perl(Config::Tiny)
Requires:       perl(Const::Fast)
Requires:       perl(DBIx::Class)
Requires:       perl(DBIx::Class::Fixtures)
Requires:       perl(DBIx::Class::Migration)
Requires:       perl(Dancer2)
Requires:       perl(Dancer2::Plugin::Auth::Extensible)
Requires:       perl(Dancer2::Plugin::Auth::Extensible::Provider::DBIC)
Requires:       perl(Dancer2::Plugin::DBIC)
Requires:       perl(Dancer2::Plugin::REST)
Requires:       perl(Expect)
Requires:       perl(File::HomeDir)
Requires:       perl(File::LibMagic)
Requires:       perl(IO::Uncompress::UnXz)
Requires:       perl(IPC::Run)
Requires:       perl(JSON::XS)
Requires:       perl(Log::Log4perl)
Requires:       perl(Moose)
Requires:       perl(MooseX::App)
Requires:       perl(MooseX::Singleton)
Requires:       perl(Net::IP)
Requires:       perl(Net::OBS::Client)
Requires:       perl(Net::SSH2)
Requires:       perl(Path::Class)
Requires:       perl(Sys::Virt)
Requires:       perl(Template)
Requires:       perl(Template::Plugin::Filter::ANSIColor)
Requires:       perl(Term::ReadKey)
Requires:       perl(Test::Simple)
Requires:       perl(XML::Structured)
Requires:       perl(XML::XPath)
Requires:       perl(YAML::PP)
# DBD::SQLite is also provided by perl-DBD-SQLite-Amalgamation
# but perl-DBD-SQLite-Amalgamation is breaks with SQL syntax errors
# at job_histroy_sub table
Requires:       perl-DBD-SQLite
Requires:       perl(Archive::Cpio)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Mail::Sendmail)
Requires:       perl(UUID)
%if 0%{?suse_version}
Requires:       openssl(cli)
%else
Requires:       openssl
%endif

Conflicts:      perl-DBD-SQLite-Amalgamation

%description common
common config and lib files used in kanku

%post common
%tmpfiles_create %_tmpfilesdir/kanku.conf

%files common
%doc README.md RELEASE-NOTES-*.md CHANGELOG.md

%dir /usr/lib/kanku
%dir /usr/lib/kanku/lib
%dir /usr/lib/kanku/lib/Kanku
%dir /usr/lib/kanku/lib/Kanku/Daemon

# share contains database related stuff
%dir /usr/share/kanku
/usr/share/kanku/fixtures
/usr/share/kanku/migrations

%attr(755,root,root) /usr/bin/kanku
%attr(755,root,root) /usr/lib/kanku/network-setup.pl

%dir /etc/kanku
%ghost /etc/kanku/config.yml
%dir /etc/kanku/logging/
%config(noreplace) /etc/kanku/logging/console.conf
%config(noreplace) /etc/kanku/logging/network-setup.conf
%config(noreplace) /etc/kanku/logging/default.conf

%dir /etc/kanku/templates
%dir /etc/kanku/templates/cmd
%dir /etc/kanku/templates/cmd/setup
%config /etc/kanku/templates/default-vm.tt2
%config /etc/kanku/templates/with-spice.tt2
%config /etc/kanku/templates/cmd/init.tt2
%config /etc/kanku/templates/cmd/setup/*
%dir    /etc/kanku/templates/examples-vm/
%config /etc/kanku/templates/examples-vm/obs-server-26.tt2
%config /etc/kanku/templates/examples-vm/sles11sp3.tt2
%config /etc/kanku/templates/examples-vm/obs-server.tt2

%dir /etc/kanku/jobs
%dir /etc/kanku/jobs/examples
%config /etc/kanku/jobs/examples/obs-server.yml
%config /etc/kanku/jobs/examples/obs-server-26.yml
%config /etc/kanku/jobs/examples/sles11sp3.yml

# %exclude %dir /etc/sudoers.d
# %ghost /etc/sudoers.d/kanku

%exclude %dir /usr
%exclude %dir /usr/bin/
%exclude %dir /usr/sbin/
%exclude %dir /usr/share/
%exclude %dir /usr/lib/

%exclude %dir /etc/profile.d
%config /etc/profile.d/kanku.sh

%exclude %dir %_tmpfilesdir
%_tmpfilesdir/kanku.conf

%dir /usr/lib/kanku/lib/Kanku/NotifyQueue/
/usr/lib/kanku/lib/Kanku/NotifyQueue/*.pm
/usr/lib/kanku/lib/Kanku/Handler/
/usr/lib/kanku/lib/Kanku/Roles/
/usr/lib/kanku/lib/Kanku/Schema/
/usr/lib/kanku/lib/Kanku/Setup/
/usr/lib/kanku/lib/Kanku/Util/
/usr/lib/kanku/lib/Kanku/Util.pm
/usr/lib/kanku/lib/Kanku/Task/
/usr/lib/kanku/lib/OpenStack/
/usr/lib/kanku/lib/Kanku/Config.pm
/usr/lib/kanku/lib/Kanku/Handler.pod
/usr/lib/kanku/lib/Kanku/Notifier
/usr/lib/kanku/lib/Kanku/Job.pm
/usr/lib/kanku/lib/Kanku/RabbitMQ.pm
/usr/lib/kanku/lib/Kanku/Schema.pm
/usr/lib/kanku/lib/Kanku/JobList.pm
/usr/lib/kanku/lib/Kanku/Task.pm
/usr/lib/kanku/lib/Kanku/Airbrake.pm
/usr/lib/kanku/lib/Kanku/NotifyQueue.pm
/usr/lib/kanku/lib/Kanku/GPG.pm
/usr/lib/kanku/lib/Kanku/YAML.pm

%dir /usr/lib/kanku/lib/Kanku/WebSocket
/usr/lib/kanku/lib/Kanku/WebSocket/Notification.pm
/usr/lib/kanku/lib/Kanku/WebSocket/Session.pm

%dir /usr/lib/kanku/lib/Kanku/Airbrake
/usr/lib/kanku/lib/Kanku/Airbrake/Dummy.pm

%dir /usr/lib/kanku/lib/Kanku/LibVirt
/usr/lib/kanku/lib/Kanku/LibVirt/HostList.pm

%dir /usr/lib/kanku/lib/Kanku/Dispatch/
/usr/lib/kanku/lib/Kanku/Dispatch/Local.pm

/usr/lib/kanku/lib/Kanku/Test/

%package cli
Summary:        Command line client for kanku
Requires:       kanku-common = %{version}
Requires:       libvirt-client
Requires(pre):  libvirt-daemon libvirt-daemon-driver-qemu
Requires(pre):  sudo
Requires:       (perl(Passwd::Keyring::Gnome) if gnome-keyring)
Requires:       (perl(Passwd::Keyring::KDEWallet) if kwalletd5)
Requires:       perl(IO::Interactive)
Requires:       perl(Net::AMQP::RabbitMQ)

%description cli
Command line client for kanku, mainly used for setup tasks
and in developer mode.

%post cli
    cat >> %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something << EOF

WARNING: kankus iptables/ss/netstat handling changed.

Please re-run "kanku setup --devel" if you are using kanku in developer mode.


EOF

%files cli
%dir /usr/share/kanku/views/cli/
%dir /usr/share/kanku/views/cli/rjob
/usr/share/kanku/views/cli/*.tt
/usr/share/kanku/views/cli/rjob/*.tt
/usr/lib/kanku/lib/Kanku/Cli/
/usr/lib/kanku/lib/Kanku/Cli.pm
/usr/lib/kanku/iptables_wrapper
/usr/lib/kanku/ss_netstat_wrapper
/etc/bash_completion.d/kanku.sh
%ghost %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something

%package common-server
Summary:        Common server files or settings for kanku
Requires(pre):  libvirt-daemon libvirt-daemon-driver-qemu

%if 0%{?fedora}
Requires(pre):  shadow-utils
%else
Requires(pre):  shadow
%endif

%description common-server
This package contains common server files, settings and dependencies
for the kanku server components like kanku-worker, kanku-dispatcher,
kanku-web, kanku-scheduler and kanku-triggerd.

%pre common-server
getent group %{kanku_group} >/dev/null || groupadd -r %{kanku_group}
getent passwd %{kanku_user} >/dev/null || useradd -r -g %{kanku_group} -G libvirt -d %{kanku_vardir} -s /sbin/nologin -c "user for kanku" %{kanku_user}

%files common-server
%defattr(-, root, root)
%dir %attr(755, kankurun, kanku) /var/lib/kanku
%dir %attr(755, kankurun, kanku) /var/lib/kanku/db
%dir %attr(755, kankurun, kanku) /var/cache/kanku
%ghost %dir %attr(755, kankurun, kanku) /run/kanku

%package web
Summary:        WebUI for kanku
Requires:       kanku-common = %{version}
Requires:       kanku-common-server = %{version}
Requires:       perl(Dancer2::Plugin::WebSocket)
Requires:       perl(Mail::Message::Body::String)
Requires:       perl(Mail::Transport::Send)
Requires:       perl(Net::AMQP::RabbitMQ)
Requires:       perl(Template::Plugin::JSON::Escape)
Requires:       perl(Twiggy)
Requires:       perl(UUID)
%if 0%{?fedora}
Requires:       server(smtp)
%else
Requires:       smtp_daemon
%endif

%description web
WebUI for kanku using perl Dancer

%post web
%systemd_post kanku-web.service

%preun web
%systemd_preun kanku-web.service

%postun web
%systemd_postun_with_restart kanku-web.service

%files web
%attr(755,root,root) /usr/lib/kanku/kanku-app.psgi
%dir %attr(755, kankurun, kanku) /var/lib/kanku/sessions
%dir /usr/share/kanku/views/
%{_unitdir}/kanku-web.service
%{_sbindir}/rckanku-web
/usr/share/kanku/views/admin.tt
/usr/share/kanku/views/guest.tt
/usr/share/kanku/views/index.tt
/usr/share/kanku/views/job.tt
/usr/share/kanku/views/notify.tt
/usr/share/kanku/views/notify_disabled.tt
/usr/share/kanku/views/job_history.tt
/usr/share/kanku/views/job_result.tt
%dir /usr/share/kanku/views/layouts
/usr/share/kanku/views/layouts/main.tt
/usr/share/kanku/views/login.tt
%dir /usr/share/kanku/views/login
/usr/share/kanku/views/login/denied.tt
/usr/share/kanku/views/admin.tt
/usr/share/kanku/views/settings.tt
/usr/share/kanku/views/signup.tt
/usr/share/kanku/views/pwreset.tt
/usr/share/kanku/views/reset_password.tt
/usr/share/kanku/views/worker.tt

%dir /etc/apache2
%dir /etc/apache2/conf.d
%ghost %config (noreplace) /etc/apache2/conf.d/kanku.conf
%config /etc/kanku/jobs/remove-domain.yml

# public contains css/js/bootstrap/jquery etc
/usr/share/kanku/public/
/usr/lib/kanku/lib/Kanku.pm
/usr/lib/kanku/lib/Kanku/REST.pm
/usr/lib/kanku/lib/Kanku/REST

%package worker
Summary:        Worker daemon for kanku

Requires:       kanku-common = %{version}
Requires:       kanku-common-server = %{version}
Requires:       perl(Net::AMQP::RabbitMQ)
Requires:       perl(Sys::CPU)
Requires:       perl(Sys::LoadAvg)
Requires:       perl(Sys::MemInfo)
Requires:       perl(UUID)
%if "%{_arch}" == "x86_64" || "%{_arch}" == "i686"
Requires:       qemu-kvm
%endif
%if "%{_arch}" == "aarch64"
Requires:       qemu-arm
%endif
# apache2 is only needed for delivering console logs
Recommends:     apache2

%description worker
A remote worker for kanku based on RabbitMQ.

%post worker
%systemd_post kanku-worker.service

%preun worker
%systemd_preun kanku-worker.service

%postun worker
%systemd_postun_with_restart kanku-worker.service

%files worker
/etc/apache2/conf.d/kanku-worker.conf
%{_unitdir}/kanku-worker.service
%{_sbindir}/rckanku-worker
%{_sbindir}/kanku-worker
/usr/lib/kanku/lib/Kanku/Daemon/Worker.pm

%package dispatcher
Summary:        Dispatcher daemon for kanku

Requires:       kanku-common = %{version}
Requires:       kanku-common-server = %{version}
Requires:       perl(Net::AMQP::RabbitMQ)
Requires(pre):  sudo
Recommends:     rabbitmq-server

%description dispatcher
A dispatcher for kanku based on RabbitMQ.

%post dispatcher
%systemd_post kanku-dispatcher.service

%preun dispatcher
%systemd_preun kanku-dispatcher.service

%postun dispatcher
%systemd_postun_with_restart kanku-dispatcher.service

%files dispatcher
%{_unitdir}/kanku-dispatcher.service
%{_sbindir}/rckanku-dispatcher
%{_sbindir}/kanku-dispatcher
/usr/lib/kanku/lib/Kanku/Daemon/Dispatcher.pm
/usr/lib/kanku/lib/Kanku/Dispatch/RabbitMQ.pm
/usr/share/kanku/views/notifier/

%package scheduler
Summary:        Scheduler daemon for kanku
Requires:       kanku-common = %{version}
Requires:       kanku-common-server = %{version}

%description scheduler
A scheduler for kanku based on RabbitMQ.

%post scheduler
%systemd_post kanku-scheduler.service

%preun scheduler
%systemd_preun kanku-scheduler.service

%postun scheduler
%systemd_postun_with_restart kanku-scheduler.service

%files scheduler
%attr(755,root,root) %{_sbindir}/kanku-scheduler
/usr/lib/kanku/lib/Kanku/Daemon/Scheduler.pm
%{_unitdir}/kanku-scheduler.service
%{_sbindir}/rckanku-scheduler

%package triggerd
Summary:        Trigger daemon for kanku
Requires:       kanku-common = %{version}
Requires:       kanku-common-server = %{version}

%description triggerd
A triggerd for kanku based on RabbitMQ.

%post triggerd
%systemd_post kanku-triggerd.service

%preun triggerd
%systemd_preun kanku-triggerd.service

%postun triggerd
%systemd_postun_with_restart kanku-triggerd.service

%files triggerd
%attr(755,root,root) %{_sbindir}/kanku-triggerd
%{_unitdir}/kanku-triggerd.service
%{_sbindir}/rckanku-triggerd
%dir /usr/lib/kanku/lib/Kanku/Listener
/usr/lib/kanku/lib/Kanku/Daemon/TriggerD.pm
/usr/lib/kanku/lib/Kanku/Listener/RabbitMQ.pm

%package doc
Summary:        Documentation files for kanku

%description doc
This package contains the documentation files for kanku.

%files doc
%{_defaultdocdir}/kanku/

%package urlwrapper
Summary:        Url wrapper for kanku:// urls
Requires:       desktop-file-utils
Requires:       kanku-cli = %{version}
Requires:       shared-mime-info
Obsoletes:      kanku-url-wrapper

%description urlwrapper
A URL wrapper to start kanku from kanku:// urls in the browser.

%post urlwrapper
update-mime-database /usr/share/mime
update-desktop-database

%preun urlwrapper
update-mime-database /usr/share/mime
update-desktop-database

%postun urlwrapper
update-mime-database /usr/share/mime
update-desktop-database

%files urlwrapper
%attr(644,root,root) /usr/share/applications/kanku-urlwrapper.desktop
%attr(644,root,root) /usr/share/mime/packages/kanku.xml
%dir /usr/share/icons/hicolor
%dir /usr/share/icons/hicolor/32x32
%dir /usr/share/icons/hicolor/32x32/apps
/usr/share/icons/hicolor/32x32/apps/kanku.png
%dir /usr/share/icons/hicolor/48x48
%dir /usr/share/icons/hicolor/48x48/apps
/usr/share/icons/hicolor/48x48/apps/kanku.png
%dir /usr/share/icons/hicolor/64x64
%dir /usr/share/icons/hicolor/64x64/apps
/usr/share/icons/hicolor/64x64/apps/kanku.png

%changelog

%changelog cli

%changelog common
