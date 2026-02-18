#
# spec file for package netbird
#
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


%ifnarch %{ix86}
%bcond_without netbird_ui
%else
%bcond_with netbird_ui
%endif

%if 0%{?sle_version} <= 150600 && !0%{?is_opensuse}
%bcond_without appindicator_sle
%else
%bcond_with appindicator_sle
%endif

# safeguard to not enable it by default until we have finished  it for all subpackages
%bcond_with stub_config

Name:           netbird
Version:        0.65.2
Release:        0
Summary:        Mesh VPN based on WireGuard
License:        AGPL-3.0-only AND BSD-3-Clause
URL:            https://github.com/netbirdio/netbird
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        %{name}.service
Source3:        %{name}-management.service
Source4:        %{name}-signal.service
Patch0:         service-install-cli-change.patch
BuildRequires:  fdupes
BuildRequires:  fish
BuildRequires:  git-core
BuildRequires:  zsh
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.25
# Required for testing
BuildRequires:  pkgconfig(libpcap)
# For GUI applet
%if %{with netbird_ui}
BuildRequires:  pkgconfig(xxf86vm)
%if %{with appindicator_sle}
BuildRequires:  pkgconfig(appindicator3-0.1)
%else
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
%endif
BuildRequires:  hicolor-icon-theme
%endif

%description
NetBird combines a configuration-free peer-to-peer private network and a
centralized access control system in a single platform, making it easy to
create secure private networks for your organization or home.

%if %{with netbird_ui}
%package applet
Summary:        Optional UI panel indicator for %{name}
Requires:       %{name}

%description applet
Optional UI panel indicator for %{name}.
%endif

%package management
Summary:        Backend management portion for %{name} server

%description management
Optional management server component for %{name}. Please note that this does not
comprise a full netbird backend server, and is merely built for convenience.
Management/signal/relay are not required for the netbird client application.

%package signal
Summary:        Backend signal portion for %{name} server

%description signal
Optional signal server component for %{name}. Please note that this does not
comprise a full netbird backend server, and is merely built for convenience.
Management/signal/relay are not required for the netbird client application.

%package relay
Summary:        Backend signal portion for %{name} server

%description relay
Optional new relay component for %{name}. Please note that this does not
comprise a full netbird backend server, and is merely built for convenience.
Management/signal/relay are not required for the netbird client application.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package management-bash-completion
Summary:        Bash Completion for %{name}
Requires:       bash-completion
Requires:       netbird-management
Supplements:    (%{name}-management and bash-completion)
BuildArch:      noarch

%description management-bash-completion
Bash command line completion support for %{name}-management.

%package management-fish-completion
Summary:        Fish Completion for %{name}-management
Requires:       fish
Requires:       netbird-management
Supplements:    (%{name}-management and fish)
BuildArch:      noarch

%description management-fish-completion
Fish command line completion support for %{name}-management.

%package management-zsh-completion
Summary:        Zsh Completion for %{name}-management
Requires:       netbird-management
Requires:       zsh
Supplements:    (%{name}-management and zsh)
BuildArch:      noarch

%description management-zsh-completion
Zsh command line completion support for %{name}-management.

%package signal-bash-completion
Summary:        Bash Completion for %{name}-management
Requires:       bash-completion
Requires:       netbird-signal
Supplements:    (%{name}-signal and bash-completion)
BuildArch:      noarch

%description signal-bash-completion
Bash command line completion support for %{name}-signal.

%package signal-fish-completion
Summary:        Fish Completion for %{name}-signal
Requires:       fish
Requires:       netbird-signal
Supplements:    (%{name}-signal and fish)
BuildArch:      noarch

%description signal-fish-completion
Fish command line completion support for %{name}-signal.

%package signal-zsh-completion
Summary:        Zsh Completion for %{name}-signal
Requires:       netbird-signal
Requires:       zsh
Supplements:    (%{name}-signal and zsh)
BuildArch:      noarch

%description signal-zsh-completion
Zsh command line completion support for %{name}-signal.

%prep
%autosetup -p1 -a1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

export LDFLAGS="-X github.com/netbirdio/netbird/version.version=v%{version} \
    -X main.commit=${COMMIT_HASH:0:8} \
    -X main.date=${BUILD_DATE} -X main.builtBy=openSUSE"

go build -o %{name} -buildmode=pie -mod=vendor -ldflags "$LDFLAGS" ./client
go build -o %{name}-mgmt -buildmode=pie -mod=vendor -ldflags "$LDFLAGS" ./management
go build -o %{name}-signal -buildmode=pie -mod=vendor -ldflags "$LDFLAGS" ./signal
go build -o %{name}-relay -buildmode=pie -mod=vendor -ldflags "$LDFLAGS" ./relay

%if %{with netbird_ui}
go build -o %{name}-ui -buildmode=pie -mod=vendor -ldflags "$LDFLAGS" ./client/ui
%endif

%install
install -Dm755 -t %{buildroot}%{_bindir} %{name}{,-mgmt,-signal,-relay}

# Install the applet and the icons, so the desktop file doesn't have an empty icon.
%if %{with netbird_ui}
install -Dm755 %{name}-ui %{buildroot}%{_bindir}/%{name}-ui
install -Dm644 client/ui/build/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
# All icons are 256x256. These seem to get pulled into the applet binary regardless,
# but still worth throwing in separately.
install -dm755 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -Dm644 client/ui/assets/%{name}*.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
# The system-tray-connected icon is the same as netbird.ico, which won't be picked up by xdg with .ico metadata
install -Dm644 client/ui/assets/%{name}-systemtray-connected.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/netbird.png
%endif

