#
# spec file for package bleachbit
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 8/2011 by open-slx GmbH <Sascha.Manns@open-slx.de>
# Copyright (c) 2010 - 7/2011 by Sascha Manns <saigkill@opensuse.org>
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


%define         _desktopname       org.bleachbit.BleachBit

Name:           bleachbit
Version:        4.0.0
Release:        0
Summary:        Tool for removing unnecessary files, freeing space, and maintaining privacy
License:        GPL-3.0-only
Group:          Productivity/File utilities
URL:            https://www.bleachbit.org/
Source:         https://github.com/bleachbit/bleachbit/archive/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  kf5-filesystem
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(systemd)
Requires:       python3
Requires:       python3-chardet
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-xml
Requires:       xdg-utils
BuildArch:      noarch
%lang_package

%description
BleachBit deletes unnecessary files to free valuable disk space and
maintain privacy. Rid your system of old junk including broken
menu entries, cache, cookies, localizations, and temporary files.
Designed for Linux  systems, it wipes clean Bash, Beagle, Epiphany,
Firefox, Flash, GNOME, Java, KDE, OpenOffice.org, Opera, RealPlayer,
VIM, XChat, and more.

%prep
%setup -q
sed -i -e 's|%{_bindir}/env python.*|%{_bindir}/python3|g' \
        bleachbit/{CLI.py,GUI.py} bleachbit.py

%build
make -C po local %{?_smp_mflags}
python3 setup.py build

%install
make DESTDIR=%{buildroot} install prefix=%{_prefix}

# create root desktop-file and change exec
cp %{_desktopname}.desktop %{_desktopname}-root.desktop
sed -i -e 's/Name=BleachBit$/Name=BleachBit as Administrator/g' \
        %{_desktopname}-root.desktop
sed -i -e 's/^Exec=bleachbit$/Exec=xdg-su -c bleachbit/g' \
        %{_desktopname}-root.desktop
# installing .desktop Files
%suse_update_desktop_file -n    %{_desktopname}      Utility Filesystem
%suse_update_desktop_file -n -i %{_desktopname}-root Utility Filesystem

%find_lang %{name}
%fdupes -s %{buildroot}

# Fix non-executable-script
chmod +x %{buildroot}%{_datadir}/%{name}/CLI.py
chmod +x %{buildroot}%{_datadir}/%{name}/GUI.py

%files
%doc README.md doc/*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{_desktopname}.desktop
%{_datadir}/applications/%{_desktopname}-root.desktop
%{_datadir}/metainfo/%{_desktopname}.metainfo.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/polkit-1/actions/org.%{name}.policy

%files lang -f %{name}.lang

%changelog
