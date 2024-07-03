#
# spec file for package python-Sphinx
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-Sphinx%{psuffix}
Version:        7.3.7
Release:        0
Summary:        Python documentation generator
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://www.sphinx-doc.org
Source:         https://files.pythonhosted.org/packages/source/s/sphinx/sphinx-%{version}.tar.gz
# Provide intersphinx inventory offline, run update-intersphinx.sh
# https://docs.python.org/3/objects.inv
Source2:        python3.inv
# https://requests.readthedocs.io/en/stable/objects.inv
Source3:        requests.inv
# https://docs.readthedocs.io/en/stable/objects.inv
Source4:        readthedocs.inv
Source5:        update-intersphinx.sh
Source99:       python-Sphinx.keyring
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
# workaround for suboptimal CentOS-7 project config
#!BuildIgnore:  texinfo
Requires:       python-Babel >= 1.3
Requires:       python-Jinja2 >= 2.3
Requires:       python-Pygments >= 2.14
Requires:       python-alabaster >= 0.7
Requires:       python-defusedxml >= 0.7.1
Requires:       python-docutils >= 0.12
Requires:       python-imagesize
Requires:       python-packaging
Requires:       python-requests >= 2.5.0
Requires:       python-snowballstemmer >= 1.1
Requires:       python-sphinx_rtd_theme
Requires:       python-sphinxcontrib-applehelp
Requires:       python-sphinxcontrib-devhelp
Requires:       python-sphinxcontrib-htmlhelp >= 2.0.0
Requires:       python-sphinxcontrib-jsmath
Requires:       python-sphinxcontrib-qthelp >= 1.0.2
Requires:       python-sphinxcontrib-serializinghtml >= 1.1.9
Requires:       python-sphinxcontrib-websupport
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-SQLAlchemy >= 0.9
Recommends:     python-Sphinx-doc-man
Recommends:     python-Whoosh >= 2.0
BuildArch:      noarch
%if 0%{?python_version_nodots} < 310
Requires:       python-importlib-metadata >= 4.4
%endif
%if %{with test}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Sphinx = %{version}}
BuildRequires:  %{python_module Sphinx-latex = %{version}}
BuildRequires:  %{python_module defusedxml >= 0.7.1}
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-websupport}
BuildRequires:  %{python_module testsuite}
BuildRequires:  ImageMagick
BuildRequires:  graphviz
# For PNG format
BuildRequires:  graphviz-gd
# For PDF format (!?)
BuildRequires:  graphviz-gnome
BuildRequires:  texlive-tex-gyre
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
Requires:       tex(tgtermes.sty)
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

%if 0%{?suse_version} > 1500
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
Obsoletes:      python-Sphinx-doc-man-common <= %{version}

%description -n python-Sphinx-doc-man
Sphinx is a tool that facilitates creating documentation for Python
projects (or other documents consisting of multiple reStructuredText
sources).

This package contains the manual pages for the Sphinx executables.

%package -n python-Sphinx-doc-html
Summary:        HTML Documentation for python-Sphinx
Group:          Documentation/HTML
Provides:       python-Sphinx-doc-html = %{version}

%description -n python-Sphinx-doc-html
Sphinx is a tool that facilitates creating documentation for Python
projects (or other documents consisting of multiple reStructuredText
sources).

This package contains the HTML documentation for Sphinx.
%endif

%prep
%setup -q -n sphinx-%{version}
%autopatch -p1

%build
%pyproject_wheel

%if %{with test}
mkdir build.doc

cp %{SOURCE2} doc/python3.inv
cp %{SOURCE3} doc/requests.inv
cp %{SOURCE4} doc/readthedocs.inv
%{python_expand # Use one bundled intersphinx inventory for all flavors.
# The python3.6 inventory fails to build even in its own flavor.
# Use a more recent default (currently 3.9) from the source tag instead.
# The same for requests.
sed -i -e "s/\((.https:..docs.python.org.3.., \)None\()\)/\1'python3.inv'\2/g" doc/conf.py
sed -i -e "s/\((.https:..requests.readthedocs.io.*, \)None\()\)/\1'requests.inv'\2/g" doc/conf.py
sed -i -e "s/\((.https:..docs.readthedocs.io.*, \)None\()\)/\1'readthedocs.inv'\2/g" doc/conf.py
# rm build/sphinx/html/.buildinfo
$python -m sphinx -b man -j auto ./doc ./build.doc/man
$python -m sphinx -b html -j auto ./doc ./build.doc/html
}
%endif

