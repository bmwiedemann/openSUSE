#
# spec file for package blueman
#
# Copyright (c) 2023 SUSE LLC
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


%global __requires_exclude ^typelib\\(AppIndicator3\\)
%if 0%{?is_opensuse}
%bcond_without caja
%bcond_without nautilus
%bcond_without nemo
%else
%bcond_with caja
%bcond_with nautilus
%bcond_with nemo
%endif
Name:           blueman
Version:        2.3.5
Release:        0
Summary:        GTK Bluetooth Manager
License:        GPL-3.0-only
Group:          System/GUI/GNOME
URL:            https://github.com/blueman-project/blueman
Source:         https://github.com/%{name}-project/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  adwaita-icon-theme
BuildRequires:  automake
BuildRequires:  dbus-1-python3-devel
BuildRequires:  fdupes
# Needed for typelib() - Requires.
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool >= 0.35.0
BuildRequires:  iproute2
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-Cython
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(bluez) >= 5.48
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.27.2
BuildRequires:  pkgconfig(python3)
Requires:       bluez >= 5.48
Requires:       dbus-1-python3
Requires:       gdk-pixbuf-loader-rsvg
Requires:       obex-data-server
Requires:       polkit
Requires:       pulseaudio-utils
Requires:       python3-cairo
Requires:       python3-gobject-Gdk
Requires:       python3-notify2
Requires:       dbus(org.freedesktop.Notifications)
%glib2_gsettings_schema_requires

%description
Blueman provides means for controlling the BlueZ API and presenting
Bluetooth operations such as:

    * Connecting to 3G/EDGE/GPRS via dial-up
    * Connecting to/Creating bluetooth networks
    * Connecting to input devices
    * Connecting to audio devices
    * Sending/Receiving/Browsing files via OBEX
    * Pairing

using a graphical user interface.

%package -n thunar-sendto-%{name}
Summary:        A sendto integration for Thunar
Group:          System/GUI/XFCE
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description -n thunar-sendto-%{name}
This package add sendto integration for Thunar.

%if %{with caja}
%package -n caja-extension-sendto-%{name}
Summary:        A sendto integration for Caja
Group:          System/GUI/Other
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(caja-python)
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description -n caja-extension-sendto-%{name}
This package add sendto integration for Caja.

%files -n caja-extension-sendto-%{name}
%{_datadir}/caja-python/extensions/caja_blueman_sendto.py
%endif

%if %{with nautilus}
%package -n nautilus-extension-sendto-%{name}
Summary:        A sendto integration for Nautilus
Group:          System/GUI/GNOME
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(nautilus-python)
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description -n nautilus-extension-sendto-%{name}
This package add sendto integration for Nautilus.

%files -n nautilus-extension-sendto-%{name}
%{_datadir}/nautilus-python/extensions/nautilus_blueman_sendto.py
%endif

%if %{with nemo}
%package -n nemo-extension-sendto-%{name}
Summary:        A sendto integration for Nemo
Group:          System/GUI/Other
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(nemo-python)
Requires:       %{name} = %{version}-%{release}
Enhances:       nemo
BuildArch:      noarch

%description -n nemo-extension-sendto-%{name}
This package add sendto integration for Nemo.

%files -n nemo-extension-sendto-%{name}
%{_datadir}/nemo-python/extensions/nemo_blueman_sendto.py
%endif

%lang_package

%prep
%autosetup
sed -i '1s/python.*/python3/' apps/%{name}-*
echo -e 'NotShowIn=KDE;GNOME;Pantheon;' >> data/%{name}.desktop.in

%build
%configure \
    --disable-static \
    --enable-polkit \
    --disable-schemas-compile
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
rm -r %{buildroot}%{_datadir}/doc/%{name}

%fdupes %{buildroot}%{python3_sitelib}
%fdupes %{buildroot}%{_datadir}/icons/hicolor

%find_lang %{name}

%suse_update_desktop_file -i %{name}-manager

# Move blueman.rules to docs and leave default security untouched boo#1124339
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/polkit-1/rules.d/blueman.rules %{buildroot}%{_docdir}/%{name}/blueman.rules
rm -rf %{buildroot}%{_datadir}/polkit-1/rules.d

# openSUSE rcFOO links
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcblueman-mechanism
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcblueman-applet

%pre
%service_add_pre blueman-mechanism.service

%post
%service_add_post blueman-mechanism.service

%preun
%service_del_preun blueman-mechanism.service

%postun
%service_del_postun blueman-mechanism.service

%files
%doc CHANGELOG.md FAQ README.md blueman.rules
%license COPYING
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}-*
%{_libexecdir}/%{name}-mechanism
%{_libexecdir}/%{name}-rfcomm-watcher
%{python3_sitelib}/%{name}
%{python3_sitearch}/*%{name}*
%{_datadir}/applications/%{name}-manager.desktop
%{_datadir}/applications/%{name}-adapters.desktop
%{_datadir}/%{name}
%{_datadir}/dbus-1/system-services/org.%{name}.Mechanism.service
%{_datadir}/dbus-1/services/org.%{name}.Applet.service
%{_datadir}/dbus-1/services/org.%{name}.Manager.service
%{_datadir}/dbus-1/system.d/org.%{name}.Mechanism.conf
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/*/blue*.*
%{_mandir}/man*/%{name}-*%{ext_man}
%{_datadir}/polkit-1/actions/org.%{name}.policy
%{_unitdir}/%{name}-mechanism.service
%{_userunitdir}/%{name}-applet.service
%{_userunitdir}/%{name}-manager.service
%{_sbindir}/rcblueman-mechanism
%{_sbindir}/rcblueman-applet

%files -n thunar-sendto-%{name}
%dir %{_datadir}/Thunar
%dir %{_datadir}/Thunar/sendto
%{_datadir}/Thunar/sendto/thunar-sendto-%{name}.desktop

%files lang -f %{name}.lang

%changelog
