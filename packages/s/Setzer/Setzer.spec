#
# spec file for package Setzer
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


Name:           Setzer
Version:        66
Release:        0
Summary:        Simple yet full-featured LaTeX editor for GTK/GNOME
License:        GPL-3.0-or-later
URL:            https://www.cvfosammmm.org/setzer/
Source:         https://github.com/cvfosammmm/Setzer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
Requires:       python3-bibtexparser
Requires:       python3-cairo
Requires:       python3-gobject-Gdk
Requires:       python3-pexpect
BuildArch:      noarch

%description
Setzer is an easy to use yet full-featured LaTeX editor for the GNU/Linux
desktop, written in Python with Gtk.

%lang_package

%prep
%autosetup
# Clear out unnecessary hashbangs
find ./ -name "*.py" -exec sed -Ei "1{\@/usr/bin/env python3@d}" {} \;

%build
%meson
%meson_build

%install
%meson_install
%find_lang setzer %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}/%{name}/

sed -Ei "s@/usr/bin/env python3@%{_bindir}/python3@" %{buildroot}%{_bindir}/setzer

%files
%license COPYING
%doc README.md
%{_bindir}/setzer
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/mime/packages/*.mime.xml
%{_mandir}/man1/setzer.1%{?ext_man}
%{python3_sitelib}/setzer/

%files lang -f setzer.lang

%changelog
