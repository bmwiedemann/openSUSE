#
# spec file for package monero
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


# set binary names
%define daemon_name %{name}d
%define display_name Monero
%define cli_name %{name}-wallet-cli
%define rpc_name %{name}-wallet-rpc
%define gen_name %{name}-gen-trusted-multisig
%define bc_ancestry_name %{name}-blockchain-ancestry
%define bc_depth_name %{name}-blockchain-depth
%define bc_export_name %{name}-blockchain-export
%define bc_import_name %{name}-blockchain-import
%define bc_outputs_name %{name}-blockchain-mark-spent-outputs
%define bc_usage_name %{name}-blockchain-usage
# set ports
%define p2p_port 18080
%define rpc_port 18081
%define description_text_1 Monero is a private, secure, untraceable, decentralised digital currency. You are your bank, you control your funds, and nobody can trace your transfers unless you allow them to do so.
%define description_text_2 Privacy: Monero uses a cryptographically sound system to allow you to send and receive funds without your transactions being easily revealed on the blockchain (the ledger of transactions that everyone has). This ensures that your purchases, receipts, and all transfers remain absolutely private by default.
%define description_text_3 Security: Using the power of a distributed peer-to-peer consensus network, every transaction on the network is cryptographically secured. Individual wallets have a 24 word mnemonic seed that is only displayed once, and can be written down to backup the wallet. Wallet files are encrypted with a passphrase to ensure they are useless if stolen.
%define description_text_4 Untraceability: By taking advantage of ring signatures, a special property of a certain type of cryptography, Monero is able to ensure that transactions are not only untraceable, but have an optional measure of ambiguity that ensures that transactions cannot easily be tied back to an individual user or computer.
Name:           monero
Version:        0.18.2.0
Release:        0
Summary:        P2P digital currency
License:        MIT
Group:          Productivity/Networking/Other
URL:            https://get%{name}.org/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.0
BuildRequires:  cppzmq-devel
BuildRequires:  gcc-c++ >= 4.7.3
BuildRequires:  ldns-devel >= 1.6.17
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libevent-devel >= 2.0
BuildRequires:  libexpat-devel >= 1.1
BuildRequires:  libminiupnpc-devel >= 2.0
BuildRequires:  libopenssl-devel
BuildRequires:  libsodium-devel
BuildRequires:  libunwind-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  shadow
BuildRequires:  unbound-devel >= 1.4.16
BuildRequires:  xz-devel

%description
%{description_text_1}
%{description_text_2}
%{description_text_3}
%{description_text_4}

%package utils
Summary:        Utils for the %{display_name} crypto-currency
Group:          Productivity/Networking/Other

%description utils
%{description_text_1}
%{description_text_2}
%{description_text_3}
%{description_text_4}

This package provides %{display_name}-CLI, a command line interface for %{display_name}.

%package -n %{daemon_name}
Summary:        Headless daemon for %{name} crypto-currency
Group:          Productivity/Networking/Other

%description -n %{daemon_name}
%{description_text_1}
%{description_text_2}
%{description_text_3}
%{description_text_4}

This package provides %{daemon_name}, a headless %{name} daemon.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++

%description devel
%{description_text_1}
%{description_text_2}
%{description_text_3}
%{description_text_4}

The %{name}-devel package contains libraries and header files for developing applications that use %{name}.

%prep
%autosetup -p1

# setup systemd service
sed -i 's#^Description=Monero Full Node$#Description=%{display_name} Daemon#g' utils/systemd/%{daemon_name}.service
sed -i 's#^PIDFile=/run/monero/monerod.pid$#PIDFile=%{_rundir}/%{name}/%{daemon_name}.pid#g' utils/systemd/%{daemon_name}.service
sed -i 's#^ExecStart=%{_bindir}/monerod --config-file %{_sysconfdir}/monerod.conf \\$#ExecStart=%{_bindir}/%{daemon_name} --detach --pidfile %{_rundir}/%{name}/%{daemon_name}.pid --config-file=%{_sysconfdir}/%{name}.conf --data-dir=%{_localstatedir}/lib/%{name}#g' utils/systemd/%{daemon_name}.service
sed -i 's#^    --detach --pidfile /run/monero/monerod.pid#ExecReload=/bin/kill -HUP \$MAINPID#g' utils/systemd/%{daemon_name}.service
sed -i 's#^User=monero$#User=%{name}#g' utils/systemd/%{daemon_name}.service
sed -i 's#^Group=monero$#Group=%{name}#g' utils/systemd/%{daemon_name}.service

