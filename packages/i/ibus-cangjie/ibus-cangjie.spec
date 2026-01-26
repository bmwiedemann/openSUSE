#
# spec file for package ibus-cangjie
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global module_name ibus_cangjie
Name:           ibus-cangjie
Version:        2.5
Release:        0
Summary:        An IBus engine for users of the Cangjie and Quick input methods
License:        GPL-3.0-only
Group:          System/I18n/Chinese
URL:            http://cangjians.github.io/projects/%{name}
Source:         https://gitlab.freedesktop.org/cangjie/%{name}/-/archive/2.5/%{name}-%{version}.tar.bz2
BuildRequires:  %{python_module coverage}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  ibus-devel
BuildRequires:  intltool
BuildRequires:  libcangjie-data
BuildRequires:  libtool
BuildRequires:  meson >= 1.3.2
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
%meson
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}/%{python3_sitelib}/

cangjie_docdir=%{buildroot}%{_datadir}/doc/%{name}
suse_docdir=%{buildroot}%{_docdir}/%{name}
doc_files=(AUTHORS README.md)

if [ ! -d "$suse_docdir" ]; then
    mkdir -p "$suse_docdir"
fi

for file in "${doc_files[@]}"; do
    if [ -e "$cangjie_docdir/$file" ]; then
        mv "$cangjie_docdir/$file" "$suse_docdir"
    fi
done

if [ -d "$cangjie_docdir" ] && \
   [ -z "$(ls -A "$cangjie_docdir")" ]; then
    rmdir "$cangjie_docdir"
fi

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README.md
%license COPYING
%{_bindir}/ibus-setup-cangjie
%{python3_sitelib}/%{module_name}
%{_libexecdir}/ibus-engine-cangjie
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/setup.ui
%{_datadir}/%{name}/setup.css
%{_datadir}/ibus/component/org.freedesktop.cangjie.ibus.Cangjie.xml
%{_datadir}/ibus/component/org.freedesktop.cangjie.ibus.Quick.xml
%{_datadir}/applications/ibus-setup-cangjie.desktop
%{_datadir}/applications/ibus-setup-quick.desktop
%{_datadir}/applications/org.freedesktop.cangjie.ibus.cangjie-setup.desktop
%{_datadir}/applications/org.freedesktop.cangjie.ibus.quick-setup.desktop
%{_datadir}/glib-2.0/schemas/org.cangjians.ibus.cangjie.gschema.xml
%{_datadir}/glib-2.0/schemas/org.cangjians.ibus.quick.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.cangjie.ibus.Cangjie.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.cangjie.ibus.Quick.gschema.xml
%{_datadir}/metainfo/org.freedesktop.cangjie.ibus.Cangjie.metainfo.xml
%{_datadir}/metainfo/org.freedesktop.cangjie.ibus.Quick.metainfo.xml
%{_datadir}/icons/hicolor/16x16/intl/org.freedesktop.cangjie.ibus.Cangjie.png
%{_datadir}/icons/hicolor/16x16/intl/org.freedesktop.cangjie.ibus.Quick.png
%{_datadir}/icons/hicolor/scalable/intl/org.freedesktop.cangjie.ibus.Cangjie.svg
%{_datadir}/icons/hicolor/scalable/intl/org.freedesktop.cangjie.ibus.Quick.svg

%changelog
