#
# spec file for package google-extension-manager
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2026 SUSE LLC and contributors
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


%define guest_agent_base_addons_dir %{_exec_prefix}/lib/google/guest_agent
%define telemetry_ext_dir %{guest_agent_base_addons_dir}/GuestTelemetryExtension
%define mgd_wrk_ld_dir %{guest_agent_base_addons_dir}/ManagedWorkloadIdentityExtension
%define core_plugin_dir %{guest_agent_base_addons_dir}/GuestAgentCorePlugin

%define upstream_name google-guest-agent

Name:           google-extension-manager
Version:        20260903.01
Release:        0
Summary:        Google Cloud Guest Agent
License:        Apache-2.0
Group:          System/Daemons
URL:            https://%{provider_prefix}
Source0:        %{upstream_name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        rpmlintrc
BuildRequires:  golang-packaging
BuildRequires:  protobuf-devel
BuildRequires:  protoc-gen-go
BuildRequires:  protoc-gen-go-grpc
BuildRequires:  golang(API) = 1.25
Requires:       google-guest-agent >= 20260903.01
Requires:       google-guest-configs
Requires:       google-guest-oslogin >= 20231003
Provides:       google-compute-engine-init = %{version}
Obsoletes:      google-compute-engine-init < %{version}
BuildRoot:      %{_tmppath}/%{upstream_name}-%{version}-build

%{go_nostrip}
%{go_provides}

%description
Google Cloud Guest Agent

%prep
%setup -n %{upstream_name}-%{version} -a1

%build
sed -i s/google_guest_agent/google_guest_agent_manager/ build/configs/usr/lib/systemd/system/google-guest-agent.service
%goprep %{import_path}
make

%install
# binaries
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{telemetry_ext_dir}
install -d %{buildroot}%{mgd_wrk_ld_dir}
#install -d %{buildroot}%{core_plugin_dir}
install -p -m 0755 cmd/gce_metadata_script_runner/gce_metadata_script_runner %{buildroot}%{_bindir}/gce_metadata_script_runner
# Executable gets renamed to not conflict with the old sources in the fallback package
install -p -m 0755 cmd/google_guest_agent/google_guest_agent %{buildroot}%{_bindir}/google_guest_agent_manager
install -p -m 0755 cmd/ggactl/ggactl_plugin %{buildroot}%{_bindir}/ggactl_plugin
# # At present while we use both code-bases, new and old, we do not want the compat manager
#install -p -m 0755 cmd/google_guest_compat_manager/google_guest_compat_manager %{buildroot}%{_bindir}/google_guest_compat_manager
install -p -m 0755 cmd/metadata_script_runner_compat/gce_compat_metadata_script_runner %{buildroot}%{_bindir}/gce_compat_metadata_script_runner
# Telemetry
install -p -m 0755 cmd/guest_telemetry_extension/guest_telemetry %{buildroot}%{telemetry_ext_dir}/guest_telemetry
install -p -m 0644 build/configs/usr/lib/google/guest_agent/GuestTelemetryExtension/manifest.binpb %{buildroot}%{telemetry_ext_dir}/manifest.binpb
# Plugins
# At present while we use both code-bases, new and old, we do not want the core plugin
#install -p -m 0755 cmd/core_plugin/core_plugin %{buildroot}%{core_plugin_dir}/core_plugin
#install -p -m 0755 build/configs/%{core_plugin_dir}/manifest.binpb %{buildroot}%{core_plugin_dir}/manifest.binpb
# configuration files
install -d %{buildroot}%{_sysconfdir}/default
install -p -m 0644 build/configs/usr/share/google-guest-agent/instance_configs.cfg %{buildroot}%{_sysconfdir}/default/instance_configs.cfg
# systemd unit files
install -d %{buildroot}%{_unitdir}
install -p -m 0644 build/configs/usr/lib/systemd/system/google-guest-agent.service %{buildroot}%{_unitdir}/google-guest-agent-manager.service
mkdir -p %{buildroot}%{_sbindir}
for srv_name in %{buildroot}%{_unitdir}/*.service; do rc_name=$(basename -s '.service' $srv_name); ln -s service %{buildroot}%{_sbindir}/rc$rc_name; done

%pre
    if [ -f /usr/lib/systemd/system/google-ip-forwarding-daemon.service ]; then
        systemctl stop --no-block google-ip-forwarding-daemon
        systemctl disable google-ip-forwarding-daemon.service
    fi
    if [ -f /usr/lib/systemd/system/google-network-setup.service ]; then
        systemctl stop --no-block google-network-setup
        systemctl disable google-network-setup.service
    fi
    %service_add_pre google-guest-agent-manager.service google-shutdown-scripts.service google-startup-scripts.service

%preun
    %service_del_preun google-guest-agent-manager.service google-shutdown-scripts.service google-startup-scripts.service

%post
    # Handle enabling of services during an upgrade from the old google-compute-engine-init package
    if [ "$1" = "1" ] && ! [ -e /.buildenv ] && systemctl is-enabled -q google-accounts-daemon.service 2>/dev/null ; then
    	mktemp --suffix ".google-accounts-daemon-enabled"
    	if systemctl is-active --quiet google-accounts-daemon.service ; then
    	    mktemp --suffix ".google-accounts-daemon-active"
    	fi
    fi
    if [ "$1" = "1" ] && ! [ -e /.buildenv ] && systemctl is-enabled -q google-startup-scripts.service 2>/dev/null ; then
    	mktemp --suffix ".google-startup-scripts"
    fi
    if [ "$1" = "1" ] && ! [ -e /.buildenv ] && systemctl is-enabled -q google-shutdown-scripts.service 2>/dev/null ; then
    	mktemp --suffix ".google-shutdown-scripts"
    fi
    # Handle enabling of the new google-guest-agent-manager service and then
    # disable he old service google-guest-agent.service if the old service
    # was enabled
    if [ "$1" = "1" ] && ! [ -e /.buildenv ] && systemctl is-enabled -q google-guest-agent.service 2>/dev/null ; then
    	mktemp --suffix ".google-guest-agent"
    fi

    %service_add_post google-guest-agent-manager.service google-shutdown-scripts.service google-startup-scripts.service

%posttrans
    if ! [ -e /.buildenv ] && [ -f /tmp/tmp\.[A-Z,a-z,0-9]*\.google-accounts-daemon-enabled ] ; then
        systemctl enable google-guest-agent.service
    	rm -f /tmp/tmp\.[A-Z,a-z,0-9]*\.google-accounts-daemon-enabled
    	if [ -f /tmp/tmp\.[A-Z,a-z,0-9]*\.google-accounts-daemon-enabled ] ; then
    	    systemctl stop google-accounts-daemon.service
    	    systemctl start google-guest-agent.service
    	    rm -f /tmp/tmp\.[A-Z,a-z,0-9]*\.google-accounts-daemon-active
    	fi
    fi

%postun
    %service_del_postun google-guest-agent.service

%files
%defattr(0644,root,root,0755)
%license LICENSE
%dir %{_exec_prefix}/lib/google
%dir %{guest_agent_base_addons_dir}
%dir %{telemetry_ext_dir}
%dir %{mgd_wrk_ld_dir}
%attr(0755,root,root) %{_bindir}/gce_compat_metadata_script_runner
%attr(0755,root,root) %{_bindir}/gce_metadata_script_runner
%attr(0755,root,root) %{_bindir}/ggactl_plugin
%attr(0755,root,root) %{_bindir}/google_guest_agent_manager
#%attr(0755,root,root) %{_bindir}/google_guest_compat_manager
# Initially we do not want the core plugin
#%attr(0755,root,root) %{core_plugin_dir}/core_plugin
#%attr(0755,root,root) %{core_plugin_dir}/manifest.binpb
# Telemetry
%attr(0755,root,root) %{telemetry_ext_dir}/guest_telemetry
%attr(0755,root,root) %{telemetry_ext_dir}/manifest.binpb
%attr(0755,root,root) %{_sbindir}/rcgoogle-guest-agent-manager
%config %{_sysconfdir}/default/instance_configs.cfg
%{_unitdir}/google-guest-agent-manager.service

%changelog
