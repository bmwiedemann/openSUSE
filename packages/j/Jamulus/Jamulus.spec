#
# spec file for package Jamulus
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2014 Pascal Bleser <pascal.bleser@opensuse.org>
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


%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

%define tarball_version 3_10_0

Name:           Jamulus
Version:        3.11.0
Release:        0
Summary:        Low-latency internet connection tool for real-time jam sessions
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://jamulus.io/
Source0:        https://github.com/jamulussoftware/jamulus/archive/r%{tarball_version}/%{name}-%{version}.tar.gz
Source1:        %{name}_icon.png
Source10:       %{name}-public.service
Source11:       %{name}-private.service
Source12:       %{name}-newrec.service
Source13:       %{name}-togglerec.service
Source20:       %{name}.sysconfig
Source21:       %{name}.firewalld
Source90:       README.SUSE
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  firewall-macros
BuildRequires:  firewalld
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  jack-devel >= 1.9.21
BuildRequires:  pkgconfig
BuildRequires:  pwdutils
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt6Concurrent) >= 6.6.3
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(opus)
Requires:       jack >= 1.9.21
Requires(pre):  shadow
Requires(pre):  %fillup_prereq
Requires(pre):  group(nogroup)
Provides:       llcon = %{version}
Obsoletes:      llcon < %{version}
Provides:       jamulus = %{version}
Obsoletes:      jamulus < %{version}
%{?systemd_requires}

%description
The Jamulus software enables musicians to perform real-time jam sessions over
the internet. There is one server running the Jamulus server software which
collects the audio data from each Jamulus client software, mixes the audio data
and sends the mix back to each client.

%prep
%autosetup -p1 -n jamulus-r%{tarball_version}
install %{SOURCE1} .
install -m644 %{SOURCE90} .

%build
%qmake6 CONFIG+=opus_shared_lib CONFIG+=disable_version_check
%make_jobs

%install
install -D -m0755 Jamulus %{buildroot}%{_bindir}/%{name}
for s in 16 22 32 48 64 72 96 128 192; do
   mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
   convert -strip -resize ${s}x${s} %{name}_icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done
install -Dm0644 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png \
                %{buildroot}%{_datadir}/pixmaps/%{name}.png

# sysconfig
install -d -m0755 %{buildroot}%{_fillupdir}
install -D -m0644 %{SOURCE20} %{buildroot}%{_fillupdir}/sysconfig.jamulus

# firewalld
install -D -m0644 %{SOURCE21} %{buildroot}%{_prefix}/lib/firewalld/services/jamulus.xml

# systemd/services
install -D -m0644 %{SOURCE10} %{buildroot}%{_unitdir}/jamulus-public.service
install -d -m0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcjamulus-public

install -D -m0644 %{SOURCE11} %{buildroot}%{_unitdir}/jamulus-private.service
install -d -m0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcjamulus-private

install -D -m0644 %{SOURCE12} %{buildroot}%{_unitdir}/jamulus-newrec.service
install -d -m0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcjamulus-newrec

install -D -m0644 %{SOURCE13} %{buildroot}%{_unitdir}/jamulus-togglerec.service
install -d -m0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcjamulus-togglerec

# desktop file
sed -i -e 's|$$TARGET|Jamulus|g' linux/jamulus.desktop.in
sed -i -e 's|Icon=jamulus|Icon=Jamulus|g' linux/jamulus.desktop.in
install -D -m 0644 linux/jamulus.desktop.in %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name}

%fdupes %{buildroot}%{_datadir}

%pre
%service_add_pre jamulus-public.service jamulus-private.service jamulus-newrec.service jamulus-togglerec.service
getent passwd jamulus >/dev/null || \
	useradd -r -g nogroup -d /var/lib/empty -s /bin/false \
	-c "Jamulus Server" jamulus

%post
%service_add_post jamulus-public.service jamulus-private.service jamulus-newrec.service jamulus-togglerec.service
%{fillup_only -n jamulus}
%firewalld_reload

%preun
%service_del_preun jamulus-public.service jamulus-private.service jamulus-newrec.service jamulus-togglerec.service

%postun
%service_del_postun jamulus-public.service jamulus-private.service jamulus-newrec.service jamulus-togglerec.service

%files
%doc README.md ChangeLog README.SUSE
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
# sysconfig
%{_fillupdir}/sysconfig.jamulus
# firewalld
%{_prefix}/lib/firewalld/services/jamulus.xml
# systemd/services
%{_unitdir}/jamulus-public.service
%{_sbindir}/rcjamulus-public
%{_unitdir}/jamulus-private.service
%{_sbindir}/rcjamulus-private
%{_unitdir}/jamulus-newrec.service
%{_sbindir}/rcjamulus-newrec
%{_unitdir}/jamulus-togglerec.service
%{_sbindir}/rcjamulus-togglerec

%changelog
