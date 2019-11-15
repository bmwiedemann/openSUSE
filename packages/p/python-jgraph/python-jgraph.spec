#
# spec file for package python-jgraph
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%bcond_without test
Name:           python-jgraph
Version:        0.2.1
Release:        0
Summary:        An embeddable webGL graph visualization library
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/patrickfuller/jgraph/
Source:         https://files.pythonhosted.org/packages/source/j/jgraph/jgraph-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ipython
Requires:       python-notebook
Provides:       python-jupyter_jgraph = %{version}
Obsoletes:      python-jupyter_jgraph <= %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module ipython}
%endif
%ifpython3
Provides:       jupyter-jgraph = %{version}
%endif
%python_subpackages

%description
An embeddable webGL graph visualization library.
With this, jgraph can be used with Jupyter notebooks.

%prep
%setup -q -n jgraph-%{version}
sed -i -e '/^#!\//, 1d' python/json_formatter.py
chmod a-x LICENSE.txt
cp -r python jgraph
cp -r js jgraph/js

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/jgraph/
%{python_sitelib}/jgraph-%{version}-py*.egg-info

%changelog
