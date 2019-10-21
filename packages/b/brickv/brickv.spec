#
# spec file for package brickv
#
# Copyright (c) 2019 Frank Kunz
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           brickv
Version:        2.4.9
Release:        0
Summary:        Tinkerforge Brick Viewer
License:        GPL-2.0-only
Group:          Development/Tools/Debuggers
Url:            http://www.tinkerforge.com
Source0:        https://github.com/Tinkerforge/brickv/archive/v%{version}.tar.gz
Patch0:         0001-Support-to-use-local-iso-codes-and-mobile-providers-.patch
Patch1:         0002-Fix-shebang.patch
BuildRequires:  python3-setuptools
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-qt5
BuildRequires:  fdupes
BuildRequires:  mobile-broadband-provider-info
BuildRequires:  iso-codes
BuildRequires:  update-desktop-files
Requires:       python3-qt5
Requires:       python3-serial
Requires:       python3-pytz
Requires:       python3-tzlocal
BuildArch:      noarch

%description
Small Qt GUI to control and test all Bricks and Bricklets from Tinkerforge.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export SERVICEPROVIDERS_XML_PATH=/usr/share/mobile-broadband-provider-info/serviceproviders.xml
export ISOCODES_JSON_PATH=/usr/share/iso-codes/json/iso_3166-1.json
# force UTF-8 for build scripts
export LANG=C.UTF-8
pushd src
python3 build_src.py
# remove no more needed build scripts
rm -f build_src.py brickv/plugin_system/plugins/red/build_extra.py brickv/plugin_system/plugins/red/build_scripts.py
popd

%install
pushd src
python3 setup.py install --root=%{buildroot} --prefix=/usr
install -m 644 -D -t %{buildroot}%{_libexecdir}/udev/rules.d build_data/linux/%{name}/lib/udev/rules.d/99-tinkerforge-brickv.rules
install -m 644 -D -t %{buildroot}/usr/share/pixmaps build_data/linux/%{name}/usr/share/pixmaps/brickv-icon.png
install -m 644 -D -t %{buildroot}/usr/share/applications build_data/linux/%{name}/usr/share/applications/%{name}.desktop
popd
%fdupes -s %{buildroot}%{python3_sitelib}/brickv/
%suse_update_desktop_file -r %{name} Development Debugger

%files -n %{name}
%doc src/changelog README.rst
%{_bindir}/%{name}
%{python3_sitelib}/brickv*
%{_libexecdir}/udev/rules.d/*.rules
/usr/share/pixmaps/*
/usr/share/applications/*


%changelog
