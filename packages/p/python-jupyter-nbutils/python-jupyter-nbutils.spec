#
# spec file for package python-jupyter-nbutils
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-jupyter-nbutils
Version:        0.1.3
Release:        0
License:        MIT
Summary:        A collection of Jupyter notebook tools and utilities
Url:            https://github.com/CermakM/jupyter-nbutils
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/j/jupyter-nbutils/jupyter-nbutils-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-daiquiri
Requires:       python-ipykernel
Requires:       python-ipython
Recommends:     python-jupyter-require >= 0.2.0
BuildArch:      noarch

%python_subpackages

%description
Tools and utilities to improve your experience with Jupyter Notebooks.

%prep
%setup -q -n jupyter-nbutils-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
