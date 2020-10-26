#
# spec file for package rabbitmq-server
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%bcond_without split_plugins

%define _rabbit_erllibdir %{_libdir}/rabbitmq/lib/rabbitmq_server-%{version}
%define _rabbit_libdir %{_libdir}/rabbitmq

%if %{undefined _initddir}
%define _initddir %{_sysconfdir}/init.d
%endif

%define _make_args DESTDIR="%{buildroot}" PREFIX="%{_prefix}" RMQ_ROOTDIR=%{_rabbit_libdir} RMQ_ERLAPP_DIR=%{_rabbit_erllibdir} MAN_INSTALL_PATH="%{_mandir}" DOC_INSTALL_DIR=%{buildroot}/%{_docdir} VERSION=%{version} V=1

Name:           rabbitmq-server
Version:        3.8.9
Release:        0
Summary:        A message broker supporting AMQP, STOMP and MQTT
License:        MPL-2.0
Group:          System/Daemons
URL:            http://www.rabbitmq.com/
Source:         https://github.com/rabbitmq/rabbitmq-server/releases/download/v%{version}/rabbitmq-server-%{version}.tar.xz
Source1:        rabbitmq-server.init
# This comes from: http://hg.rabbitmq.com/rabbitmq-server/raw-file/2da625c0a436/packaging/common/rabbitmq-script-wrapper
Source2:        rabbitmq-script-wrapper
Source3:        rabbitmq-server.logrotate
Source4:        rabbitmq-env.conf
Source5:        rabbitmq-server.sysconfig
Source6:        rabbitmq-server.service
Source7:        rabbitmq-server.tmpfiles.d.conf
Source8:        README.SUSE
# from https://raw.githubusercontent.com/rabbitmq/rabbitmq-server/v3.7.x/docs/rabbitmq.conf.example
Source9:        rabbitmq.conf.example
Source10:       advanced.config.example
Source11:       rabbitmq.config.example
BuildRequires:  elixir
# https://www.rabbitmq.com/which-erlang.html
BuildRequires:  erlang >= 21.3
BuildRequires:  erlang-src
BuildRequires:  fdupes
BuildRequires:  libxslt
BuildRequires:  python3
BuildRequires:  rsync
BuildRequires:  unzip
BuildRequires:  xmlto
BuildRequires:  xz
BuildRequires:  zip
Requires:       erlang >= 21.3
Requires:       erlang-epmd
Requires:       logrotate
Provides:       AMQP-server
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(pre):  shadow
Requires(pre):  %fillup_prereq
Requires(pre):  %insserv_prereq
Requires:       rabbitmq-server-plugins
%if 0%{?suse_version} > 1140
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%define have_systemd 1
Requires:       socat
%else
Requires:       %fillup_prereq
Requires:       %insserv_prereq
%endif
# Do not use noarch since the Erlang packaging does not really allow that
#BuildArch:      noarch

%description
RabbitMQ is an implementation of an AMQP broker. AMQP is an emerging
standard for messaging.

%package plugins
Summary:        Plugins for the RabbitMQ server
Group:          System/Daemons
Requires:       rabbitmq-server = %{version}

%description plugins
RabbitMQ is an implementation of an AMQP broker. AMQP is an emerging
standard for messaging.

This package includes some plugins for the RabbitMQ server.

%package -n erlang-rabbitmq-client
Summary:        RabbitMQ AMQP language bindings for Erlang
Group:          Development/Libraries/Other
Requires:       erlang
Provides:       erlang-gen_server2 = %{version}

%description -n erlang-rabbitmq-client
RabbitMQ is an implementation of an AMQP broker. AMQP is an emerging
standard for messaging.

This package includes the RabbitMQ AMQP language bindings for Erlang.

%prep
%setup -q
cp %{SOURCE8} .

%build
# Make elixir happy with Unicode
export LANG=en_US.UTF-8
export PYTHON=%{_bindir}/python3
make all %{_make_args} %{?_smp_mflags}

%install
# Make elixir happy with Unicode
export LANG=en_US.UTF-8
export PYTHON=%{_bindir}/python3
make install %{_make_args}

mkdir -p %{buildroot}%{_sbindir}
%if 0%{?have_systemd}
install -p -D -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}.service
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -p -D -m 0644 %{SOURCE7} %{buildroot}/usr/lib/tmpfiles.d/rabbitmq-server.conf
%else
# Install init scripts
install -p -D -m 0755 %{SOURCE1} %{buildroot}%{_initddir}/rabbitmq-server
ln -sf %{_initddir}/rabbitmq-server %{buildroot}%{_sbindir}/rcrabbitmq-server
mkdir -p %{buildroot}%{_fillupdir}/
install -p -D -m 644 %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.rabbitmq-server
%endif

