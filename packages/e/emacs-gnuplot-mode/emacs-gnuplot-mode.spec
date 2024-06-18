#
# spec file for package emacs-gnuplot-mode
#
# Copyright (c) 2024 SUSE LLC
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


%define _sitedir %{_datadir}/emacs/site-lisp

Name:           emacs-gnuplot-mode
Version:        0.8.0
Release:        0
Summary:        Gnuplot mode for EMACS
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            https://github.com/bruceravel/gnuplot-mode/tree/master
Source:         https://github.com/bruceravel/gnuplot-mode/archive/%{version}.tar.gz#/gnuplot-mode-%{version}.tar.gz
BuildRequires:  emacs-nox
BuildRequires:  texlive-latex
BuildRequires:  tex(fancybox.sty)
Requires:       emacs
Requires:       gnuplot
# Split-alias tag, gnuplot-mode was part of the gnuplot package
Provides:       gnuplot:%{_sitedir}/gnuplot.el
BuildArch:      noarch

%description
Gnuplot-mode is a major Emacs mode for editing Gnuplot source code. It
provides syntax highlighting, automatic indentation and context sensitive
command completion.

%package doc
Summary:        Documentation for EMACS Gnuplot mode

%description doc
This package contains the Gnuplot mode documentation in PDF format.

%prep
%setup -q -n gnuplot-%{version}

%build
make -f Makefile default
pdflatex gpelcard.tex

%install
install -pm 755 -d %{buildroot}%{_sitedir}
install -pm 644 gnuplot*.el %{buildroot}%{_sitedir}/
install -pm 644 gnuplot*.elc %{buildroot}%{_sitedir}/

%files
%license LICENSE
%doc README.org
%dir %{_sitedir}
%{_sitedir}/gnuplot*el
%{_sitedir}/gnuplot*elc

%files doc
%doc gpelcard.pdf

%changelog
