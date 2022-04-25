#
# spec file for package python-myst-parser
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-myst-parser
Version:        0.17.2
Release:        0
Summary:        An extended commonmark compliant parser, with bridges to docutils & sphinx
License:        MIT
URL:            https://myst-parser.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/m/myst-parser/myst-parser-%{version}.tar.gz
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
MyST is a flavor of markdown that is designed for simplicity, flexibility, and extensibility.
This is the reference implementation of MyST Markdown, as well as a collection of tools to support working with MyST in Python and Sphinx.
It contains an extended CommonMark (https://commonmark.org)-compliant parser using markdown-it-py (https://markdown-it-py.readthedocs.io/), as well as a Sphinx (https://www.sphinx-doc.org) extension that allows to write MyST Markdown in Sphinx.

%prep
%setup -q -n myst-parser-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/myst-anchors
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-html
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-html5
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-latex
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-pseudoxml
%python_clone -a %{buildroot}%{_bindir}/myst-docutils-xml
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%{python_install_alternative myst-anchors myst-docutils-html myst-docutils-html5 myst-docutils-latex myst-docutils-pseudoxml myst-docutils-xml}

%postun
%python_uninstall_alternative myst-anchors

%files %{python_files}
%{python_sitelib}/myst_parser/
%{python_sitelib}/myst_parser-%{version}*-info
%license LICENSE
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/myst-anchors
%python_alternative %{_bindir}/myst-docutils-html
%python_alternative %{_bindir}/myst-docutils-html5
%python_alternative %{_bindir}/myst-docutils-latex
%python_alternative %{_bindir}/myst-docutils-pseudoxml
%python_alternative %{_bindir}/myst-docutils-xml

%changelog
