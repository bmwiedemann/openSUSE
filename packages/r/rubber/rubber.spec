#
# spec file for package rubber
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


%define pythons python3
Name:           rubber
Version:        1.6.7
Release:        0
Summary:        An automated system for building LaTeX documents
License:        GPL-2.0-only
URL:            https://gitlab.com/latex-rubber/rubber
Source:         https://gitlab.com/latex-rubber/rubber/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  makeinfo
BuildRequires:  perl-Parse-RecDescent
BuildRequires:  texinfo
BuildRequires:  texlive-biber
BuildRequires:  texlive-bibtex8
BuildRequires:  texlive-cweb
BuildRequires:  texlive-dvipdfmx
BuildRequires:  texlive-dvips
BuildRequires:  tex(asymptote.sty)
BuildRequires:  tex(beamer.cls)
BuildRequires:  tex(bibtopic.sty)
BuildRequires:  tex(glossaries.sty)
BuildRequires:  tex(moreverb.sty)
BuildRequires:  tex(multibib.sty)
BuildRequires:  tex(nomencl.sty)
Requires:       texlive-latex
Requires(post): info
BuildArch:      noarch

%description
Rubber is a building system for LaTeX documents. It is based on a routine that
runs just as many compilations as necessary. The module system provides a
great flexibility that virtually allows support for any package with no user
intervention, as well as pre- and post-processing of the document. The
standard modules currently provide support for bibtex, dvips, dvipdfm, pdftex,
makeindex. A good number of standard packages are supported, including
graphics/graphicx (with automatic conversion between various formats and
Metapost compilation).

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}/usr/share/doc/%{name}/%{name}.* %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}/usr/share/doc/%{name}
cp doc/%{name}/%{name}.info %{buildroot}%{_infodir}
gzip %{buildroot}%{_infodir}/%{name}.info
%fdupes %{buildroot}%{python3_sitelib}/rubber/

%check
pushd tests
# Disable tests that fail due to missing files or unwieldy deps
for dir in combine cweb-latex fig2dev-dvi fig2dev-path-inplace fig2dev-path \
    fig2dev-path-into hooks-input-file graphicx-dotted-files knitr metapost \
    metapost-input metapost-error pstricks-pd pythontex; do
    touch $dir/disable
done
./run.sh *
popd

%post
install-info %{_infodir}/rubber.info.gz %{_infodir}/dir

%postun
install-info --delete %{_infodir}/rubber.info.gz %{_infodir}/dir

%files
%doc NEWS README.md
%license COPYING
%{_bindir}/rubber
%{_bindir}/rubber-pipe
%{_bindir}/rubber-info
%{_bindir}/rubber-lsmod
%{python3_sitelib}/rubber/
%{python3_sitelib}/latex_rubber-%{version}.dist-info
%{_mandir}/man1/rubber-info.1%{?ext_man}
%{_mandir}/man1/rubber-pipe.1%{?ext_man}
%{_mandir}/man1/rubber.1%{?ext_man}
%{_infodir}/rubber.info%{?ext_info}
%{_mandir}/fr/man1/*.gz
%{_docdir}/%{name}/
%{_datadir}/zsh

%changelog
