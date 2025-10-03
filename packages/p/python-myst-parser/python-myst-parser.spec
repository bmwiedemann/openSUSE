#
# spec file for package python-myst-parser
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-myst-parser
Version:        4.0.1
Release:        0
Summary:        An extended commonmark compliant parser, with bridges to docutils & sphinx
License:        MIT
URL:            https://myst-parser.readthedocs.io/
Source:         https://github.com/executablebooks/MyST-Parser/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PyPI tarball does not contain tests
#Source:         https://files.pythonhosted.org/packages/source/m/myst-parser/myst-parser-%%{version}.tar.gz
# PATCH-FIX-OPENSUSE Regenerate failing files with --regen-file-failure
Patch0:         support-docutils-0.22.patch
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module docutils >= 0.18 with %python-docutils < 0.23}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module linkify-it-py}
BuildRequires:  %{python_module markdown-it-py}
BuildRequires:  %{python_module mdit-py-plugins}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-PyYAML
Requires:       python-Sphinx
Requires:       python-docutils >= 0.18
Requires:       python-markdown-it-py
Requires:       python-mdit-py-plugins
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION tests
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest-param-files}
BuildRequires:  %{python_module pytest-regressions}
BuildRequires:  %{python_module pytest}
# /SECTION
# SECTION docs
#BuildRequires:  python3-Sphinx
#BuildRequires:  python3-Jinja2
#BuildRequires:  python3-PyYAML
#BuildRequires:  python3-Sphinx >= 3.1
#BuildRequires:  python3-docutils >= 0.15
#BuildRequires:  python3-markdown-it-py >= 1
#BuildRequires:  python3-mdit-py-plugins < 0.4
# /SECTION
%python_subpackages

%description
MyST is a flavor of markdown that is designed for simplicity, flexibility, and extensibility.
This is the reference implementation of MyST Markdown, as well as a collection of tools to support working with MyST in Python and Sphinx.
It contains an extended CommonMark (https://commonmark.org)-compliant parser using markdown-it-py (https://markdown-it-py.readthedocs.io/), as well as a Sphinx (https://www.sphinx-doc.org) extension that allows to write MyST Markdown in Sphinx.

%prep
%autosetup -p1 -n MyST-Parser-%{version}
rm docs/.gitignore

%build
%pyproject_wheel
# docs require unavailable sphinxcontrib-bibtex
#pushd docs
#PYTHONPATH=.. make html
#rm _build/html/.buildinfo
#popd

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/myst-anchors
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-html
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-html5
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-latex
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-pseudoxml
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-xml
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-demo
%python_clone -a %{buildroot}%{_bindir}/myst-inv
%python_group_libalternatives myst-anchors myst-docutils-html myst-docutils-html5 myst-docutils-latex myst-docutils-pseudoxml myst-docutils-xml myst-docutils-demo myst-inv
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no python-sphinx-pytest package
ignore="--ignore=tests/test_renderers/test_fixtures_sphinx.py"
ignore+=" --ignore=tests/test_renderers/test_myst_refs.py"
ignore+=" --ignore=tests/test_sphinx/test_sphinx_builds.py"
%pytest $ignore

%pre
%python_libalternatives_reset_alternative myst-anchors

%post
%python_install_alternative myst-anchors myst-docutils-html myst-docutils-html5 myst-docutils-latex myst-docutils-pseudoxml myst-docutils-xml myst-docutils-demo myst-inv

%postun
%python_uninstall_alternative myst-anchors

%files %{python_files}
%{python_sitelib}/myst_parser/
%{python_sitelib}/myst_parser-%{version}.dist-info
%license LICENSE
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/myst-anchors
%python_alternative %{_bindir}/myst-docutils-html
%python_alternative %{_bindir}/myst-docutils-html5
%python_alternative %{_bindir}/myst-docutils-latex
%python_alternative %{_bindir}/myst-docutils-pseudoxml
%python_alternative %{_bindir}/myst-docutils-xml
%python_alternative %{_bindir}/myst-docutils-demo
%python_alternative %{_bindir}/myst-inv
%doc docs

%changelog
