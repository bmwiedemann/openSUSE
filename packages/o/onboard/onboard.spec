#
# spec file for package onboard
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


%define series 1.4
%define pythons python3
%define srcver 1.4.3-7
Name:           onboard
Version:        1.4.3.7
Release:        0
Summary:        Simple on-screen Keyboard
License:        GPL-3.0-only
Group:          System/X11/Utilities
URL:            https://github.com/dr-ni/onboard
Source:         https://github.com/dr-ni/onboard/archive/refs/tags/%{srcver}.tar.gz#/onboard-%{srcver}.tar.gz
Source1:        onboard-defaults.conf
Patch0:         onboard-fix-crash-on-hover.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# Needed for typelib() - Requires.
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  librsvg-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xtst)
Requires:       dbus-1-python3
Requires:       gdk-pixbuf-loader-rsvg
Requires:       gsettings-desktop-schemas
Requires:       hicolor-icon-theme
Requires:       iso-codes
Requires:       python3-cairo
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Recommends:     %{name}-data

%description
Onboard is an onscreen keyboard useful for tablet PC users and for mobility impaired users.

%package data
Summary:        Simple On-screen Keyboard
Group:          Productivity/Office/Dictionary
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Language model files for the word suggestion feature of Onboard

%package -n gnome-shell-extension-onboard
Summary:        GNOME Shell extension for onboard, an on-screen keyboard
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)
BuildArch:      noarch

%description -n gnome-shell-extension-onboard
Onboard is an onscreen keyboard useful for tablet PC users and for mobility impaired users.

This GNOME Shell extension integrates the onboard keyboard with the GNOME Shell.

%lang_package

%prep
%autosetup -p1 -n %{name}-%{srcver}

%build
# remove shebang
sed -i "1,4{/#!\/usr\/bin/d}" \
  Onboard/IconPalette.py \
  Onboard/pypredict/lm_wrapper.py \
  Onboard/settings.py \
  Onboard/UnicodeData.py \
  data/layoutstrings.py

%pyproject_wheel

%install
%pyproject_install
install -dm 0755 %{buildroot}%{_datadir}/locale
cp -a build/mo/* %{buildroot}%{_datadir}/locale/

install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/
rm %{buildroot}%{_datadir}/doc/%{name}/{AUTHORS,CHANGELOG,COPYING*,DBUS.md,HACKING,README.md,*.example}
rm -r %{buildroot}%{_datadir}/icons/ubuntu-mono-*
# this will be built upon installation of the package
rm %{buildroot}/usr/share/glib-2.0/schemas/gschemas.compiled

%if 0%{?suse_version} < 1600
# Manually install onboard-autostart.desktop if distutils.extra is too old...
# Currently, onboard-autostart.desktop installation only works on openSUSE:Factory.
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
cp -a build/share/autostart/onboard-autostart.desktop %{buildroot}%{_sysconfdir}/xdg/autostart
%else
mv %{buildroot}%{python3_sitearch}%{_sysconfdir} %{buildroot}
%endif

rm -r %{buildroot}%{_datadir}/icons/hicolor/28x28

%suse_update_desktop_file -i -r %{name} Utility Accessibility
%suse_update_desktop_file -i -r %{name}-settings Utility Accessibility

%fdupes %{buildroot}%{python3_sitearch}/
%fdupes %{buildroot}%{_datadir}/onboard/models/

%find_lang %{name}

%files
%doc AUTHORS CHANGELOG DBUS.md README.md HACKING *.example
%license COPYING*
%{_bindir}/%{name}
%{_bindir}/%{name}-settings
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/tools/
%{_datadir}/%{name}/emojione/
%{_datadir}/%{name}/tools/checkmodels
%{_datadir}/%{name}/layouts/
%{_datadir}/%{name}/scripts/
%{_datadir}/%{name}/themes/
%{_datadir}/%{name}/layoutstrings.py
%{_datadir}/%{name}/%{name}-defaults.conf*
%{_datadir}/%{name}/settings*.ui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%dir %{_datadir}/icons/HighContrast
%dir %{_datadir}/icons/HighContrast/symbolic
%dir %{_datadir}/icons/HighContrast/symbolic/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}*.svg
%{_datadir}/icons/HighContrast/symbolic/apps/%{name}.svg
%dir %{_datadir}/sounds/freedesktop
%dir %{_datadir}/sounds/freedesktop/stereo
%{_datadir}/sounds/freedesktop/stereo/%{name}-key-feedback.oga
%{_datadir}/dbus-1/services/org.%{name}.Onboard.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{python3_sitearch}/Onboard/
%{python3_sitearch}/%{name}-%{series}.*.dist-info
%{python3_sitearch}/__pycache__/settings_ui.cpython*.pyc
%{python3_sitearch}/settings_ui.py
%{python3_sitearch}/%{name}-%{series}.*.dist-info
%{_datadir}/icons/hicolor/*/apps/onboard.png
%{_mandir}/man1/onboard.1%{?ext_man}
%{_mandir}/man1/onboard-settings.1%{?ext_man}
%config %{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop

%files lang -f %{name}.lang

%files data
%{_datadir}/%{name}/models/

%files -n gnome-shell-extension-onboard
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/extensions
%{_datadir}/gnome-shell/extensions/Onboard_Indicator@onboard.org/

%changelog
