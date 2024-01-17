#
# spec file for package hevea
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 Aaron Puchert.
# Copyright (c) 2017 Peter Trommler.
# Copyright (c) 2008 Gernot Hillier.
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


Name:           hevea
Version:        2.36
Release:        0
Summary:        A fast LaTeX to HTML translator
License:        LGPL-2.0-only AND QPL-1.0
Group:          Productivity/Publishing/HTML/Tools
URL:            https://hevea.inria.fr/
Source0:        https://hevea.inria.fr/distri/%{name}-%{version}.tar.gz
Source1:        https://hevea.inria.fr/distri/%{name}-%{version}-manual.tar.gz
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml(ocaml.opt) >= 4.08

%description
HEVEA is a LaTeX to HTML translator.  The input language is a fairly
complete subset of LaTeX2e (old LaTeX style is also accepted) and
the output language is HTML.

%prep
%setup -q
%setup -q -a 1

%build
make %{?_smp_mflags} LIBDIR=%{_datadir}/%{name}

%install
# Remove configuration
rm config.sh
%make_install \
    PREFIX=%{_prefix} \
    LIBDIR=%{_datadir}/%{name} \
    LATEXLIBDIR=%{_datadir}/texmf/tex/latex

%files
%license LICENSE
%doc CHANGES README
%doc %{name}-%{version}-manual/*
%{_bindir}/bibhva
%{_bindir}/esponja
%{_bindir}/hacha
%{_bindir}/hevea
%{_bindir}/imagen
%{_datadir}/%{name}
%dir %{_datadir}/texmf
%dir %{_datadir}/texmf/tex
%dir %{_datadir}/texmf/tex/latex
%{_datadir}/texmf/tex/latex/%{name}.sty
%{_datadir}/texmf/tex/latex/mathjax.sty

%changelog
