#
# spec file for package gocr
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gocr
Version:        0.52
Release:        0
Summary:        Optical Character Recognition Program
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://www-e.uni-magdeburg.de/jschulen/ocr/index.html
Source0:        https://www-e.uni-magdeburg.de/jschulen/ocr/%{name}-%{version}.tar.gz
Source1:        gocr.desktop
BuildRequires:  ImageMagick
BuildRequires:  ghostscript_any
BuildRequires:  gnu-free-fonts
BuildRequires:  libnetpbm-devel
BuildRequires:  transfig
# Native supported format is pnm, others are imported with helpers
Recommends:     jpeg
Recommends:     netpbm
Recommends:     transfig

%description
GOCR is an optical character recognition program. It reads images in
many formats and outputs a text file. It is also able to recognize
and translate barcodes.

%package gui
Summary:        Optical Character Recognition Program - Basic Graphical Interface
Group:          Productivity/Graphics/Other
Requires:       %{name} = %{version}
Requires:       tk
Supplements:    (gocr and tk)
BuildArch:      noarch

%description gui
GOCR is an optical character recognition program. It reads images in
many formats and outputs a text file. It is also able to recognize
and translate barcodes.

This package contains a basic graphical interface for GOCR.

%prep
%setup -q
# According to "convert -list font", the regular variant is just "FreeMono"
sed -i -e 's,"FreeMono-Regular","FreeMono",' examples/Makefile

# Fix rpmlint warning "hidden-file-or-dir"
rm -f examples/.#Makefile.1.22

# Do not use urandom for examples to make package build reproducible (boo#1062303)
cat > examples/rnd80.png.txt <<EOF
/yErGfRT8Wwbrmrs4EGybmpgVy5au84ELYsFXxMnHCuKTnkRWKI6qGTjCXwCE/ixGYfMyw8Rki4u
J0IBpx2IQZG1bKy7HG+6XlD+3lnU3+NYiSfdAxK9p3yEpCXa2VEakQXPkuVWQ1b010TonIAtAS23
TQgnj2Gq+C9is6KQkK9kMcS3UDoWHYaJDzukARATW3XFcd9WvXzuCl6Cb5KTo/ed2ZbEdLA/rJbu
LBso89YtC4nv+Ltxmb/AB0E4wtQZWeYISVNB3oBqiQZIPEHuAW/vvS664zrge3MS08E1jn8HzBPe
EOF

%build
# configure does not check if netpbm headers are installed in /usr/include/netpbm
export CPPFLAGS=-I%{_includedir}/netpbm
%configure
%make_build
%make_build examples

%install
%make_install

# Fix rpmlint warning "spurious-executable-perm"
chmod 644 %{buildroot}%{_mandir}/man1/gocr.1

# Fix doc files path in manpage
sed -i -e "s|/usr/share/doc/gocr-\\\fBX.XX\\\fR/|%{_docdir}/gocr/|" %{buildroot}%{_mandir}/man1/gocr.1

# Install desktop file
install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"

%files
%license gpl.html
%doc AUTHORS BUGS CREDITS HISTORY README TODO
%doc doc/{examples.txt,gocr.html,unicode.txt}
%doc examples/
%{_mandir}/man1/gocr.1%{?ext_man}
%{_bindir}/gocr

%files gui
%{_bindir}/gocr.tcl
%{_datadir}/applications/gocr.desktop

%changelog
