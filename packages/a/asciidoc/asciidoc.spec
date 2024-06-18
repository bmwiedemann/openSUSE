#
# spec file for package asciidoc
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


%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" != ""
%define name_suffix -%{flavor}
%endif

Name:           asciidoc%{?name_suffix}
Version:        10.2.0
Release:        0
Summary:        Text-Based Document Generation
License:        GPL-2.0-or-later
URL:            https://asciidoc-py.github.io/
Source0:        https://github.com/asciidoc-py/asciidoc-py/releases/download/%{version}/asciidoc-%{version}.tar.gz
Patch0:         asciidoc.version.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock >= 3.3
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
Requires:       docbook-xsl-stylesheets
Requires:       python3-xml
# a2x needs /usr/bin/xsltproc
Recommends:     libxslt
BuildArch:      noarch
%if "%{flavor}" == "latextest"
BuildRequires:  asciidoc-latex-backend
%endif

%description
AsciiDoc is a text document format for writing short documents,
articles, books, and UNIX man pages. AsciiDoc files can be translated
to HTML and DocBook markups using the asciidoc command.

%package examples
Summary:        Examples and Documents for asciidoc

%description examples
This package contains examples and documents of asciidoc.

%package latex-backend
Summary:        Provide latex backend dependencies
Requires:       %{name} = %{version}
Requires:       dblatex
Supplements:    (%{name} and dblatex)
# some of them are actually required by dblatex, but it's easier to keep them all in here
Requires:       texlive-metafont-bin
Requires:       tex(8r.enc)
Requires:       tex(fancybox.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(pcrr8c.tfm)
Requires:       tex(phvr8t.tfm)
Requires:       tex(ptmr8t.tfm)
Requires:       tex(ptmri7t.tfm)
Requires:       tex(rsfs10.tfm)
Requires:       tex(upquote.sty)
Requires:       tex(zptmcm7v.tfm)
Requires:       tex(zptmcm7y.tfm)

%description latex-backend
AsciiDoc can generate pdf from asciidoc format through dblatex. For that it needs quite some
latex dependencies that we don't want to have by default. So this package is optional.

%prep
%setup -q -n asciidoc-%{version}
# do not use env
# Remove python shebang from sitelib files, this will remove the
# automatic dependency on /usr/bin/python3
find asciidoc -name \*.py -exec sed -i -e '/\/usr\/bin\/env/d' {} \;

%if "%{flavor}" == "latextest"
%build
a2x --verbose --xsltproc-opts --nonet --attribute=badges --attribute=external_title -a toc -a numbered --attribute=pdf_format --format=pdf -a docinfo1 doc/a2x.1.txt

%else

%build
%python3_build

%install
%python3_install
mkdir -p %{buildroot}%{_mandir}/man1/
cp -a doc/*.1 %{buildroot}%{_mandir}/man1/

%fdupes %{buildroot}%{python3_sitelib}/%{name}

%check
export PYTHONPATH="$PYTHONPATH:%{buildroot}%{python3_sitelib}"
export PYTHONDONTWRITEBYTECODE=1
python3 -m asciidoc.asciidoc --doctest
python3 -m pytest --ignore=_build.python3 -v
python3 tests/testasciidoc.py run

%files
%license COPYRIGHT LICENSE
%doc README.md BUGS.adoc CHANGELOG.adoc
%{python3_sitelib}/asciidoc
%{python3_sitelib}/asciidoc-%{version}*
%{_bindir}/%{name}
%{_bindir}/a2x
%{_mandir}/man1/*

%files examples
%doc doc

%files latex-backend
%license COPYRIGHT

%endif

%changelog
