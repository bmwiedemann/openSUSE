#
# spec file for package latex2html
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


%define share_dir %{_datadir}/latex2html
Name:           latex2html
Version:        2019.2
Release:        0
Summary:        LaTeX to HTML Converter
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Utilities
Url:            http://www.ctan.org/tex-archive/support/latex2html
Source0:        https://github.com/latex2html/latex2html/archive/v%{version}.tar.gz
Source1:        latex2html-manual.tar.bz2
Patch0:         latex2html-share-dir.diff
Patch1:         latex2html-perl-bindir.diff
Patch2:         latex2html-dest-dir.diff
Patch3:         latex2html-binmode.diff
Patch4:         latex2html-backref-workaround.diff
BuildRequires:  fdupes
BuildRequires:  ghostscript-fonts-std
BuildRequires:  ghostscript-x11
BuildRequires:  netpbm
BuildRequires:  texlive-dvips
BuildRequires:  texlive-kpathsea
BuildRequires:  texlive-latex
BuildRequires:  texlive-preview
Requires:       ghostscript_any
Requires:       latex2html-pngicons
Requires:       netpbm
Requires:       perl
Requires:       texlive-dvips
Requires:       texlive-latex
BuildArch:      noarch
%define _texmfmaindir   %{_datadir}/texmf

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
%setup -q -a 1
%patch0
%patch1
%patch2
%patch3
%patch4

%build
# Not autotools based configure
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 latex2html.1 %{buildroot}/%{_mandir}/man1
rm -r %{buildroot}%{share_dir}/{docs,example,dot.latex2html-init}
chmod 755 %{buildroot}%{_datadir}/%{name}/{cweb2html/makemake.pl,cweb2html/cweb2html,makemap,makeseg/makeseg}
%fdupes -s %{buildroot}

%check
make %{?_smp_mflags} test

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
%doc manual
%doc tests
%doc example

%changelog
