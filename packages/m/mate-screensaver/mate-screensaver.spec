#
# spec file for package mate-screensaver
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


%define _version 1.28

Name:           mate-screensaver
Version:        1.28.0
Release:        0
Summary:        MATE Desktop screensaver
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE mate-screensaver-1.7.1-vendor_pam_integration.patch nmarques@mate-desktop.org -- PAM integration with SUSE.
Patch0:         mate-screensaver-1.7.1-vendor_pam_integration.patch
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xscreensaver-data
BuildRequires:  xscreensaver-data-extra
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libmate-menu) >= %{_version}
BuildRequires:  pkgconfig(libmatekbdui)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(mate-desktop-2.0) >= %{_version}
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)
Requires:       mate-session-manager-gschemas >= %{_version}
Recommends:     %{name}-lang
Recommends:     xscreensaver-data
Suggests:       mate-power-manager >= %{_version}
%glib2_gsettings_schema_requires

%description
mate-screensaver is a screen saver and locker that integrates with
the MATE desktop.

%package devel
Summary:        Development files for mate-screensaver
Requires:       %{name} = %{version}

%description devel
mate-screensaver is a screen saver and locker that integrates with
the MATE desktop.

This subpackage contains the pkgconfig file.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure  \
  --libexecdir=%{_libexecdir}/%{name} \
  --with-xscreensaverdir=%{_sysconfdir}/xscreensaver \
  --with-pam-prefix=%{_sysconfdir}    \
  --with-systemd                      \
  --without-console-kit               \
  --disable-docbook-docs
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}

pushd %{buildroot}%{_datadir}/applications/
for desktop in $(ls | grep \.desktop); do
    %suse_update_desktop_file %{buildroot}%{_datadir}/applications/$desktop
done
popd

%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/mate-screensaver %{buildroot}%{_pam_vendordir}

%pre
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/mate-screensaver ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/mate-screensaver ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files
%license COPYING COPYING.LIB
%doc README NEWS
%dir %{_sysconfdir}/xdg/menus/
%config %{_sysconfdir}/xdg/menus/mate-screensavers.menu
%config %{_sysconfdir}/xdg/autostart/mate-screensaver.desktop
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/mate-screensaver
%else
%config %{_sysconfdir}/pam.d/mate-screensaver
%endif
%{_bindir}/%{name}*
%{_libexecdir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/applications/screensavers/
%{_datadir}/backgrounds/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/desktop-directories/
%{_datadir}/mate-background-properties/
%{_datadir}/%{name}/
%{_datadir}/pixmaps/gnome-logo-white.svg
%{_datadir}/pixmaps/mate-logo-white.svg
%{_datadir}/glib-2.0/schemas/*.xml
%{_mandir}/man?/*.?%{?ext_man}

%files devel
%{_libdir}/pkgconfig/mate-screensaver.pc

%files lang -f %{name}.lang

%changelog
