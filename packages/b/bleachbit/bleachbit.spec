#
# spec file for package bleachbit
#
# Copyright (c) 2025 SUSE LLC and contributors
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
# 'typelib(AppIndicator)' doesn't exist anymore. It is a fallback if AppIndicator3 can't be found (bleachbit/GUI.py:50)
%global         __requires_exclude typelib\\(AppIndicator\\)
Name:           bleachbit
Version:        5.0.0
Release:        0
Summary:        Tool for removing unnecessary files, freeing space, and maintaining privacy
License:        GPL-3.0-only
Group:          Productivity/File utilities
URL:            https://www.bleachbit.org/
Source:         https://github.com/bleachbit/bleachbit/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  dbus-1
BuildRequires:  e2fsprogs
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-chardet
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-psutil
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
BuildRequires:  update-desktop-files
BuildRequires:  util-linux
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(systemd)
BuildRequires:  typelib(Notify)
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

# Remove test dependency on python3-mock
sed -i 's/^import mock/import unittest.mock as mock/' tests/*.py

# These two use network
sed -Ei 's/(test_download_url_to_fn|test_Chaff|test_have_models)/_\1/g' tests/TestChaff.py
# These four use network
sed -Ei 's/(test_update_url|test_update_winapp2|test_get_ip_for_url)/_\1/g' tests/TestUpdate.py
# These use network
sed -Ei 's/(test_download_url_to_fn|test_fetch_url_nonretry|test_fetch_url_retry|test_get_ip_for_url)/_\1/g' tests/TestNetwork.py
# Tests fail / use network
sed -Ei 's/(test_notify|test_chaff)/_\1/g' tests/TestGUI.py
# Tests fail / use network
sed -Ei 's/(test_get_real_uid)/_\1/g' tests/TestGeneral.py
# Test is very slow
sed -Ei 's/(test_wipe_path)/_\1/g' tests/TestFileUtilities.py
# Wants to mount
sed -Ei 's/(test_same_partition)/_\1/g' tests/TestFileUtilities.py

%build
%make_build -C po local
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
%fdupes %{buildroot}

# Fix non-executable-script
chmod +x %{buildroot}%{_datadir}/%{name}/CLI.py
chmod +x %{buildroot}%{_datadir}/%{name}/GUI.py

%check
export PATH=$PATH:/sbin
export ALLTESTS=1
touch ~/.profile
xvfb-run make tests

%files
%doc README.md doc/*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{_desktopname}.desktop
%{_datadir}/applications/%{_desktopname}-root.desktop
%{_datadir}/metainfo/%{_desktopname}.metainfo.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-indicator.svg
%{_datadir}/polkit-1/actions/org.%{name}.policy

%files lang -f %{name}.lang

%changelog
