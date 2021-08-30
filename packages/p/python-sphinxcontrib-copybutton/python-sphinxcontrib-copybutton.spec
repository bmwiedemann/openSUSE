#
# spec file for package python-sphinxcontrib-copybutton
#
# Copyright (c) 2021 SUSE LLC
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
%global skip_python2 1
%global skip_python36 1
Name:           python-sphinxcontrib-copybutton
Version:        0.4.0
Release:        0
Summary:        Sphinx extension to add a "copy" button to code blocks
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/executablebooks/sphinx-copybutton
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-copybutton/sphinx-copybutton-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinx-book-theme}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 0.6
BuildArch:      noarch
%python_subpackages

%description
Sphinx extension for adding a "copy" button to code blocks.

%prep
%setup -q -n sphinx-copybutton-%{version}

%build
%python_build
%{python_expand export PYTHONPATH=build/lib
sphinx-build -n -b html docs/ docs/_build
rm -r docs/_build/.{buildinfo,doctrees}
}

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mv -v docs/_build documentation/
%fdupes documentation/

%files %{python_files}
%doc README.md documentation
%license LICENSE
%{python_sitelib}/sphinx_copybutton*

%changelog
