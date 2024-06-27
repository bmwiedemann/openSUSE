#
# spec file for package TeXmacs
#
# Copyright (c) 2024 SUSE LLC
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


Name:           TeXmacs
Version:        2.1.4
Release:        0
Summary:        A Structured WYSIWYG Scientific Text Editor
License:        GPL-3.0-or-later
URL:            https://www.texmacs.org/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(guile-1.8)
BuildRequires:  pkgconfig(python3)

%description
GNU TeXmacs is a free scientific text editor, inspired by TeX and GNU
Emacs. The editor allows you to write structured documents via a
WYSIWYG (what-you-see-is-what-you-get) and user friendly interface. New
styles can be created by the user. The program implements high-quality
typesetting algorithms and TeX fonts, which help you to produce
professional looking documents.

The high typesetting quality still goes through for automatically
generated formulas, which makes TeXmacs suitable as an interface for
computer algebra systems. TeXmacs also supports the Guile/Scheme
extension language, so that you may customize the interface and write
your own extensions to the editor.

%package examples
Summary:        A Structured WYSIWYG Scientific Text Editor
Group:          Productivity/Scientific/Other

%description examples
GNU TeXmacs is a free scientific text editor, inspired by TeX and GNU
Emacs. The editor allows you to write structured documents via a
WYSIWYG (what-you-see-is-what-you-get) and user friendly interface. New
styles can be created by the user. The program implements high-quality
typesetting algorithms and TeX fonts, which help you to produce
professional looking documents.

The high typesetting quality still goes through for automatically
generated formulas, which makes TeXmacs suitable as an interface for
computer algebra systems. TeXmacs also supports the Guile/Scheme
extension language, so that you may customize the interface and write
your own extensions to the editor.

%prep
%autosetup

%build
ARCH_FLAGS="`echo %{optflags} | sed -e 's|-Werror=return-type||g'`"
export CFLAGS="${ARCH_FLAGS}"
export CXXFLAGS="${ARCH_FLAGS}"
%configure
%make_build TEXMACS

%install
export XDG_UTILS_INSTALL_MODE=system

%make_install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/mime/packages
install -m 0644 TeXmacs/misc/mime/texmacs.xml %{buildroot}%{_datadir}/mime/packages/texmacs.xml

%suse_update_desktop_file -i texmacs

%fdupes %{buildroot}/%{_prefix}

%files
%{_bindir}/fig2ps
%{_bindir}/texmacs
%{_includedir}/TeXmacs.h
%{_mandir}/man1/fig2ps.1%{?ext_man}
%{_mandir}/man1/texmacs.1%{?ext_man}
%doc %{_datadir}/TeXmacs/examples
%doc %{_datadir}/TeXmacs/doc
%license %{_datadir}/TeXmacs/LICENSE
%doc %{_datadir}/TeXmacs/texts
%{_datadir}/icons/hicolor/*/*/*texmacs*
%{_datadir}/pixmaps/*.xpm
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/texmacs.xml
%dir %{_datadir}/TeXmacs
%{_libexecdir}/TeXmacs/bin/*
%{_libexecdir}/TeXmacs/
%{_libexecdir}/TeXmacs/bin
%{_datadir}/TeXmacs/fonts
%{_datadir}/TeXmacs/langs
%{_datadir}/TeXmacs/packages
%{_datadir}/TeXmacs/misc
%{_datadir}/TeXmacs/plugins
%{_datadir}/TeXmacs/progs
%{_datadir}/TeXmacs/styles
%{_datadir}/icons/hicolor

%changelog
