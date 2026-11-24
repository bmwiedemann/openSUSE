#
# spec file for package python-sphinx-llm-friendly
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-sphinx-llm-friendly
Version:        0.7.0
Release:        0
Summary:        Sphinx extension to make documentation LLM-friendly
License:        MIT
URL:            https://github.com/scrapy/sphinx-llm-friendly
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-llm-friendly/sphinx_llm_friendly-%{version}.tar.gz
BuildRequires:  %{python_module hatchling >= 1.27.0}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module Sphinx >= 7.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinx-design}
BuildRequires:  %{python_module sphinxcontrib-httpdomain}
BuildRequires:  %{python_module sphinxcontrib-youtube}
BuildRequires:  %{python_module tabulate}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Sphinx >= 7.4
Requires:       python-docutils
Requires:       python-tabulate
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Sphinx extension that makes documentation LLM-friendly:
-   A Markdown version of every page, next to its HTML version.
-   llms.txt, with a link to the Markdown version of every page.
-   HTML pages point to their Markdown version with a <link
    rel="alternate" type="text/markdown"> tag, and get a button to copy
    their Markdown version.

%prep
%autosetup -p1 -n sphinx_llm_friendly-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/sphinx-llm-friendly
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative sphinx-llm-friendly

%postun
%python_uninstall_alternative sphinx-llm-friendly

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/sphinx-llm-friendly
%{python_sitelib}/sphinx_llm_friendly
%{python_sitelib}/sphinx_llm_friendly-%{version}.dist-info

%changelog
