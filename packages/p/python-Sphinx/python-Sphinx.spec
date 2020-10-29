#
# spec file for package python-Sphinx
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-Sphinx%{psuffix}
Version:        3.2.1
Release:        0
Summary:        Python documentation generator
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://sphinx-doc.org
Source:         https://files.pythonhosted.org/packages/source/S/Sphinx/Sphinx-%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/S/Sphinx/Sphinx-%{version}.tar.gz.asc
Source2:        python3.inv
Source99:       python-Sphinx-rpmlintrc
# PATCH-FIX-UPSTREAM: https://patch-diff.githubusercontent.com/raw/sphinx-doc/sphinx/pull/8205.patch
Patch0:         sphinx-pygments-compat.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# workaround for suboptimal CentOS-7 project config
#!BuildIgnore:  texinfo
Requires:       python-Babel >= 1.3
Requires:       python-Jinja2 >= 2.3
Requires:       python-Pygments >= 2.1
Requires:       python-alabaster >= 0.7
Requires:       python-docutils >= 0.12
Requires:       python-imagesize
Requires:       python-requests >= 2.5.0
Requires:       python-setuptools
Requires:       python-snowballstemmer >= 1.1
Requires:       python-sphinx_rtd_theme
Requires:       python-sphinxcontrib-applehelp
Requires:       python-sphinxcontrib-devhelp
Requires:       python-sphinxcontrib-htmlhelp
Requires:       python-sphinxcontrib-jsmath
Requires:       python-sphinxcontrib-qthelp
Requires:       python-sphinxcontrib-serializinghtml
Requires:       python-sphinxcontrib-websupport
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-SQLAlchemy >= 0.9
Recommends:     python-Sphinx-doc-man
Recommends:     python-Whoosh >= 2.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Sphinx = %{version}}
BuildRequires:  %{python_module Sphinx-latex = %{version}}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-websupport}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module typed-ast}
BuildRequires:  ImageMagick
%endif
%python_subpackages

%description
Sphinx is a tool that facilitates creating documentation for Python
projects (or other documents consisting of multiple reStructuredText
sources). It was originally created for the Python documentation, and
supports Python project documentation well, but C/C++ is likewise
supported.

Sphinx uses reStructuredText as its markup language. Sphinx draws from
the parsing and translating suite, the Docutils.

