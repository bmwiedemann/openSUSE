#
# spec file for package python-nbsmoke
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
Name:           python-nbsmoke
Version:        0.2.8
Release:        0
Summary:        Basic notebook checks
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pyviz/nbsmoke
Source:         https://files.pythonhosted.org/packages/source/n/nbsmoke/nbsmoke-%{version}.tar.gz
Source99:       python-nbsmoke-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4
Requires:       python-ipykernel
Requires:       python-jupyter_client
Requires:       python-nbconvert
Requires:       python-nbformat
Requires:       python-pyflakes
Requires:       python-pytest >= 3.1.1
Requires:       python-requests
Provides:       python-jupyter_nbsmoke = %{version}
Obsoletes:      python-jupyter_nbsmoke < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module pyflakes}
BuildRequires:  %{python_module pytest >= 3.1.1}
BuildRequires:  %{python_module requests}
# /SECTION
%ifpython3
Provides:       jupyter-nbsmoke = %{version}
%endif
%python_subpackages

%description
Basic notebook smoke tests for checking whether the notebooks run,
and whether they contain lint.

WARNING: early stage proof of concept; work in progress. Use at your
own risk.

In particular, this extension is supposed to handle ipython magics as
far as possible, but has not yet been widely tested.

%prep
%setup -q -n nbsmoke-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python -c "import nbsmoke"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/nbsmoke-%{version}-py*.egg-info
%{python_sitelib}/nbsmoke/

%changelog
