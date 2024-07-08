#
# spec file for package google-guest-agent
#
# Copyright (c) 2024 SUSE LLC
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


%global provider        github
%global provider_tld    com
%global project         GoogleCloudPlatform
%global repo            guest-agent
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           google-guest-agent
Version:        20240701.00
Release:        0
Summary:        Google Cloud Guest Agent
License:        Apache-2.0
Group:          System/Daemons
URL:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        rpmlintrc
Patch0:         disable_google_dhclient_script.patch
Patch1:         dont_overwrite_ifcfg.patch
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.21
Requires:       google-guest-configs
Requires:       google-guest-oslogin >= 20231003
Provides:       google-compute-engine-init = %{version}
Obsoletes:      google-compute-engine-init < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%{go_nostrip}
%{go_provides}

%description
Google Cloud Guest Agent

%prep
%setup -n %{repo}-%{version} -a1
%patch -P 0 -P 1 -p1

%build
%goprep %{import_path}
for bin in google_guest_agent google_metadata_script_runner; do
    pushd "$bin"
    CGO_ENABLED=0 go build -ldflags="-s -w -X main.version=%{version}" -mod=vendor
    popd
done

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 google_guest_agent/google_guest_agent %{buildroot}%{_bindir}/google_guest_agent
install -p -m 0755 google_metadata_script_runner/google_metadata_script_runner %{buildroot}%{_bindir}/google_metadata_script_runner
install -d %{buildroot}/usr/share/google-guest-agent
install -p -m 0644 instance_configs.cfg %{buildroot}/usr/share/google-guest-agent/instance_configs.cfg
install -d %{buildroot}%{_unitdir}
install -p -m 0644 %{name}.service %{buildroot}%{_unitdir}
install -p -m 0644 google-startup-scripts.service %{buildroot}%{_unitdir}
install -p -m 0644 google-shutdown-scripts.service %{buildroot}%{_unitdir}
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
    %service_add_pre google-guest-agent.service google-shutdown-scripts.service google-startup-scripts.service

%preun
    %service_del_preun google-guest-agent.service google-shutdown-scripts.service google-startup-scripts.service

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

    %service_add_post google-guest-agent.service google-shutdown-scripts.service google-startup-scripts.service

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
    if ! [ -e /.buildenv ] && [ -f /tmp/tmp\.[A-Z,a-z,0-9]*\.google-startup-scripts ] ; then
        rm -f /tmp/tmp\.[A-Z,a-z,0-9]*\.google-startup-scripts
        systemctl enable google-startup-scripts.service
    fi
    if ! [ -e /.buildenv ] && [ -f /tmp/tmp\.[A-Z,a-z,0-9]*\.google-shutdown-scripts ] ; then
	rm -f /tmp/tmp\.[A-Z,a-z,0-9]*\.google-shutdown-scripts
        systemctl enable google-shutdown-scripts.service
    fi

%postun
    %service_del_postun google-guest-agent.service google-shutdown-scripts.service google-startup-scripts.service

%files
%defattr(0644,root,root,0755)
%license LICENSE
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/google-guest-agent
%{_sbindir}/*
%{_unitdir}/*

%changelog
