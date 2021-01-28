#
# spec file for package monero
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


Name:           monero
Version:        0.17.1.9
Release:        0
Summary:        P2P digital currency
License:        MIT
Group:          Productivity/Networking/Other
URL:            https://get%{name}.org/
Source0:        %{name}-%{version}.tar.gz
%if 0%{?suse_version} > 1320
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
%if 0%{?is_opensuse} && 0%{?suse_version} == 1315 && 0%{?sle_version} >= 120200
BuildRequires:  boost-devel >= 1.58
%else
BuildRequires:  boost_1_58_0-devel
%endif
%endif
BuildRequires:  cmake >= 3.0
BuildRequires:  cppzmq-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 4.7.3
BuildRequires:  graphviz
BuildRequires:  ldns-devel >= 1.6.17
BuildRequires:  libevent-devel >= 2.0
BuildRequires:  libexpat-devel >= 1.1
BuildRequires:  libminiupnpc-devel >= 2.0
BuildRequires:  libopenssl-devel
BuildRequires:  libsodium-devel
BuildRequires:  libunwind-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
%if 0%{?is_opensuse} && 0%{?suse_version} == 1315 && 0%{?sle_version} >= 120200
BuildRequires:  shadow
%endif
BuildRequires:  unbound-devel >= 1.4.16
BuildRequires:  xz-devel

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

%package devel-static
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-static
%{description_text_1}
%{description_text_2}
%{description_text_3}
%{description_text_4}

This package provides static libraries for %{name}.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/Man
BuildArch:      noarch

%description doc
%{description_text_1}
%{description_text_2}
%{description_text_3}
%{description_text_4}

This package contains the documentation for %{name}.

%prep
%autosetup -p1

# setup systemd service
%{__sed} -i 's#^Description=Monero Full Node$#Description=%{display_name} Daemon#g' utils/systemd/%{daemon_name}.service
%{__sed} -i 's#^PIDFile=/run/monero/monerod.pid$#PIDFile=%{_rundir}/%{name}/%{daemon_name}.pid#g' utils/systemd/%{daemon_name}.service
%{__sed} -i 's#^ExecStart=/usr/bin/monerod --config-file /etc/monerod.conf \\$#ExecStart=%{_bindir}/%{daemon_name} --detach --pidfile %{_rundir}/%{name}/%{daemon_name}.pid --config-file=%{_sysconfdir}/%{name}.conf --data-dir=%{_localstatedir}/lib/%{name}#g' utils/systemd/%{daemon_name}.service
%{__sed} -i 's#^    --detach --pidfile /run/monero/monerod.pid#ExecReload=/bin/kill -HUP \$MAINPID#g' utils/systemd/%{daemon_name}.service
%{__sed} -i 's#^User=monero$#User=%{name}#g' utils/systemd/%{daemon_name}.service
%{__sed} -i 's#^Group=monero$#Group=%{name}#g' utils/systemd/%{daemon_name}.service

# setup default config file
%{__sed} -i 's#monerod#%{daemon_name}#g' utils/conf/%{daemon_name}.conf
%{__sed} -i 's#^data-dir=/var/lib/monero$#data-dir=%{_localstatedir}/lib/%{name}#g' utils/conf/%{daemon_name}.conf
%{__sed} -i 's#wlog-file=/var/log/monero/monero.log$#log-file=%{_localstatedir}/log/%{name}/%{name}.log#g' utils/conf/%{daemon_name}.conf

# setup run folder
echo "d %{_rundir}/%{name} 0770 root %{name}" > rundir.conf

%build
%{__mkdir_p} build/release
cd build/release
%{__cmake} -DARCH=default -DBUILD_TESTS=OFF -DBUILD_GUI_DEPS=ON -DCMAKE_BUILD_TYPE=release ../..
%make_jobs
%{__strip} -s bin/%{daemon_name}
%{__strip} -s bin/%{cli_name}
%{__strip} -s bin/%{rpc_name}
%{__strip} -s bin/%{gen_name}
%{__strip} -s bin/%{bc_ancestry_name}
%{__strip} -s bin/%{bc_depth_name}
%{__strip} -s bin/%{bc_export_name}
%{__strip} -s bin/%{bc_import_name}
%{__strip} -s bin/%{bc_outputs_name}
%{__strip} -s bin/%{bc_usage_name}
cd ../..
HAVE_DOT=YES %{_bindir}/doxygen Doxyfile