%package latex
Summary:        Sphinx packages for LaTeX
Group:          Productivity/Publishing/TeX/Base
Requires:       python-Sphinx = %{version}
Requires:       texlive-dvipng
Requires:       texlive-gnu-freefont
Requires:       texlive-latex
Requires:       texlive-latexmk
Requires:       texlive-makeindex
Requires:       texlive-metafont
Requires:       texlive-pdftex
Requires:       tex(8r.enc)
Requires:       tex(alltt.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(atbegshi.sty)
Requires:       tex(babel.sty)
Requires:       tex(bm.sty)
Requires:       tex(capt-of.sty)
Requires:       tex(cmap.sty)
Requires:       tex(color.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(dvipdfmx.def)
Requires:       tex(english.ldf)
Requires:       tex(eqparbox.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(float.sty)
Requires:       tex(fncychap.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(footnote.sty)
Requires:       tex(framed.sty)
Requires:       tex(graphics.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hypcap.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(longtable.sty)
Requires:       tex(luatex85.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(multirow.sty)
Requires:       tex(needspace.sty)
Requires:       tex(newfloat.sty)
Requires:       tex(palatino.sty)
Requires:       tex(parskip.sty)
Requires:       tex(pcrr.tfm)
Requires:       tex(pdftex.def)
Requires:       tex(pdftex.map)
Requires:       tex(phvr.tfm)
Requires:       tex(polyglossia.sty)
Requires:       tex(pplr.tfm)
Requires:       tex(preview.sty)
Requires:       tex(ptmr.tfm)
Requires:       tex(pzcmi.tfm)
Requires:       tex(tabulary.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(threeparttable.sty)
Requires:       tex(times.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(upquote.sty)
Requires:       tex(utf8.def)
Requires:       tex(utf8x.def)
Requires:       tex(varwidth.sty)
Requires:       tex(wrapfig.sty)

%description    latex
Sphinx is a tool that facilitates creating documentation for Python
projects (or other documents consisting of multiple reStructuredText
sources).

This package contains the LaTeX components for python-Sphinx.

%package -n python-Sphinx-doc
Summary:        Man files for python-Sphinx
Group:          Documentation/Other
Requires:       python3-Sphinx = %{version}

%description -n python-Sphinx-doc
Sphinx is a tool that facilitates creating documentation for Python
projects (or other documents consisting of multiple reStructuredText
sources). It was originally created for the Python documentation, and
supports Python project documentation well, but C/C++ is likewise
supported.

Sphinx uses reStructuredText as its markup language. Sphinx draws from
the parsing and translating suite, the Docutils.

This package contains the documentation for Sphinx.

%package -n python-Sphinx-doc-man
Summary:        Man files for python-Sphinx
Group:          Documentation/Man
Requires:       python3-Sphinx = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Supplements:    python3-Sphinx
Obsoletes:      %{python_module Sphinx-doc-man-common <= %{version}}

%description -n python-Sphinx-doc-man
Sphinx is a tool that facilitates creating documentation for Python
projects (or other documents consisting of multiple reStructuredText
sources).

This package contains the manual pages for the Sphinx executables.

%package -n python-Sphinx-doc-html
Summary:        HTML Documentation for python-Sphinx
Group:          Documentation/HTML
Provides:       %{python_module Sphinx-doc-html = %{version}}

%description -n python-Sphinx-doc-html
Sphinx is a tool that facilitates creating documentation for Python
projects (or other documents consisting of multiple reStructuredText
sources).

This package contains the HTML documentation for Sphinx.

%prep
%setup -q -n Sphinx-%{version}
%autopatch -p1

sed -i 's/\r$//' sphinx/themes/basic/static/jquery.js # Fix wrong end-of-line encoding

%build
%python_build

%if %{with test}
mkdir build.doc

# get its intersphinx_inventroy from python3-doc
# instead of via network from https://docs.python.org/3/objects.inv
cp %{SOURCE2} doc/python3.inv
%python_expand sed -i -e "s/\(intersphinx_mapping = ..python.: (.https:..docs.python.org.3.., \)None\()}\)/\1'%{$python_prefix}.inv'\2/g" doc/conf.py
%python_exec setup.py build_sphinx && rm build/sphinx/html/.buildinfo
%python_exec setup.py build_sphinx -b man

mv build/sphinx/{html,man} build.doc/
%endif

%install
%if ! %{with test}
%python_install

%python_clone -a %{buildroot}%{_bindir}/sphinx-apidoc
%python_clone -a %{buildroot}%{_bindir}/sphinx-autogen
%python_clone -a %{buildroot}%{_bindir}/sphinx-build
%python_clone -a %{buildroot}%{_bindir}/sphinx-quickstart

%python_expand mkdir -p %{buildroot}%{$python_sitelib}/sphinxcontrib
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%find_lang sphinx

%else
mkdir -p %{buildroot}%{_docdir}/python-Sphinx/
mv build.doc/html %{buildroot}%{_docdir}/python-Sphinx/

mkdir -p %{buildroot}%{_mandir}/man1
mv build.doc/man/sphinx-all.1 %{buildroot}%{_mandir}/man1/sphinx-all.1
mv build.doc/man/sphinx-apidoc.1 %{buildroot}%{_mandir}/man1/sphinx-apidoc.1
mv build.doc/man/sphinx-build.1 %{buildroot}%{_mandir}/man1/sphinx-build.1
mv build.doc/man/sphinx-quickstart.1 %{buildroot}%{_mandir}/man1/sphinx-quickstart.1
%endif

# Always deduplicate
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if ! %{with test}
%post
%{python_install_alternative sphinx-apidoc sphinx-autogen sphinx-build sphinx-quickstart}

%postun
%python_uninstall_alternative sphinx-apidoc
%endif

%check
%if %{with test}
export LC_ALL="C.utf8"
%pytest tests -k 'not (linkcheck or test_latex_images)'
%endif

%if ! %{with test}
%files %{python_files} -f sphinx.lang
%license LICENSE
%doc AUTHORS CHANGES README.rst
%python_alternative %{_bindir}/sphinx-apidoc
%python_alternative %{_bindir}/sphinx-autogen
%python_alternative %{_bindir}/sphinx-build
%python_alternative %{_bindir}/sphinx-quickstart
%{python_sitelib}/sphinx/
%exclude %{python_sitelib}/sphinx/texinputs/
%{python_sitelib}/Sphinx-%{version}-py*.egg-info
%dir %{python_sitelib}/sphinxcontrib

%files %{python_files latex}
%license LICENSE
%doc AUTHORS
%{python_sitelib}/sphinx/texinputs/
%endif

%if %{with test}
%files -n python-Sphinx-doc-man
%license LICENSE
%doc AUTHORS
%{_mandir}/man1/sphinx-all.1%{?ext_man}
%{_mandir}/man1/sphinx-apidoc.1%{?ext_man}
%{_mandir}/man1/sphinx-build.1%{?ext_man}
%{_mandir}/man1/sphinx-quickstart.1%{?ext_man}

%files -n python-Sphinx-doc-html
%license LICENSE
%doc AUTHORS
%dir %{_docdir}/python-Sphinx/
%{_docdir}/python-Sphinx/html/
%endif

%changelog
