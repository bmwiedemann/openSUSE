#
# spec file for package rabbitmq-server
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%bcond_without split_plugins

# We want to install into /usr/lib, even on 64-bit platforms
%define _rabbit_libdir %{_exec_prefix}/lib/rabbitmq
%define _rabbit_erllibdir %{_rabbit_libdir}/lib/rabbitmq_server-%{version}

%if %{undefined _initddir}
%define _initddir %{_sysconfdir}/init.d
%endif

%define _make_args DESTDIR="%{buildroot}" PREFIX="%{_exec_prefix}" RMQ_ROOTDIR=%{_rabbit_libdir} RMQ_ERLAPP_DIR=%{_rabbit_erllibdir} MANDIR="%{_mandir}" DOC_INSTALL_DIR=%{buildroot}/%{_docdir} VERSION=%{version} V=1

%define _plugins_state_dir %{_localstatedir}/lib/rabbitmq/plugins
%define _rabbitmqctl_autocomplete scripts/bash_autocomplete.sh
%define _rabbitmq_user rabbitmq
%define _rabbitmq_group rabbitmq

Name:           rabbitmq-server
Version:        3.13.7
Release:        0
Summary:        A message broker supporting AMQP, STOMP and MQTT
License:        MPL-2.0
Group:          System/Daemons
URL:            https://www.rabbitmq.com/
Source:         https://github.com/rabbitmq/rabbitmq-server/releases/download/v%{version}/rabbitmq-server-%{version}.tar.xz
Source1:        https://github.com/rabbitmq/rabbitmq-server/releases/download/v%{version}/rabbitmq-server-%{version}.tar.xz.asc
Source2:        https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc#/%{name}.keyring
Source3:        https://raw.githubusercontent.com/rabbitmq/rabbitmq-packaging/v%{version}/RPMS/Fedora/rabbitmq-server.logrotate
Source4:        rabbitmq-env.conf
Source6:        rabbitmq-server.service
Source7:        https://raw.githubusercontent.com/rabbitmq/rabbitmq-packaging/v%{version}/RPMS/Fedora/rabbitmq-server.tmpfiles
Source8:        README.SUSE
Patch0:         rabbitmq-server-allow-elixir-1.18.patch
BuildRequires:  elixir
# https://www.rabbitmq.com/which-erlang.html
BuildRequires:  erlang >= 25.0
BuildRequires:  erlang-src
BuildRequires:  fdupes
BuildRequires:  hostname
# BuildRequires:  libxslt
BuildRequires:  python3
BuildRequires:  rsync
BuildRequires:  unzip
BuildRequires:  xmlto
BuildRequires:  xz
BuildRequires:  zip
Requires:       erlang >= 25.0
Requires:       erlang-epmd
Requires:       logrotate
Provides:       AMQP-server
Requires(pre):  shadow
Requires(pre):  %fillup_prereq
Requires:       rabbitmq-server-plugins
BuildRequires:  pkgconfig(systemd)
Provides:       group(%{_rabbitmq_group})
Provides:       user(%{_rabbitmq_user})
%{?systemd_ordering}
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
Provides:       erlang-amqp_client = %{version}
Provides:       erlang-gen_server2 = %{version}
Provides:       erlang-rabbit_common = %{version}

%description -n erlang-rabbitmq-client
RabbitMQ is an implementation of an AMQP broker. AMQP is an emerging
standard for messaging.

This package includes the RabbitMQ AMQP language bindings for Erlang.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Optional dependency offering bash completion for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
BuildRequires:  zsh
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Optional dependency offering zsh completion for %{name}.

%prep
%autosetup -p1
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
make install install-bin install-man %{_make_args}

mkdir -p %{buildroot}%{_sbindir}
install -p -D -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}.service
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -D -p -m 0644 %{SOURCE7} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
# Use /run instead of deprecated /var/run in tmpfiles.conf  (bsc#1185075)
sed -i 's/\/var//' %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf

# Install wrapper scripts
sed \
  -e 's|@RABBITMQ_USER@|%{_rabbitmq_user}|' -e 's|@RABBITMQ_GROUP@|%{_rabbitmq_group}|' \
  < scripts/rabbitmq-script-wrapper \
  > %{buildroot}%{_sbindir}/rabbitmqctl
chmod 0755 %{buildroot}%{_sbindir}/rabbitmqctl
for script in rabbitmq-server rabbitmq-plugins rabbitmq-diagnostics rabbitmq-queues rabbitmq-upgrade rabbitmq-streams; do \
  cp -a %{buildroot}%{_sbindir}/rabbitmqctl %{buildroot}%{_sbindir}/$script
done

