#
# spec file for package nfoview
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


Name:           nfoview
Version:        2.1
Release:        0
Summary:        Simple Viewer for NFO Files
License:        GPL-3.0-or-later
URL:            https://otsaloma.io/nfoview/
Source:         https://github.com/otsaloma/nfoview/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  python3-base
Requires:       python3
Requires:       python3-cairo
Requires:       python3-gobject-Gdk
Requires:       typelib(Gtk) = 4.0
Requires:       typelib(Pango) = 1.0
Requires:       typelib(PangoCairo) = 1.0
Recommends:     saja-cascadia-code-fonts
BuildArch:      noarch

%description
NFO Viewer is a simple viewer for NFO files, which are "ASCII" art in
the CP437 codepage. The advantages of using NFO Viewer instead of a text
editor are preset font and encoding settings, automatic window size and
clickable hyperlinks.

%lang_package

%prep
%autosetup -p1

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}
sed -i '1s|#!%{_bindir}/env python3|#!%{_bindir}/python3|' %{buildroot}%{_bindir}/%{name}
desktop-file-install --add-category="Office" --delete-original \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/io.otsaloma.nfoview.desktop
%find_lang %{name}
python3 -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{_datadir}/%{name}

%check
# import nfoview pulls GTK 4 and segfaults without a display (upstream
# disabled pytest for the same reason). Compile-check the installed modules.
python3 -m py_compile %{buildroot}%{_datadir}/%{name}/nfoview/*.py
desktop-file-validate %{buildroot}%{_datadir}/applications/io.otsaloma.nfoview.desktop

%files
%doc AUTHORS.md NEWS.md README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo/io.otsaloma.nfoview.appdata.xml
%{_datadir}/applications/io.otsaloma.nfoview.desktop
%{_datadir}/icons/hicolor/*/apps/io.otsaloma.nfoview*.svg
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
