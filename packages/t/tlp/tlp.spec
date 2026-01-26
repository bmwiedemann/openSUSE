#
# spec file for package tlp
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define _name TLP
%define systemd_sleepdir %{_systemd_util_dir}/system-sleep
%if 0%{?suse_version} > 01500
%define _udevdir %(pkg-config --variable udev_dir udev || echo %{_prefix}/lib/udev)
%else
%{!?_udevdir: %define _udevdir %{_prefix}/lib/udev}
%endif
%{!?_udevrulesdir: %define _udevrulesdir %{_udevdir}/rules.d}
Name:           tlp
Version:        1.9.1
Release:        0
Summary:        Tools to save battery power on laptops
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Hardware/Mobile
URL:            https://linrunner.de/tlp
Source:         TLP-%{version}.tar.zst
Source10:       tlp-rpmlintrc
BuildRequires:  gzip
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(udev)
Requires:       hdparm
Requires:       iw
Requires:       pciutils
Requires:       rfkill
Requires:       usbutils
Requires:       util-linux >= 2.17
Requires(pre):  systemd
Recommends:     %{name}-pd = %{version}
Recommends:     %{name}-rdw = %{version}
Recommends:     ethtool
Recommends:     lsb-release
Recommends:     smartmontools
Conflicts:      laptop-mode-tools
Conflicts:      power-profiles-daemon
Conflicts:      tuned
BuildArch:      noarch
%{?systemd_ordering}

%description
TLP is a feature-rich command-line utility, saving laptop battery power
without the need to delve deeper into technical details.

TLP’s default settings are already optimized for battery life and implement
Powertop’s recommendations out of the box. Moreover TLP is highly
customizable to fulfill specific user requirements.

Settings are organized into two profiles, allowing to adjust between
savings and performance independently for battery (BAT) and AC operation.
In addition TLP can enable or disable Bluetooth, NFC, Wi-Fi and WWAN radio
devices on boot.

For ThinkPads and selected other laptops it provides a unified way
to configure charge thresholds and re-calibrate the battery.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}.

%package rdw
Summary:        TLP Radio Device Wizard
Group:          Hardware/Mobile
Requires:       %{name} = %{version}
Requires:       NetworkManager >= 1.20
Requires(pre):  systemd
BuildArch:      noarch

%description rdw
Radio device wizard is an add-on to TLP. It provides event based
switching of Bluetooth, NFC, Wi-Fi and WWAN radio devices on:
 - network connect/disconnect
 - dock/undock

%package rdw-bash-completion
Summary:        Bash Completion for %{name}-rdw
Group:          System/Shells
Requires:       %{name}-rdw = %{version}
Requires:       bash-completion
Supplements:    (%{name}-rdw and bash-completion)
BuildArch:      noarch

%description rdw-bash-completion
The official bash completion script for %{name}-rdw.

%package rdw-fish-completion
Summary:        Fish Completion for %{name}-rdw
Group:          System/Shells
Requires:       %{name}-rdw = %{version}
Supplements:    (%{name}-rdw and fish)
BuildArch:      noarch

%description rdw-fish-completion
The official fish completion script for %{name}-rdw.

%package rdw-zsh-completion
Summary:        ZSH Completion for %{name}-rdw
Group:          System/Shells
Requires:       %{name}-rdw = %{version}
Supplements:    (%{name}-rdw and zsh)
BuildArch:      noarch

%description rdw-zsh-completion
The official zsh completion script for %{name}-rdw.

%package pd
Summary:        TLP Power Profiles Daemon
Group:          Hardware/Mobile
Requires:       %{name} = %{version}
Requires(pre):  systemd
BuildArch:      noarch

%description pd
Power Profiles Daemon replacement for TLP.

%package -n tlpctl-bash-completion
Summary:        Bash Completion for tlpctl
Group:          System/Shells
Requires:       %{name}-pd = %{version}
Requires:       bash-completion
Supplements:    (%{name}-pd and bash-completion)
BuildArch:      noarch

%description -n tlpctl-bash-completion
The official bash completion script for tlpctl.

%package -n tlpctl-fish-completion
Summary:        Fish Completion for tlpctl
Group:          System/Shells
Requires:       %{name}-pd = %{version}
Supplements:    (%{name}-pd and fish)
BuildArch:      noarch

%description -n tlpctl-fish-completion
The official fish completion script for tlpctl.

%package -n tlpctl-zsh-completion
Summary:        ZSH Completion for tlpctl
Group:          System/Shells
Requires:       %{name}-pd = %{version}
Supplements:    (%{name}-pd and zsh)
BuildArch:      noarch

%description -n tlpctl-zsh-completion
The official zsh completion script for tlpctl.

%prep
%setup -q -n %{_name}-%{version}

%build
%make_build \
  TLP_ULIB=%{_udevdir} \
  TLP_SYSD=%{_unitdir}

