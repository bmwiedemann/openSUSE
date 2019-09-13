#
# spec file for package hp-drive-guard
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define new_polkit	(%suse_version >= 1140)
%define use_upower	(%suse_version > 1120)
%define use_gtk3	(%suse_version > 1140)
%define with_systemd	(%suse_version > 1140)

%if %{new_polkit}
%define polkitdir	%{_datadir}/polkit-1/actions
%else
%define polkitdir	%{_datadir}/PolicyKit/policy
%endif

Name:           hp-drive-guard
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  intltool
%if %{use_gtk3}
BuildRequires:  gtk3-devel
%else
BuildRequires:  gtk2-devel
%endif
BuildRequires:  dbus-1-glib-devel
BuildRequires:  libnotify-devel
BuildRequires:  libxslt
%if %{new_polkit}
BuildRequires:  polkit-devel
%else
BuildRequires:  PolicyKit-gnome-devel
%endif
%if %{use_upower}
BuildRequires:  libupower-glib-devel
%else
BuildRequires:  hal-devel
%endif
# BuildRequires:  scrollkeeper
BuildRequires:  update-desktop-files
%if %{with_systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%else
PreReq:         %insserv_prereq
%endif
Version:        0.3.12
Release:        0
Summary:        HP DriveGuard for SUSE
License:        GPL-2.0+
Group:          Hardware/Mobile
Source:         hp-drive-guard-%{version}.tar.bz2
Source1:        hp-drive-guard.service
Patch1:         0001-Fix-misc-compile-warnings.patch
Patch2:         0002-Fix-build-with-the-new-libnotify.patch
Patch3:         use-new-polkit.diff
Patch4:         use-gtk3.diff
Url:            http://www.gnome.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
HP DriveGuard for SUSE. Can protect hard disks on HP laptops by
spinning them down when shaking or free-fall is detected.



Authors:
--------
    Hans Petter Jansson <hpj@suse.com>

%lang_package
%prep
%setup -q
%patch1 -p1
%patch2 -p1
%if %{new_polkit}
%patch3 -p1
%endif
%if %{use_gtk3}
%patch4 -p1
%endif

%if %use_upower
%define pm_method	upower
%else
%define pm_method	hal
%endif

%if %suse_version >= 1120
%define user_setup	--enable-user-setup
%else
# HP requested to prohibit changing parameters in setup dialog for SLED
%define user_setup	--disable-user-setup
%endif

%build
autoreconf -f -i
%configure --with-pm=%{pm_method} %user_setup \
	--disable-schemas-install \
	--disable-scrollkeeper
%__make %{?jobs:-j%jobs}

%install
%makeinstall
%if %with_systemd
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -c -m 0644 %{S:1} $RPM_BUILD_ROOT%{_unitdir}/hp-drive-guard.service
# do not ship the init.d script on a systemd setup
rm %{buildroot}%{_sysconfdir}/init.d/hp-drive-guard
%endif
%find_lang %{name}
%fdupes $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%if %{with_systemd}
%service_add_pre hp-drive-guard.service
%endif

%post
%if %{with_systemd}
%service_add_post hp-drive-guard.service
%else
%{fillup_and_insserv -n hp-drive-guard}
%endif

%preun
%if %{with_systemd}
%service_del_preun hp-drive-guard.service
%else
%{stop_on_removal hp-drive-guard}
%endif

%postun
%if %{with_systemd}
%service_del_postun hp-drive-guard.service
%else
%{restart_on_update hp-drive-guard}
%insserv_cleanup
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%config(noreplace) /etc/*.conf
%{_bindir}/*
%{_sbindir}/*
%{_libexecdir}/hp-drive-guard
%{_sysconfdir}/xdg/autostart/hp-drive-guard-client.desktop
%{_sysconfdir}/dbus-1/system.d/hp-drive-guard-dbus.conf
%{polkitdir}/*
%if %{with_systemd}
%{_unitdir}/hp-drive-guard.service
%else
%{_sysconfdir}/init.d/hp-drive-guard
%endif

%changelog
