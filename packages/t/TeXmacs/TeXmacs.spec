#
# spec file for package TeXmacs
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 8/2011 - now  open-slx GmbH <Sascha.Manns@open-slx.de>
# Copyright (c) 2009 - 7/2011 Sascha Manns <saigkill@opensuse.org>
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


%define rev 15315

Name:           TeXmacs
Version:        2.1.5
Release:        0
Summary:        A Structured WYSIWYG Scientific Text Editor
License:        GPL-3.0-or-later
URL:            https://www.texmacs.org
Source:         %{name}-%{version}-src.tar.gz
Patch1:         Reproducibility.patch

BuildRequires:  fdupes
BuildRequires:  fontpackages-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-devel
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pkgconfig
BuildRequires:  png++-devel
BuildRequires:  pspell-devel
BuildRequires:  rsync
BuildRequires:  shared-mime-info
BuildRequires:  texinfo
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  perl(Digest::SHA)
BuildRequires:  pkgconfig(default-icon-theme)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(xcb)

# Qt6
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-tools-devel
BuildRequires:  qt6-wayland-devel
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)

%description
GNU TeXmacs is a free wysiwyw (what you see is what you want) editing
platform with special features for scientists. The software aims to provide
a unified and user friendly framework for editing structured documents with
different types of content (text, graphics, mathematics, interactive content,
etc.). The rendering engine uses high-quality typesetting algorithms so as to
produce professionally looking documents, which can either be printed out
or presented from a laptop.

The software includes a text editor with support for mathematical formulas,
a small technical picture editor and a tool for making presentations from
a laptop. Moreover, TeXmacs can be used as an interface for many external
systems for computer algebra, numerical analysis, statistics, etc.
New presentation styles can be written by the user and new features can be
added to the editor using the Scheme extension language. A native spreadsheet
and tools for collaborative authoring are planned for later.

TeXmacs runs on all major Unix platforms and Windows. Documents can be
saved in TeXmacs, Xml or Scheme format and printed as Postscript or
Pdf files. Converters exist for TeX/LaTeX and Html/Mathml.

%prep
%autosetup -p1 -n %{name}-%{version}.%{rev}

%build
export PATH="%{_qt6_bindir}:%{_qt6_libexecdir}:$PATH"
export QT_SELECT=qt6
%set_build_flags
export CFLAGS="$CFLAGS -Wno-error=return-type"
export CXXFLAGS="$CXXFLAGS -Wno-error=return-type"
export LDFLAGS="$LDFLAGS -pthread -ldl -Wl,--copy-dt-needed-entries"

./configure --prefix=%{_prefix} \
            --with-qt-find-method=pkgconfig \
            --with-guile=embedded18 \
            --with-gnutls=yes

cp -rf tm-guile188/ice-9 ./TeXmacs/progs/
%make_build TEXMACS

%install
export XDG_UTILS_INSTALL_MODE=system
%make_install

mkdir -p %{buildroot}%{_datadir}/mime/packages
install -m 0644 TeXmacs/misc/mime/texmacs.xml %{buildroot}%{_datadir}/mime/packages/texmacs.xml

# Fix python shebangs
find %{buildroot} -type f -name "*.py" -exec sed -i 's|^#!/usr/bin/env python.*$|#!/usr/bin/python3|' {} +

%suse_update_desktop_file -i texmacs

%fdupes %{buildroot}/%{_datadir}

%files
%license %{_datadir}/%{name}/LICENSE
%{_bindir}/fig2ps
%{_bindir}/texmacs
%doc %{_datadir}/%{name}/examples
%doc %{_datadir}/%{name}/doc
%doc %{_datadir}/%{name}/texts
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/bin
%{_includedir}/%{name}.h
%{_mandir}/man1/fig2ps.1%{?ext_man}
%{_mandir}/man1/texmacs.1%{?ext_man}
%{_datadir}/icons/hicolor/*/*/*texmacs*
%{_datadir}/applications/texmacs.desktop
%dir %{_datadir}/icons/hicolor/*x*
%dir %{_datadir}/icons/hicolor/*x*/apps
%dir %{_datadir}/icons/hicolor/*x*/mimetypes
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/mime/packages/texmacs.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/langs
%{_datadir}/%{name}/packages
%{_datadir}/%{name}/misc
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/progs
%{_datadir}/%{name}/styles

%changelog
