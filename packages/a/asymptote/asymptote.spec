#
# spec file for package asymptote
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


%bcond_with lsp
Name:           asymptote
Version:        3.15
Release:        0
Summary:        2D & 3D TeX-Aware vector graphics language
License:        LGPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://asymptote.sourceforge.io/
#Git-Clone:     https://github.com/vectorgraphics/asymptote
Source:         https://github.com/vectorgraphics/asymptote/archive/refs/tags/%version.tar.gz
#NEWS:          https://asymptote.sourceforge.io/ReleaseNotes
Patch1:         use-system-libs.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
%if %{with lsp}
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%endif
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
BuildRequires:  python-rpm-macros
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-kpathsea-bin
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  xz
BuildRequires:  pkgconfig(atomic_ops)
BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  libglfw-devel
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  tex(media9.sty)
BuildRequires:  tex(parskip.sty)
BuildRequires:  tex(type1cm.sty)
Conflicts:      texlive-asymptote
Conflicts:      texlive-asymptote-bin
Conflicts:      texlive-asymptote-doc
Provides:       bundled(glew) = 2.2.0

%description
Asymptote is a descriptive vector graphics language for technical
drawing, inspired by MetaPost, but with a C++-like syntax. Asymptote
provides for figures the same quality of typesetting that LaTeX does
for scientific text.

%prep
%autosetup
rm -Rfv libatomic_ops gc

%build
if [ ! -e configure ]; then autoreconf -fiv; fi
%configure --with-docdir="%_docdir/%name"
%make_build

%install
b="%buildroot"
%make_install
mv -v "$b/usr/local/share"/* "$b/%_datadir/"
chmod a-x "$b/%_datadir/asymptote/shaders"/*.glsl
find "$b/%_datadir/asymptote/GUI" -type f -name "*.py" \
	-exec perl -i -lpe "s{^#!/usr/bin/env python3}{#!/usr/bin/python%python3_bin_suffix}g" {} +

mkdir -pv "$b/%_libdir" "$b/%_datadir/licenses"
mv -v "$b/%_docdir/asymptote/licenses" "$b/%_datadir/licenses/%name"
# move misplaced dlopened extensions
mv -v "$b/%_datadir/%name"/libasy*.so "$b/%_libdir/"

%files
%_bindir/asy
%_bindir/xasy
%_libdir/libasy*.so
%_datadir/%name/
%_datadir/texmf/
%_docdir/%name/
%_infodir/asy*
%_mandir/*/*asy.1*
%_datadir/licenses/*

%changelog
