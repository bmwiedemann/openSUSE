#
# spec file for package ibus-cangjie
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


%global module_name ibus_cangjie
Name:           ibus-cangjie
Version:        2.4
Release:        0
Summary:        An IBus engine for users of the Cangjie and Quick input methods
License:        GPL-3.0
Group:          System/I18n/Chinese
Url:            http://cangjians.github.io/projects/%{name}
Source:         https://github.com/Cangjians/%{name}/releases/download/v2.4/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE fix_import_version.patch wnereiz@eienteiland.org
# Use python3 'gi' coding import format to insure it can be built success in openSUSE build env.
Patch0:         ibus-cangjie-fix_import_version.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  ibus-devel
BuildRequires:  intltool
BuildRequires:  libcangjie-data
BuildRequires:  libtool
BuildRequires:  python3 >= 3.4
BuildRequires:  python3-cangjie >= 1.2
BuildRequires:  python3-gobject
BuildRequires:  update-desktop-files
Requires:       ibus
Requires:       python3 >= 3.4
Requires:       python3-cangjie >= 1.2
Requires:       python3-gobject
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
IBus engine for users of the Cangjie and Quick input methods.
It is primarily intended to Hong Kong people who want to input Traditional Chinese, as they are (by far) the majority of Cangjie and Quick users. However, it should work for others as well (e.g to input Simplified Chinese).

%prep
%autosetup -p1

%build
%configure --srcdir=%{_builddir}/%{name}-%{version}
make %{?_smp_mflags}

%install
%make_install

%fdupes -s %{buildroot}/%{python3_sitelib}/

rename cangjie\. ibus-setup-cangjie\. %{buildroot}%{_datadir}/icons/hicolor/*/intl/*
rename quick\. ibus-setup-quick\. %{buildroot}%{_datadir}/icons/hicolor/*/intl/*

%suse_update_desktop_file -G 'IBus Cangjie Setup' ibus-setup-cangjie Utility DesktopUtility System
%suse_update_desktop_file ibus-setup-quick Utility DesktopUtility System

%find_lang %{name}

%check
make %{?_smp_mflags} check

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README.md
%license COPYING
%{_bindir}/ibus-setup-cangjie
%{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/ibus-engine-cangjie
%{python3_sitelib}/%{module_name}
%{_datadir}/%{name}
%{_datadir}/%{name}/setup.ui
%dir %{_datadir}/appdata
%{_datadir}/appdata/cangjie.appdata.xml
%{_datadir}/appdata/quick.appdata.xml
%{_datadir}/ibus/component/cangjie.xml
%{_datadir}/ibus/component/quick.xml
%{_datadir}/applications/ibus-setup-cangjie.desktop
%{_datadir}/applications/ibus-setup-quick.desktop
%{_datadir}/glib-2.0/schemas/org.cangjians.ibus.*.gschema.xml
%{_datadir}/icons/hicolor/*/intl/*

%changelog
