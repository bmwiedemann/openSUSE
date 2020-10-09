#
# spec file for package ibus-hangul
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ibus-hangul
Version:        1.5.3
Release:        0
Summary:        The Hangul engine for IBus input platform
License:        GPL-2.0-or-later
Group:          System/I18n/Korean
URL:            https://github.com/libhangul/ibus-hangul
Source:         https://github.com/libhangul/ibus-hangul/archive/1.5.3/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gnome-common
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libhangul)
BuildRequires:  pkgconfig(python3)
Requires:       python3-gobject
# Make sure there is a font available. Pango 1.44 requires
# a scalable font. However, since scalable-font-ko does not
# pull the current default Korean font, Noto Sans KR, thereby
# this spec files specifies its concrete font package name.
Requires:       scalable-font-ko
Recommends:     noto-sans-kr-fonts
Provides:       locale(ibus:ko)

%description
The Hangul engine for IBus platform. It provides Korean input method from
libhangul.

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static \
           --libexecdir=%{_ibus_libdir}
%make_build

%install
%make_install
%suse_update_desktop_file ibus-setup-hangul Utility DesktopUtility System
ln -sf %{_ibus_libdir}/ibus-setup-hangul %{buildroot}%{_bindir}/ibus-setup-hangul

%find_lang %{name}
%fdupes %{buildroot}

%files -f %{name}.lang
# /usr/share/licenses is not owned by any package on SLE 12 SP2 and older
%license COPYING
%doc AUTHORS README
%{_bindir}/ibus-setup-hangul
%{_ibus_libdir}/ibus-engine-hangul
%{_ibus_libdir}/ibus-setup-hangul
%{_ibus_componentdir}/hangul.xml
%{_datadir}/applications/ibus-setup-hangul.desktop
%{_datadir}/icons/hicolor/64x64/apps/ibus-*.png
%{_datadir}/icons/hicolor/scalable/apps/ibus-*.svg
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.hangul.gschema.xml
%{_datadir}/metainfo/org.freedesktop.ibus.engine.hangul.metainfo.xml

%changelog
