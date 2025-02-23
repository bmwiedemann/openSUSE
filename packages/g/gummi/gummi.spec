#
# spec file for package gummi
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gummi
Version:        0.8.3
Release:        0
Summary:        Simple LaTeX editor
License:        MIT
Group:          Productivity/Publishing/TeX/Frontends
URL:            https://github.com/alexandervdm/gummi
Source0:        https://github.com/alexandervdm/gummi/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  texlive-synctex-devel
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.4
BuildRequires:  pkgconfig(gtkspell3-3.0) >= 3.0
BuildRequires:  pkgconfig(poppler-glib)
Requires:       texlive-latex
Requires:       texlive-synctex
Recommends:     %{name}-lang

%description
Gummi is a LaTeX editor written using the GTK+ toolkit. It was designed with
simplicity in mind, but is useful for both novice and advanced LaTeX writers.

%lang_package

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/

%files
%doc AUTHORS ChangeLog
%license COPYING
%{_mandir}/man*/*.1%{?ext_man}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/
%{_libdir}/%{name}/

%files lang -f %{name}.lang

%changelog
