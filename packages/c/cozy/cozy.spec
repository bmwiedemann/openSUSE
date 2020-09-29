#
# spec file for package cozy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cozy
Version:        0.7.2
Release:        0
Summary:        Audio Book Player
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/geigi
Source0:        https://github.com/geigi/cozy/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       python3-cairo
Requires:       python3-distro
Requires:       python3-gst
Requires:       python3-magic
Requires:       python3-mutagen
Requires:       python3-peewee >= 3.9.6
Requires:       python3-apsw
Requires:       python3-pytaglib
Requires:	python3-pytz
Requires:	python3-requests
Requires:	python3-packaging
Recommends:     %{name}-lang
Recommends:     gstreamer-plugins-base
Recommends:     gstreamer-plugins-good
Recommends:     gstreamer-plugins-ugly
Conflicts:      com.github.geigi.cozy
Provides:       com.github.geigi.cozy = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-cairo
BuildRequires:  python3-gst
BuildRequires:  python3-magic
BuildRequires:  python3-mutagen
BuildRequires:  python3-peewee >= 3.9.6
BuildRequires:  python3-pytaglib
BuildRequires:  python3-distro
BuildRequires:  python3-apsw
BuildRequires:  python3-packaging
# /SECTION

%description
Play and organize your audio book collection.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file com.github.geigi.cozy
%find_lang com.github.geigi.cozy %{name}.lang
%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{python3_sitelib}

%files
%defattr(0644,root,root,0755)
%license LICENSE
%doc AUTHORS README.md
%attr(0755,root,root) %{_bindir}/com.github.geigi.cozy
%{_datadir}/applications/com.github.geigi.cozy.desktop
%{_datadir}/glib-2.0/schemas/com.github.geigi.cozy.gschema.xml
%{_datadir}/metainfo/com.github.geigi.cozy.appdata.xml
%{_datadir}/icons/hicolor/*/*/*.??g
%{_datadir}/com.github.geigi.cozy/
%{python3_sitelib}/cozy/

%files lang -f %{name}.lang

%changelog
