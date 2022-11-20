#
# spec file for package asymptote
#
# Copyright (c) 2022 SUSE LLC
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
Version:        2.83
Release:        0
Summary:        2D & 3D TeX-Aware vector graphics language
License:        LGPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://asymptote.sourceforge.io/

#Git-Clone:     https://github.com/vectorgraphics/asymptote
Source:         https://github.com/vectorgraphics/asymptote/archive/refs/tags/%version.tar.gz
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
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-kpathsea-bin
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  xz
BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  tex(media9.sty)
BuildRequires:  tex(parskip.sty)
Conflicts:      texlive-asymptote
Conflicts:      texlive-asymptote-bin
Conflicts:      texlive-asymptote-doc

%description
Asymptote is a descriptive vector graphics language for technical
drawing, inspired by MetaPost, but with a C++-like syntax. Asymptote
provides for figures the same quality of typesetting that LaTeX does
for scientific text.

%prep
%autosetup
rm -fv libatomic_ops-*.tar.gz gc-*.tar.gz

%build
if [ ! -e configure ]; then autoreconf -fiv; fi
%configure --with-docdir="%_docdir/%name"
%make_build

%install
%make_install
mv "%buildroot/usr/local/share"/* "%buildroot/%_datadir/"
chmod a-x "%buildroot/%_datadir/asymptote/shaders"/*.glsl
find "%buildroot/%_datadir/asymptote/GUI" -type f -name "*.py" \
	-exec perl -i -lpe 's{^#!/usr/bin/env }{#!/usr/bin/}g' {} +

%files
%_bindir/asy
%_bindir/xasy
%_datadir/%name/
%_datadir/texmf/
%_docdir/%name/
%_infodir/asy*
%_mandir/*/*asy.1*
%license LICENSE*

%changelog
