#
# spec file for package latex2html
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


%define share_dir %{_datadir}/latex2html
%define _texmfmaindir   %{_datadir}/texmf
Name:           latex2html
Version:        2023
Release:        0
Summary:        LaTeX to HTML Converter
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://github.com/latex2html/latex2html/
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE latex2html-share-dir.diff -- Fix latex2html share dir location, use /usr/share not /usr/share/lib
Patch0:         latex2html-share-dir.diff
BuildRequires:  fdupes
BuildRequires:  ghostscript-fonts-std
BuildRequires:  ghostscript-x11
BuildRequires:  netpbm
BuildRequires:  texlive-dvips
BuildRequires:  texlive-kpathsea
BuildRequires:  texlive-latex
Requires:       ghostscript_any
Requires:       latex2html-pngicons
Requires:       netpbm
Requires:       perl
Requires:       texlive-dvips
Requires:       texlive-latex
Requires:       texlive-preview
BuildArch:      noarch

%description
LaTeX2HTML lets you convert basic LaTeX documents into the HTML
format. This allows both a written and online version even of older
LaTeX texts.

%package pngicons
Summary:        Icons in the PNG format for LateX2HTML
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Utilities

%description pngicons
Icons in the PNG format for the LaTeX to HTML Converter.

%package doc
Summary:        Documentation for the Latex2HTML Converter
License:        GPL-2.0-or-later AND LPPL-1.3c
Group:          Productivity/Publishing/TeX/Utilities

%description doc
This subpackage contains the documentation for the Latex2HTML converter.

%prep
%setup -q
%patch0

%build
# Not autotools based configure
./configure --prefix=%{_prefix}
%make_build
# Build docs
export LATEX2HTMLDIR=$(pwd)
cd docs
make L2H="../latex2html -nouse_pdftex -test_mode" html
find manual -name "*.old" -delete

%install
%make_install
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 latex2html.1 %{buildroot}/%{_mandir}/man1
rm -r %{buildroot}%{share_dir}/{docs,example,dot.latex2html-init}
chmod 755 %{buildroot}%{_datadir}/%{name}/{cweb2html/makemake.pl,cweb2html/cweb2html,makemap,makeseg/makeseg}
%fdupes -s %{buildroot}

%check
%make_build test
find docs/manual tests \( -name \*.log -o -name \*.aux -o -name WARNINGS \) -delete

%files
%doc Changes FAQ README.md TODO dot.latex2html-init
%{_prefix}/lib/latex2html
%dir %{share_dir}
%{share_dir}/*.pm
%{share_dir}/IndicTeX-HTML
%{share_dir}/L2hos
%{share_dir}/XyMTeX-HTML
%{share_dir}/cweb2html
%{share_dir}/foilhtml
%{share_dir}/icons/*.html
%{share_dir}/icons/*.gif
%{share_dir}/makemap
%{share_dir}/makeseg
%{share_dir}/styles
%{share_dir}/texinputs
%{share_dir}/versions
%{_bindir}/*
%{_texmfmaindir}/tex/latex/html
%{_mandir}/man1/latex2html*

%files pngicons
%dir %{share_dir}
%dir %{share_dir}/icons
%{share_dir}/icons/*.png

%files doc
%doc docs/manual
%doc tests
%doc example

%changelog