# Generate completions
for bin in %{name} %{name}-signal %{name}-mgmt
do
  for sh in bash zsh fish
  do
    ./${bin} completion $sh > ${bin}.${sh}
  done
  install -Dm644 ${bin}.bash %{buildroot}%{_datadir}/bash-completion/completions/${bin}
  install -Dm644 ${bin}.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_${bin}
  install -Dm644 ${bin}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/${bin}.fish
done

# Install service files
install -Dm644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -Dm644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}-management.service
install -Dm644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}-signal.service
# No service files for relay yet, will likely have in the future. For now it's very new
# and unclear outside of running in docker-compose stack how a generic service file
# would look.

# Prepare config directory which netbird will populate once configured by user
install -d %{buildroot}%{_sysconfdir}/%{name}

%if %{with stub_config}
echo <<EOF > %{buildroot}/etc/netbird/config.json
##
## To add this machine to your netbird instance run:
##
## netbird up --management-url https://yournetbird.example.com --setup-key setupkey
##
## documentation can be found here: https://docs.netbird.io/how-to/cli#up
##
EOF

chmod go= %{buildroot}%{_sysconfdir}/%{name}/*
%endif

%if %{with netbird_ui}
%fdupes %{buildroot}%{_datadir}/icons/
%endif

%check
# All of these tests require networking and fail.
failing_tests=(
  TestUpload
  TestIptablesManager{,IPSet}
  TestNftablesManager
  Test{Ip,NF}tablesCreatePerformance\*
  TestUpdate{OldManagementURL,DNSServer}\*
  TestEngine_{SSH,Sync,MultiplePeers,UpdateNetworkMap}\*
  TestDNSFakeResolverHandleUpdates
  TestDNSPermanent_{update{HostDNS_emptyUpstream,Upstream},matchOnly}
  TestManagerUpdateRoutes\*
  TestWGIface_UpdateAddr
  Test_{Create,Configure}Interface
  Test_Close
  Test_{Update,Remove}Peer
  Test_ConnectPeers
  TestPostgresql_{NewStore,{Save,Delete}Account,SavePeerStatus}
  TestPostgresql_TestGetAccountByPrivateDomain
  TestPostgresql_Get{TokenIDByHashedToken,UserByTokenID}
  TestShould{ReadSTUNOnReadFrom,NotReadNonSTUNPackets}
  TestWriteTo
  TestSharedSocket_Close
  Test{AddVPNRoute,AddRouteToNonVPNIntf,Routing}\*
  TestUpstreamResolver_ServeDNS\*
  TestGetNextHop
  Test_NetAddresses
  Test_ParseNATExternalIPMappings\*
  TestRecreation\*
  TestExistsInRouteTable
  TestProxyCloseByRemoteConn
  TestNetworkMonitor_Event
  TestNetworkMonitor_MultiEvent
  TestServiceLifecycle\*
  TestUpDaemon
  TestConnectWithRetryRuns
  TestResolver_PartialUpdateReplacesOnlyUpdatedTypes
  TestResolver_EmptyUpdateDoesNotRemoveDomains
  TestResolver_PartialUpdateAddsNewTypePreservesExisting
  TestServer_Up
  TestProxyRedirect
  TestSSHClient_CommandExecution
  TestSSHClient_ContextCancellation
  TestSSHProxy_Connect
  TestPrivilegeDropper_CreateExecutorCommand
  TestPrivilegeDropper_CreateExecutorCommandInteractive
  TestJWTEnforcement/allows_when_disabled
  TestJWTAuthentication
  TestJWTDetection
  TestICEBind_HandlesConcurrentMixedTraffic
  TestRedirectAs_\*
)
# Assemble skip string by replacing spaces with a pipe.
disable=$(echo ${failing_tests[*]} | sed 's/ /|/g')
# Literally no reason to even try to test management/server components
# as the built binaries are not part of a full system and are not used
# for the client. Also rely on networking caps that get killed by OBS.
go test -skip "${disable}" ./client/...

%pre
%service_add_pre %{name}.service

%pre management
%service_add_pre %{name}-management.service

%pre signal
%service_add_pre %{name}-signal.service

%preun
%service_del_preun %{name}.service

%preun management
%service_del_preun %{name}-management.service

%preun signal
%service_del_preun %{name}-signal.service

%post
%service_add_post %{name}.service

%post management
%service_add_post %{name}-management.service

%post signal
%service_add_post %{name}-signal.service

%postun
%service_del_postun %{name}.service

%postun management
%service_del_postun %{name}-management.service

%postun signal
%service_del_postun %{name}-signal.service

%files
%license LICENSE
%doc README.md SECURITY.md AUTHORS CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTOR_LICENSE_AGREEMENT.md
%if %{with stub_config}
%dir /etc/netbird/
%config(noreplace) /etc/netbird/config.json
%endif
%{_bindir}/%{name}
%{_sysconfdir}/%{name}
%{_unitdir}/%{name}.service

%if %{with netbird_ui}
%files applet
%{_bindir}/%{name}-ui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}*.png
%endif

%files management
%{_bindir}/%{name}-mgmt
%{_unitdir}/%{name}-management.service

%files signal
%{_bindir}/%{name}-signal
%{_unitdir}/%{name}-signal.service

%files relay
%{_bindir}/%{name}-relay

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%files management-bash-completion
%{_datadir}/bash-completion/completions/%{name}-mgmt

%files management-fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}-mgmt.fish

%files management-zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}-mgmt

%files signal-bash-completion
%{_datadir}/bash-completion/completions/%{name}-signal

%files signal-fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}-signal.fish

%files signal-zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}-signal

%changelog