%install
%if ! %{with test}
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/sphinx-apidoc
%python_clone -a %{buildroot}%{_bindir}/sphinx-autogen
%python_clone -a %{buildroot}%{_bindir}/sphinx-build
%python_clone -a %{buildroot}%{_bindir}/sphinx-quickstart

%python_expand mkdir -p %{buildroot}%{$python_sitelib}/sphinxcontrib
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# gh#openSUSE/python-rpm-macros#74
%{!?python_find_lang: %define python_find_lang() \
%find_lang %{**} \
langfile=%{?2}%{!?2:%1.lang} \
%{python_expand # \
grep -v 'python.*site-packages' ${langfile} > %{$python_prefix}-${langfile} \
grep -F %{$python_sitelib} ${langfile} >> %{$python_prefix}-${langfile} \
} \
}
%python_find_lang sphinx

%else
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_docdir}/python-Sphinx/
mv build.doc/html %{buildroot}%{_docdir}/python-Sphinx/
rm -rf %{buildroot}%{_docdir}/python-Sphinx/html/_images

mkdir -p %{buildroot}%{_mandir}/man1
mv build.doc/man/sphinx-all.1 %{buildroot}%{_mandir}/man1/sphinx-all.1
mv build.doc/man/sphinx-apidoc.1 %{buildroot}%{_mandir}/man1/sphinx-apidoc.1
mv build.doc/man/sphinx-build.1 %{buildroot}%{_mandir}/man1/sphinx-build.1
mv build.doc/man/sphinx-quickstart.1 %{buildroot}%{_mandir}/man1/sphinx-quickstart.1
%endif
%endif

# Always deduplicate
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if ! %{with test}
%post
%python_install_alternative sphinx-apidoc sphinx-autogen sphinx-build sphinx-quickstart
:

%postun
%python_uninstall_alternative sphinx-apidoc
%endif

%check
%if %{with test}
export PYTHONPATH=.
export LC_ALL="C.utf8"
# test_latex_images test downloading a remote image
# test_signature_annotations doesn’t work
%pytest tests -k 'not (linkcheck or test_latex_images or test_signature_annotations or test_copy_images or test_ext_imgconverter)'
%endif

%if ! %{with test}
%files %{python_files} -f %{python_prefix}-sphinx.lang
%license LICENSE.rst
%doc CHANGES.rst README.rst
%python_alternative %{_bindir}/sphinx-apidoc
%python_alternative %{_bindir}/sphinx-autogen
%python_alternative %{_bindir}/sphinx-build
%python_alternative %{_bindir}/sphinx-quickstart
%{python_sitelib}/sphinx/
%exclude %{python_sitelib}/sphinx/texinputs/
%dir %{python_sitelib}/sphinx-%{version}.dist-info
%{python_sitelib}/sphinx-%{version}.dist-info/*
%dir %{python_sitelib}/sphinxcontrib

%files %{python_files latex}
%license LICENSE.rst
%{python_sitelib}/sphinx/texinputs/
%endif

%if %{with test}
%if 0%{?suse_version} > 1500
%files -n python-Sphinx-doc-man
%license LICENSE.rst
%{_mandir}/man1/sphinx-all.1%{?ext_man}
%{_mandir}/man1/sphinx-apidoc.1%{?ext_man}
%{_mandir}/man1/sphinx-build.1%{?ext_man}
%{_mandir}/man1/sphinx-quickstart.1%{?ext_man}

%files -n python-Sphinx-doc-html
%license LICENSE.rst
%dir %{_docdir}/python-Sphinx/
%{_docdir}/python-Sphinx/html/
%endif
%endif

%changelog