%install
%make_install \
  TLP_WITH_SYSTEMD=1           \
  TLP_WITH_ELOGIND=0           \
  TLP_NO_INIT=1                \
  TLP_ULIB=%{_udevdir} \
  TLP_SYSD=%{_unitdir} \
  TLP_SDSL=%{systemd_sleepdir}

make install-man      DESTDIR=%{buildroot}
make install-man-rdw  DESTDIR=%{buildroot}

ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rctlp


%pre
%service_add_pre tlp.service

%post
%service_add_post tlp.service
%{_bindir}/systemctl mask systemd-rfkill.service
%{_bindir}/systemctl mask systemd-rfkill.socket
%{_bindir}/systemctl mask power-profiles-daemon.service

%postun
%service_del_postun tlp.service
if [ $1 -eq 0 ] ; then
    %{_bindir}/systemctl unmask systemd-rfkill.service
    %{_bindir}/systemctl unmask systemd-rfkill.socket
    %{_bindir}/systemctl unmask power-profiles-daemon.service
fi

%preun
%service_del_preun tlp.service

%post rdw
%{_bindir}/systemctl enable NetworkManager-dispatcher.service >/dev/null 2>&1 || :

%pre pd
%service_add_pre tlp-pd.service

%post pd
%service_add_post tlp-pd.service

%postun pd
%service_del_postun tlp-pd.service

%preun pd
%service_del_preun tlp-pd.service

%files
%license COPYING LICENSE
%doc AUTHORS changelog README.rst
%dir %{_sysconfdir}/%{name}.d
%dir %{systemd_sleepdir}
%dir %{_datadir}/metainfo/
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}.d/00-template.conf
%{_sysconfdir}/%{name}.d/README
%{systemd_sleepdir}/tlp
%{_bindir}/bluetooth
%{_bindir}/run-on-{ac,bat}
%{_bindir}/%{name}-stat
%{_bindir}/nfc
%{_bindir}/wifi
%{_bindir}/wwan
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_datadir}/%{name}/
%{_datadir}/metainfo/de.linrunner.tlp.metainfo.xml
%{_udevdir}/%{name}-usb-udev
%{_udevrulesdir}/85-%{name}.rules
%{_mandir}/man?/*.?%{?ext_man}
%exclude %{_mandir}/man8/%{name}-rdw.8%{?ext_man}
%exclude %{_mandir}/man1/tlpctl.1%{?ext_man}
%exclude %{_mandir}/man8/%{name}-pd.8%{?ext_man}
%exclude %{_mandir}/man8/%{name}-pd.service.8%{?ext_man}

%files bash-completion
#%{_datadir}/bash-completion/completions/tlp.bash_completion
%{_datadir}/bash-completion/completions/*
%exclude %{_datadir}/bash-completion/completions/tlp-rdw
%exclude %{_datadir}/bash-completion/completions/tlpctl

%files zsh-completion
%{_datadir}/zsh/site-functions/*
%exclude %{_datadir}/zsh/site-functions/_tlp-rdw
%exclude %{_datadir}/zsh/site-functions/_tlpctl

%files fish-completion
%{_datadir}/fish/vendor_completions.d/*
%exclude %{_datadir}/fish/vendor_completions.d/tlp-rdw.fish
%exclude %{_datadir}/fish/vendor_completions.d/tlpctl.fish

%files rdw
%dir %{_prefix}/lib/NetworkManager
%dir %{_prefix}/lib/NetworkManager/dispatcher.d
%attr(0755,root,root) %{_prefix}/lib/NetworkManager/dispatcher.d/99tlp-rdw-nm
%{_bindir}/%{name}-rdw
%{_udevrulesdir}/85-%{name}-rdw.rules
%{_udevdir}/%{name}-rdw-udev
%{_mandir}/man8/%{name}-rdw.8%{?ext_man}

%files rdw-bash-completion
%{_datadir}/bash-completion/completions/%{name}-rdw

%files rdw-zsh-completion
%{_datadir}/zsh/site-functions/_%{name}-rdw

%files rdw-fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}-rdw.fish

%files pd
%{_bindir}/tlpctl
%{_sbindir}/tlp-pd
%{_unitdir}/%{name}-pd.service
%{_mandir}/man1/tlpctl.1%{?ext_man}
%{_mandir}/man8/%{name}-pd.8%{?ext_man}
%{_mandir}/man8/%{name}-pd.service.8%{?ext_man}
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/dbus-1/system-services/org.freedesktop.UPower.PowerProfiles.service
%{_datadir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.UPower.PowerProfiles.conf
%{_datadir}/polkit-1/actions/tlp-pd.policy

%files -n tlpctl-bash-completion
%{_datadir}/bash-completion/completions/tlpctl

%files -n tlpctl-zsh-completion
%{_datadir}/zsh/site-functions/_tlpctl

%files -n tlpctl-fish-completion
%{_datadir}/fish/vendor_completions.d/tlpctl.fish

%changelog
