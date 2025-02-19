#
# spec file for package gkrellm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           gkrellm
Version:        2.3.11
Release:        0
Summary:        Manages Multiple Stacked Monitors
License:        GPL-3.0-or-later
Group:          System/Monitoring
URL:            http://gkrellm.srcbox.net/
Source:         http://gkrellm.srcbox.net/releases/%{name}-%{version}.tar.bz2
Source1:        %name.desktop
Source2:        gkrellm-16.png
Source3:        gkrellm-24.png
Source4:        gkrellm-32.png
Source5:        gkrellm-48.png
%if 0%{?suse_version} > 1220
Source6:        gkrellmd.service
%endif
# PATCH-FIX-OPENSUSE gkrellm-lib64-plugins-dir.patch pgajdos@suse.cz -- look also into /usr/lib64/gkrellm2/plugins
Patch1:         %{name}-lib64-plugins-dir.patch
# PATCH-FIX-OPENSUSE gkrellm-install-and-reconnect-gkrellmd.conf.patch hpj@urpla.net -- install /etc/gkrellmd.conf and make reconnect default
Patch2:         %{name}-install-and-reconnect-gkrellmd.conf.patch

BuildRequires:  gtk2-devel
BuildRequires:  libsensors4-devel
%if 0%{?suse_version} > 1220
BuildRequires:  systemd-rpm-macros
%endif
BuildRequires:  openssl-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-libSM-devel
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# no libsensors
ExcludeArch:    s390 s390x

%description
With a single process, GKrellM manages multiple stacked monitors and
supports applying themes to match the monitors appearance to your
window manager, Gtk, or any other theme.

* SMP CPU, Disk, Proc, and active net interface monitors with LEDs.

* Internet monitor that displays current and charts historical port
   hits.

* Memory and swap space usage meters and a system uptime monitor.

* File system meters show capacity and free space and can mount and
   umount.

* A mailbox monitor that can launch a mail reader and fetch remote
   mail.

* Clock, calendar, and hostname display.

* APM laptop battery monitor.

* CPU and motherboard temperature display if lm_sensors modules are
   installed.

* Multiple monitors managed by a single process to reduce system
   load.

* PPP on and off button that can execute your PPP scripts.

* Charts are autoscaling with configurable grid line resolution.

* Separate colors for "in" and "out" data.  The in color is used for
   CPU user time, disk read, forks, and net receive data.  The out
   color is used for CPU sys time, disk write, load, and net
   transmit data.

* A different theme can be created with the GIMP.

%package -n gkrellmd
Summary:        Multiple Stacked Monitors daemon
Group:          System/Monitoring

%description -n gkrellmd
The GNU Grell Monitors daemon service, independent from any GUI library.

%package devel
Summary:        Files needed for gkrellm2 development
Group:          Development/Sources
Requires:       gkrellm = %{version}

%description devel
Files needed to build plugins for gkrellm2

%lang_package

%prep
%autosetup -p1

%build
cd src
# run configure to build against libsensors; otherwise it leads to
#e. g. bnc#803967 bnc#803081
./configure
cd ..
make CFLAGS="%{optflags}" X11_LIBS="-L/usr/X11R6/%{_lib} -lX11 -lSM -lICE" GTOP_LIBS="-lgmodule-2.0" PREFIX=%{_prefix}

%install
make install STRIP= \
     X11_LIBS="-L/usr/X11R6/%{_lib} -lX11 -lSM -lICE" \
     INSTALLROOT=%{buildroot}%{_prefix} \
     CFGDIR=%{buildroot}%{_sysconfdir} \
     PKGCONFIGDIR=%{buildroot}%{_libdir}/pkgconfig

for i in {16,24,32,48}; do
   mkdir -p %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps
done
cp %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gkrellm.png
cp %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/gkrellm.png
cp %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gkrellm.png
cp %{SOURCE5} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gkrellm.png
# following two directories are searched for plugins and we want to own them (bnc#841818)
mkdir -p %{buildroot}/usr/lib/gkrellm2/plugins
%if "x%{_lib}" == "xlib64"
mkdir -p %{buildroot}/usr/lib64/gkrellm2/plugins
%endif
%if 0%{?suse_version} > 1220
install -D -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/gkrellmd.service
mkdir -p %{buildroot}%{_sbindir}
ln -s /sbin/service %{buildroot}%{_sbindir}/rcgkrellmd
%endif
%suse_update_desktop_file -i %name
%find_lang %{name} %{?no_lang_C}

%if 0%{?suse_version} > 1220
%pre -n gkrellmd
%service_add_pre gkrellmd.service
%endif

%post -n gkrellmd
%if 0%{?suse_version} > 1220
%service_add_post gkrellmd.service
%endif
%if 0%{?suse_version} > 1130
%desktop_database_post
%icon_theme_cache_post
%endif

%if %{?suse_version} > 1220
%preun -n gkrellmd
%service_del_preun gkrellmd.service
%stop_on_removal gkrellmd
%endif

%postun -n gkrellmd
%if 0%{?suse_version} > 1220
%service_del_postun gkrellmd.service
%restart_on_update gkrellmd
%endif
%if 0%{?suse_version} > 1130
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%doc COPYRIGHT Changelog README Themes.html
%{_bindir}/gkrellm
%{_datadir}/icons/hicolor/*/apps/gkrellm.png
%{_datadir}/applications/gkrellm.desktop
%doc %{_mandir}/man1/*
%dir /usr/lib/gkrellm2
%dir /usr/lib/gkrellm2/plugins
%if "x%{_lib}" == "xlib64"
%dir /usr/lib64/gkrellm2
%dir /usr/lib64/gkrellm2/plugins
%endif

%files -n gkrellmd
%defattr(-,root,root)
%doc COPYRIGHT Changelog README Themes.html
%config(noreplace) %{_sysconfdir}/gkrellmd.conf
%{_bindir}/gkrellmd
%if 0%{?suse_version} > 1220
%{_sbindir}/rcgkrellmd
%{_unitdir}/gkrellmd.service
%endif

%files devel
%defattr(-,root,root)
%{_includedir}/gkrellm2/
%{_libdir}/pkgconfig/gkrellm.pc

%files lang -f %{name}.lang

%changelog