# Install wrapper scripts
%define _rabbit_wrapper %{_builddir}/`basename %{SOURCE2}`
cp %{SOURCE2} %{_rabbit_wrapper}
sed -i 's|@SU_RABBITMQ_SH_C@|su rabbitmq -s /bin/sh -c|' %{_rabbit_wrapper}
sed -i 's|@RABBITMQ_ROOT@|%{_rabbit_erllibdir}/|' %{_rabbit_wrapper}
install -p -D -m 0755 %{_rabbit_wrapper} %{buildroot}%{_sbindir}/rabbitmqctl
install -p -D -m 0755 %{_rabbit_wrapper} %{buildroot}%{_sbindir}/rabbitmq-server
install -p -D -m 0755 %{_rabbit_wrapper} %{buildroot}%{_sbindir}/rabbitmq-plugins
install -p -D -m 0755 %{_rabbit_wrapper} %{buildroot}%{_sbindir}/rabbitmq-diagnostics
install -p -D -m 0755 %{_rabbit_wrapper} %{buildroot}%{_sbindir}/rabbitmq-queues
install -p -D -m 0755 %{_rabbit_wrapper} %{buildroot}%{_sbindir}/rabbitmq-upgrade
install -p -D -m 0755 scripts/rabbitmq-server.ocf %{buildroot}%{_exec_prefix}/lib/ocf/resource.d/rabbitmq/rabbitmq-server
install -p -D -m 0755 scripts/rabbitmq-server-ha.ocf %{buildroot}%{_exec_prefix}/lib/ocf/resource.d/rabbitmq/rabbitmq-server-ha

# install config files
install -p -D -m 0644 %{SOURCE9} %{buildroot}/%{_sysconfdir}/rabbitmq/rabbitmq.conf
install -p -D -m 0644 %{SOURCE10} %{buildroot}/%{_sysconfdir}/rabbitmq/advanced.config.example
install -p -D -m 0644 %{SOURCE11} %{buildroot}/%{_sysconfdir}/rabbitmq/rabbitmq.config.example
install -p -D -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/rabbitmq/rabbitmq-env.conf

# Copy all necessary lib files etc.
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/rabbitmq-server

# Install Erlang client
mkdir -p %{buildroot}%{_libdir}/erlang/lib
for i in amqp_client rabbit_common ; do
   unzip %{buildroot}%{_rabbit_erllibdir}/plugins/$i*.ez -d %{buildroot}%{_libdir}/erlang/lib
done

# Create other necessary directories for RabbitMQ server
mkdir -p %{buildroot}%{_sysconfdir}/rabbitmq
mkdir -p %{buildroot}%{_localstatedir}/lib/rabbitmq/mnesia
mkdir -p %{buildroot}%{_localstatedir}/log/rabbitmq

# Create hardlinks for duplicate files
%fdupes %{buildroot}/usr/share

%pre
getent group rabbitmq >/dev/null || groupadd -r rabbitmq
getent passwd rabbitmq >/dev/null || useradd -r -g rabbitmq \
  -d %{_localstatedir}/lib/rabbitmq \
  -s /sbin/nologin \
  -c "user for RabbitMQ messaging server" rabbitmq
%if 0%{?have_systemd}
%service_add_pre %{name}.service
%endif

%post
%if 0%{?have_systemd}
%service_add_post %{name}.service
systemd-tmpfiles --create --clean /usr/lib/tmpfiles.d/rabbitmq-server.conf
%else
%fillup_and_insserv rabbitmq-server
%endif

%preun
%if 0%{?have_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal rabbitmq-server
%endif

%postun
%if 0%{?have_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update rabbitmq-server
%insserv_cleanup
%endif

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/logrotate.d/rabbitmq-server
%config(noreplace) %{_sysconfdir}/rabbitmq/
%{_rabbit_libdir}
%if %{with split_plugins}
%exclude %{_rabbit_erllibdir}/plugins/rabbitmq_*
%endif
#
%if 0%{?have_systemd}
%{_unitdir}/%{name}.service
/usr/lib/tmpfiles.d/rabbitmq-server.conf
%else
%{_initddir}/rabbitmq-server
%dir %attr(0755, rabbitmq, rabbitmq) %{_localstatedir}/run/rabbitmq
%endif
#
%attr(0750, rabbitmq, rabbitmq) %dir %{_localstatedir}/lib/rabbitmq
%attr(0750, rabbitmq, rabbitmq) %dir %{_localstatedir}/log/rabbitmq
#
%{_sbindir}/rabbitmq-plugins
%{_sbindir}/rabbitmq-server
%{_sbindir}/rabbitmqctl
%{_sbindir}/rabbitmq-queues
%{_sbindir}/rabbitmq-upgrade
%{_sbindir}/rcrabbitmq-server
%{_sbindir}/rabbitmq-diagnostics
#
%dir /usr/lib/ocf/
%dir /usr/lib/ocf/resource.d/
/usr/lib/ocf/resource.d/rabbitmq/
#
%license LICENSE*
%doc README* CODE_OF_CONDUCT.md CONTRIBUTING.md

%if %{with split_plugins}
%files plugins
%defattr(-,root,root)
%{_rabbit_erllibdir}/plugins/rabbitmq_*
%endif

%files -n erlang-rabbitmq-client
%defattr(-,root,root)
%{_libdir}/erlang/lib/amqp_client*/
%{_libdir}/erlang/lib/rabbit_common*/

%changelog