# setup default config file
sed -i 's#monerod#%{daemon_name}#g' utils/conf/%{daemon_name}.conf
sed -i 's#^data-dir=%{_localstatedir}/lib/monero$#data-dir=%{_localstatedir}/lib/%{name}#g' utils/conf/%{daemon_name}.conf
sed -i 's#wlog-file=%{_localstatedir}/log/monero/monero.log$#log-file=%{_localstatedir}/log/%{name}/%{name}.log#g' utils/conf/%{daemon_name}.conf

# setup run folder
echo "d %{_rundir}/%{name} 0770 root %{name}" > rundir.conf

%build
%define __builder ninja
%cmake \
  -DARCH=default \
  -DBUILD_TESTS=OFF \
  -DBUILD_GUI_DEPS=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DCMAKE_EXE_LINKER_FLAGS="%{?build_ldflags}" \
  -DCMAKE_MODULE_LINKER_FLAGS="%{?build_ldflags}" \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags}"
%cmake_build

%install
%cmake_install

# remove not needed static libraries
rm -rf %{buildroot}%{_prefix}/lib*

# install daemon supplementary files
install -D -m 0644 utils/conf/%{daemon_name}.conf  %{buildroot}%{_sysconfdir}/%{name}.conf
install -D -m 0644 utils/systemd/%{daemon_name}.service %{buildroot}%{_unitdir}/%{daemon_name}.service
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
install -d -m 0755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{daemon_name}

# install run folder configuration
install -D -m 0644 rundir.conf %{buildroot}/%{_tmpfilesdir}/%{name}_rundir.conf

%pre -n %{daemon_name}
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "%{name} daemon" %{name}
%service_add_pre %{daemon_name}.service

%preun -n %{daemon_name}
%service_del_preun %{daemon_name}.service

%post -n %{daemon_name}
%service_add_post %{daemon_name}.service
%if 0%{?suse_version} && ( 0%{?suse_version} > 1320 || ( 0%{?is_opensuse} && 0%{?suse_version} == 1315 && 0%{?sle_version} && 0%{?sle_version} >= 120100 ) )
%tmpfiles_create %{_tmpfilesdir}/%{name}_rundir.conf
%else
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}_rundir.conf >/dev/null 2>&1 || :
%endif

%postun -n %{daemon_name}
%service_del_postun %{daemon_name}.service

%files utils
%{_bindir}/%{cli_name}
%{_bindir}/%{rpc_name}
%{_bindir}/%{gen_name}
%{_bindir}/%{bc_ancestry_name}
%{_bindir}/%{bc_depth_name}
%{_bindir}/%{bc_export_name}
%{_bindir}/%{bc_import_name}
%{_bindir}/%{bc_outputs_name}
%{_bindir}/%{bc_usage_name}
%{_bindir}/monero-blockchain-prune
%{_bindir}/monero-blockchain-prune-known-spent-data
%{_bindir}/monero-blockchain-stats
%{_bindir}/monero-gen-ssl-cert

%files -n %{daemon_name}
%license LICENSE
%{_bindir}/%{daemon_name}
%{_sbindir}/rc%{daemon_name}
%{_unitdir}/%{daemon_name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %attr(700,%{name},%{name}) %{_localstatedir}/lib/%{name}
%dir %attr(700,%{name},%{name}) %{_localstatedir}/log/%{name}
%ghost %{_rundir}/%{name}
%{_tmpfilesdir}
%{_tmpfilesdir}/%{name}_rundir.conf

%files devel
%{_includedir}/wallet

%changelog
