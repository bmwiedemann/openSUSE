#
# spec file for package autorandr
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

Name:           autorandr
Version:        1.15.0.1709469470
Release:        0
Summary:        Auto-load and detect display hardware using xrandr
License:        GPL-3.0-or-later
URL:            https://github.com/phillipberndt/autorandr
Source0:        %{name}-%{version}.tar.bz2
Source10:       autorandr-rpmlintrc
BuildRequires:  python-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  pkg-config
Requires:       libinput-tools
BuildArch:      noarch

%description
Auto-detect the connect display hardware and load the appropriate X11 setup using xrandr

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%prep
%autosetup

%build

%install

%make_install \
  TARGETS="autorandr systemd udev autostart_config bash_completion" \
  DESTDIR="%{buildroot}" \
  SYSTEMD_UNIT_DIR="%{_unitdir}" \
  UDEV_RULES_DIR="%{_udevrulesdir}" \
  BASH_COMPLETIONS_DIR="%{_datadir}/bash-completion"
  
%python3_fix_shebang

%pre
%service_add_pre %{name}.service %{name}-lid-listener.service

%post
%service_add_post %{name}.service %{name}-lid-listener.service

%preun
%service_del_preun %{name}.service %{name}-lid-listener.service

%postun
%service_del_postun %{name}.service %{name}-lid-listener.service

%files
%license gpl-3.0.txt
%doc README.md
%{_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/autorandr*.desktop
%{_udevrulesdir}/40-monitor-hotplug.rules
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-lid-listener.service

%files bash-completion
%{_datadir}/bash-completion/*

%changelog
