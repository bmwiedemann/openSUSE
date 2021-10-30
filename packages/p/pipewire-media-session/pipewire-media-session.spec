#
# spec file for package pipewire-media-session
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


Name:           pipewire-media-session
Version:        0.4.0
Release:        0
Summary:        Example session manager for Pipewire
License:        MIT
URL:            https://gitlab.freedesktop.org/pipewire/media-session
Source:         media-session-%{version}.tar.xz

BuildRequires:  c_compiler
BuildRequires:  doxygen
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig(alsa) >= 1.1.7
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.39
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
Requires:       pipewire >= 0.3.39
Provides:       pipewire-session-manager

%description
PipeWire Media Session is an example session manager for PipeWire.

%lang_package

%prep
%autosetup -p1 -n media-session-%{version}

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

touch %{buildroot}%{_datadir}/pipewire/media-session.d/with-alsa

%find_lang media-session %{name}.lang

%pre
%systemd_user_pre pipewire-media-session.service

%post
%systemd_user_post pipewire-media-session.service

# If the pipewire-media-session user service is not enabled and the
# wireplumber user service is not enabled either (since it can replace pipewire-media-session)
# and the workaround for boo#1186561 has never been executed,
# we need to execute it now
if [ ! -L %{_sysconfdir}/systemd/user/pipewire.service.wants/pipewire-media-session.service \
    -a ! -L %{_sysconfdir}/systemd/user/pipewire.service.wants/wireplumber.service \
    -a ! -f %{_localstatedir}/lib/pipewire/pipewire-media-session_post_workaround \
    -a -x /usr/bin/systemctl ]; then
    for service in pipewire-media-session.service ; do
        /usr/bin/systemctl --global preset "$service" || :
    done

    mkdir -p %{_localstatedir}/lib/pipewire
    cat << EOF > %{_localstatedir}/lib/pipewire/pipewire-media-session_post_workaround
# The existence of this file means that the pipewire user services were
# enabled at least once. Please don't remove this file as that would
# make the services to be enabled again in the next package update.
#
# Check the following bugs for more information:
# https://bugzilla.opensuse.org/show_bug.cgi?id=1184852
# https://bugzilla.opensuse.org/show_bug.cgi?id=1183012
# https://bugzilla.opensuse.org/show_bug.cgi?id=1186561
EOF
fi

%preun
%systemd_user_preun pipewire-media-session.service

%postun
%systemd_user_postun pipewire-media-session.service


%files
%license COPYING LICENSE
%doc NEWS README.md
%{_bindir}/pipewire-media-session
%{_userunitdir}/pipewire-media-session.service
%dir %{_datadir}/pipewire
%dir %{_datadir}/pipewire/media-session.d/
%{_datadir}/pipewire/media-session.d/alsa-monitor.conf
%{_datadir}/pipewire/media-session.d/bluez-monitor.conf
%{_datadir}/pipewire/media-session.d/media-session.conf
%{_datadir}/pipewire/media-session.d/v4l2-monitor.conf
%{_datadir}/pipewire/media-session.d/with-pulseaudio
%{_datadir}/pipewire/media-session.d/with-jack
%{_datadir}/pipewire/media-session.d/with-alsa

%files lang -f %{name}.lang

%changelog
