#
# spec file for package uwsm
#
# Copyright (c) 2026 SUSE LLC
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


Name:           uwsm
Version:        0.26.2
Release:        0
Summary:        Universal Wayland Session Manager
License:        MIT
Group:          System/Management
URL:            https://github.com/Vladimir-csp/uwsm
Source:         %{name}-%{version}.tar.zst
BuildRequires:  meson >= 1.3
BuildRequires:  scdoc

%if 0%{?suse_version} >= 1600
BuildRequires:  python3-dbus-python
BuildRequires:  python3-pyxdg
Requires:       python3-base >= 3.10
Requires:       python3-dbus-python
Requires:       python3-pyxdg
%else
BuildRequires:  python311-dbus-python
BuildRequires:  python311-pyxdg
Requires:       python311-base
Requires:       python311-dbus-python
Requires:       python311-pyxdg
%endif

Recommends:     inotify-tools
Recommends:     libnotify-tools
Recommends:     newt
Recommends:     util-linux
Enhances:       bemenu
Enhances:       dmenu
Enhances:       fuzzel
Enhances:       rofi
Enhances:       tofi
Enhances:       wmenu
Enhances:       wofi
Provides:       fumon = %{version}
Provides:       uuctl = %{version}
Provides:       %{name}-app = %{version}
Provides:       %{name}-terminal = %{version}
Provides:       %{name}-terminal-scope = %{version}
Provides:       %{name}-terminal-service = %{version}
BuildArch:      noarch

%description
Wraps standalone Wayland compositors into a set of Systemd units on the fly.
This provides robust session management including environment, XDG autostart
support, bi-directional binding with login session, and clean shutdown.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
%meson -Dpython-bin=/usr/bin/python3.11
%endif

%meson \
    -Ddocdir=%{_docdir}/%{name} \
    -Dfumon=enabled \
    -Duuctl=enabled \
    -Duwsm-app=enabled \
    -Dwait-tray=enabled \
    -Dttyautolock=enabled

%meson_build

%install
%meson_install
rm %{buildroot}/%{_userpresetdir}/80-fumon.preset
rm %{buildroot}/%{_userpresetdir}/80-ttyautolock.preset

%check
export PYTHONDONTWRITEBYTECODE=1
PYTHONPATH=%{buildroot}/%{_datadir}/%{name}/modules %{buildroot}/%{_bindir}/%{name} --version

%files
%{_bindir}/%{name}*
%{_bindir}/fumon
%{_bindir}/ttyautolock
%{_bindir}/uuctl
%{_bindir}/wait-tray
%{_datadir}/%{name}
%{_userunitdir}/*
%{_datadir}/applications/uuctl.desktop
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/prepare-env.sh
%{_libexecdir}/%{name}/signal-handler.sh
%license LICENSE
%doc %{_docdir}/%{name}
%{_mandir}/man?/%{name}*
%{_mandir}/man1/fumon.1%{?ext_man}
%{_mandir}/man1/ttyautolock.1%{?ext_man}
%{_mandir}/man1/uuctl.1%{?ext_man}

%changelog