%install
# install binaries
%{__install} -D -m 0755 build/release/bin/%{daemon_name} %{buildroot}%{_bindir}/%{daemon_name}
%{__install} -D -m 0755 build/release/bin/%{cli_name} %{buildroot}%{_bindir}/%{cli_name}
%{__install} -D -m 0755 build/release/bin/%{rpc_name} %{buildroot}%{_bindir}/%{rpc_name}
%{__install} -D -m 0755 build/release/bin/%{gen_name} %{buildroot}%{_bindir}/%{gen_name}
%{__install} -D -m 0755 build/release/bin/%{bc_ancestry_name} %{buildroot}%{_bindir}/%{bc_ancestry_name}
%{__install} -D -m 0755 build/release/bin/%{bc_depth_name} %{buildroot}%{_bindir}/%{bc_depth_name}
%{__install} -D -m 0755 build/release/bin/%{bc_export_name} %{buildroot}%{_bindir}/%{bc_export_name}
%{__install} -D -m 0755 build/release/bin/%{bc_import_name} %{buildroot}%{_bindir}/%{bc_import_name}
%{__install} -D -m 0755 build/release/bin/%{bc_outputs_name} %{buildroot}%{_bindir}/%{bc_outputs_name}
%{__install} -D -m 0755 build/release/bin/%{bc_usage_name} %{buildroot}%{_bindir}/%{bc_usage_name}

# install libraries
%{__install} -d -m 0755 %{buildroot}%{_includedir}/%{name}/epee/net %{buildroot}%{_includedir}/%{name}/epee/serialization %{buildroot}%{_includedir}/%{name}/epee/storages
%{__install} -D -m 0644 -t %{buildroot}%{_includedir}/%{name}/epee contrib/epee/include/*.h
%{__install} -D -m 0644 -t %{buildroot}%{_includedir}/%{name}/epee/net contrib/epee/include/net/*.h
%{__install} -D -m 0644 -t %{buildroot}%{_includedir}/%{name}/epee/serialization contrib/epee/include/serialization/*.h
%{__install} -D -m 0644 -t %{buildroot}%{_includedir}/%{name}/epee/storages contrib/epee/include/storages/*.h
%{__install} -D -m 0644 src/wallet/api/wallet2_api.h %{buildroot}%{_includedir}/%{name}/wallet/api/wallet2_api.h
%{__install} -D -m 0644 build/release/contrib/epee/src/libepee.a %{buildroot}%{_libdir}/libepee.a
%{__install} -D -m 0644 build/release/contrib/epee/src/libepee_readline.a %{buildroot}%{_libdir}/libepee_readline.a
%{__install} -D -m 0644 build/release/lib/libwallet.a %{buildroot}%{_libdir}/libwallet.a
%{__install} -D -m 0644 build/release/lib/libwallet_merged.a %{buildroot}%{_libdir}/libwallet_merged.a

# install daemon supplementary files
%{__install} -D -m 0644 utils/conf/%{daemon_name}.conf  %{buildroot}%{_sysconfdir}/%{name}.conf
%{__install} -D -m 0644 utils/systemd/%{daemon_name}.service %{buildroot}%{_unitdir}/%{daemon_name}.service
%{__mkdir_p} %{buildroot}%{_localstatedir}/lib/%{name}
%{__mkdir_p} %{buildroot}%{_localstatedir}/log/%{name}
%{__install} -d -m 0755 %{buildroot}%{_sbindir}
%{__ln_s} %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{daemon_name}

# install run folder configuration
%{__install} -D -m 0644 rundir.conf %{buildroot}/%{_tmpfilesdir}/%{name}_rundir.conf

# install documentation
%{__install} -d -m 0755 %{buildroot}%{_defaultdocdir}/%{name}
%{__install} -m 0644 -p -t %{buildroot}%{_defaultdocdir}/%{name} CONTRIBUTING.md README.i18n.md README.md
%{__install} -d -m 0755 %{buildroot}%{_defaultlicensedir}/%{name}
%{__install} -m 0644 -p -t %{buildroot}%{_defaultlicensedir}/%{name} LICENSE
%{__cp} -a doc/html %{buildroot}%{_defaultdocdir}/%{name}/
%fdupes %{buildroot}%{_defaultdocdir}/%{name}

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
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{cli_name}
%attr(755,root,root) %{_bindir}/%{rpc_name}
%attr(755,root,root) %{_bindir}/%{gen_name}
%attr(755,root,root) %{_bindir}/%{bc_ancestry_name}
%attr(755,root,root) %{_bindir}/%{bc_depth_name}
%attr(755,root,root) %{_bindir}/%{bc_export_name}
%attr(755,root,root) %{_bindir}/%{bc_import_name}
%attr(755,root,root) %{_bindir}/%{bc_outputs_name}
%attr(755,root,root) %{_bindir}/%{bc_usage_name}

%files -n %{daemon_name}
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{daemon_name}
%{_sbindir}/rc%{daemon_name}
%{_unitdir}/%{daemon_name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %attr(700,%{name},%{name}) %{_localstatedir}/lib/%{name}
%dir %attr(700,%{name},%{name}) %{_localstatedir}/log/%{name}
%ghost %{_rundir}/%{name}
%{_tmpfilesdir}
%{_tmpfilesdir}/%{name}_rundir.conf

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}

%files devel-static
%defattr(-,root,root,-)
%attr(644,root,root) %{_libdir}/*.a

%files doc
%defattr(-,root,root,-)
%{_defaultdocdir}/%{name}/
%{_defaultlicensedir}/%{name}/

%changelog