# install config files
install -p -D -m 0644 deps/rabbit/docs/rabbitmq.conf.example %{buildroot}/%{_sysconfdir}/rabbitmq/rabbitmq.conf
install -p -D -m 0644 deps/rabbit/docs/advanced.config.example %{buildroot}/%{_sysconfdir}/rabbitmq/advanced.config.example
install -p -D -m 0644 deps/rabbit/docs/rabbitmq.conf.example %{buildroot}/%{_sysconfdir}/rabbitmq/rabbitmq.config.example
install -p -D -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/rabbitmq/rabbitmq-env.conf

# Copy all necessary lib files etc.
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/rabbitmq-server

# Install autocomplete scripts
for script in rabbitmqctl rabbitmq-plugins rabbitmq-diagnostics; do
  install -p -D -m 0644 %{_rabbitmqctl_autocomplete} %{buildroot}%{_datadir}/bash-completion/completions/$script
done
install -p -D -m 0644 scripts/zsh_autocomplete.sh %{buildroot}%{_datadir}/zsh/site-functions/_enable_rabbitmqctl_completion

# Install Erlang client
mkdir -p %{buildroot}%{_libdir}/erlang/lib
for i in amqp_client rabbit_common ; do
  cp -r %{buildroot}%{_rabbit_erllibdir}/plugins/$i* -d %{buildroot}%{_libdir}/erlang/lib/
done

# Create other necessary directories for RabbitMQ server
mkdir -p %{buildroot}%{_sysconfdir}/rabbitmq
mkdir -p %{buildroot}%{_localstatedir}/lib/rabbitmq/mnesia
mkdir -p %{buildroot}%{_localstatedir}/log/rabbitmq

# Create hardlinks for duplicate files
%fdupes %{buildroot}/%{_datadir}
%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_sbindir}

%pre
getent group %{_rabbitmq_group} >/dev/null || groupadd -r %{_rabbitmq_group}
getent passwd %{_rabbitmq_user} >/dev/null || useradd -r -g %{_rabbitmq_group} \
  -d %{_localstatedir}/lib/rabbitmq \
  -s /sbin/nologin \
  -c "user for RabbitMQ messaging server" %{_rabbitmq_user}
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
systemd-tmpfiles --create --clean /usr/lib/tmpfiles.d/rabbitmq-server.conf

%preun
# Clean out plugin activation state, both on uninstall and upgrade
rm -rf %{_plugins_state_dir}
for ext in rel script boot ; do
    rm -f %{_rabbit_erllibdir}/ebin/rabbit.$ext
done

%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%config(noreplace) %{_sysconfdir}/logrotate.d/rabbitmq-server
%config(noreplace) %{_sysconfdir}/rabbitmq/
%{_rabbit_libdir}
%if %{with split_plugins}
%exclude %{_rabbit_erllibdir}/plugins/rabbitmq_*
%endif
#
%{_unitdir}/%{name}.service
/usr/lib/tmpfiles.d/rabbitmq-server.conf
#
%attr(0755, rabbitmq, rabbitmq) %dir %{_localstatedir}/lib/rabbitmq
%attr(0750, rabbitmq, rabbitmq) %dir %{_localstatedir}/lib/rabbitmq/mnesia
%attr(0755, rabbitmq, rabbitmq) %dir %{_localstatedir}/log/rabbitmq
#
%{_sbindir}/rabbitmq-plugins
%{_sbindir}/rabbitmq-server
%{_sbindir}/rabbitmqctl
%{_sbindir}/rabbitmq-queues
%{_sbindir}/rabbitmq-upgrade
%{_sbindir}/rcrabbitmq-server
%{_sbindir}/rabbitmq-diagnostics
%{_sbindir}/rabbitmq-streams

#
%license LICENSE*
%doc README* CODE_OF_CONDUCT.md CONTRIBUTING.md deps/rabbit/docs/set_rabbitmq_policy.sh.example
%{_mandir}/man5/rabbitmq-env.conf.5%{?ext_man}
%{_mandir}/man8/rabbitmq*.8%{?ext_man}
# E: script-without-shebang
%exclude %{_rabbit_libdir}/autocomplete/bash_autocomplete.sh
%exclude %{_rabbit_libdir}/autocomplete/zsh_autocomplete.sh

%if %{with split_plugins}
%files plugins
%{_rabbit_erllibdir}/plugins/rabbitmq_*
%endif

%files -n erlang-rabbitmq-client
%{_libdir}/erlang/lib/amqp_client*/
%{_libdir}/erlang/lib/rabbit_common*/

%files bash-completion
%{_datadir}/bash-completion/completions/rabbitmq*

%files zsh-completion
%{_datadir}/zsh/site-functions/_enable_rabbitmqctl_completion

%changelog
