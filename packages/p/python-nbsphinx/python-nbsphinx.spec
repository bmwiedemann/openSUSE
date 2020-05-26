#
# spec file for package python-nbsphinx
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
%define         skip_python2 1
Name:           python-nbsphinx
Version:        0.6.1
Release:        0
Summary:        Jupyter Notebook Tools for Sphinx
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spatialaudio/nbsphinx/
Source:         https://files.pythonhosted.org/packages/source/n/nbsphinx/nbsphinx-%{version}.tar.gz
BuildRequires:  %{python_module Send2Trash}
BuildRequires:  %{python_module Sphinx >= 1.3.2}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-Send2Trash
Requires:       python-Sphinx >= 1.3.2
Requires:       python-docutils
Requires:       python-nbconvert
Requires:       python-nbformat
Requires:       python-sphinx_rtd_theme
Recommends:     mathjax
Recommends:     pandoc
Provides:       python-jupyter_nbsphinx = %{version}
Obsoletes:      python-jupyter_nbsphinx < %{version}
BuildArch:      noarch
%ifpython3
Provides:       jupyter-nbsphinx = %{version}
%endif
%python_subpackages

%description
The nbsphinx package is a Sphinx extension that provides a source
parser for *.ipynb files. Custom Sphinx directives are used to show
Jupyter Notebook code cells (and of course their results) in both HTML
and LaTeX output. Un-evaluated notebooks – i.e. notebooks without
stored output cells – will be automatically executed during the Sphinx
build process.

%prep
%setup -q -n nbsphinx-%{version}

%build
%python_build

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python_sitelib}}

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/nbsphinx.py*
%pycache_only %{python_sitelib}/__pycache__/nbsphinx.*.py*
%{python_sitelib}/nbsphinx-%{version}-py*.egg-info

%changelog
