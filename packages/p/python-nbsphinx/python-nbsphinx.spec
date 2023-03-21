#
# spec file for package python-nbsphinx
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-nbsphinx
Version:        0.9.1
Release:        0
Summary:        Jupyter Notebook Tools for Sphinx
License:        MIT
URL:            https://github.com/spatialaudio/nbsphinx/
Source:         https://files.pythonhosted.org/packages/source/n/nbsphinx/nbsphinx-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Sphinx >= 1.8}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinx_rtd_theme}
BuildRequires:  %{python_module traitlets >= 5}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-Sphinx >= 1.8
Requires:       python-docutils
Requires:       python-nbconvert
Requires:       python-nbformat
Requires:       python-sphinx_rtd_theme
Requires:       python-traitlets >= 5
Recommends:     mathjax
Recommends:     pandoc
Provides:       python-jupyter_nbsphinx = %{version}
Obsoletes:      python-jupyter_nbsphinx < %{version}
BuildArch:      noarch
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
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
%pyproject_wheel

%install
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # no other unit tests provided
# import the module.
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import nbsphinx'
# We cannot test it on our own doc/ because we lack the right Sphinx packages
#$python -m sphinx doc/ _build/ -Dsuppress_warnings=git.too_shallow -b html
}

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/nbsphinx
%{python_sitelib}/nbsphinx-%{version}.dist-info

%changelog
