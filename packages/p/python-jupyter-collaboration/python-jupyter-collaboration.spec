#
# spec file for package python-jupyter-collaboration
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-jupyter-collaboration
Version:        4.1.0
Release:        0
Summary:        Jupyter Server Extension Providing Support for Y Documents
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyter_collaboration
Source:         https://github.com/jupyterlab/jupyter-collaboration/archive/refs/tags/v%{version}.tar.gz#/jupyter_collaboration-%{version}-gh.tar.gz
Source99:       python-jupyter-collaboration.rpmlintrc
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling >= 1.4}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-jupyter-collaboration-ui >= 2.1.0 with python-jupyter-collaboration-ui < 3)
Requires:       (python-jupyter-docprovider >= 2.1.0 with python-jupyter-docprovider < 3)
Requires:       (python-jupyter-server-ydoc >= 2.1.0 with python-jupyter-server-ydoc < 3)
Requires:       (python-jupyterlab >= 4.4.0 with python-jupyterlab < 5)
Provides:       python-jupyter_collaboration = %{version}-%{release}
Obsoletes:      python-jupyterlab-rtc < 1
BuildArch:      noarch
BuildRequires:  %{python_module jupyter-collaboration-ui >= 2.1.0 with %python-jupyter-collaboration-ui < 3}
BuildRequires:  %{python_module jupyter-docprovider >= 2.1.0 with %python-jupyter-docprovider < 3}
BuildRequires:  %{python_module jupyter-server-ydoc-test >= 2.1.0 with %python-jupyter-server-ydoc-test < 3}
BuildRequires:  %{python_module jupyterlab > 4.4.0 with %python-jupyterlab < 5}
BuildRequires:  %{python_module pytest}
%python_subpackages

%description
Jupyter Collaboration is a Jupyter server extension providing Support for Y Documents.

This is a meta-package for:
- jupyter-collaboration-ui
- jupyter-docprovider
- jupyter-server-ydoc

%prep
%setup -q -n jupyter-collaboration-%{version}
sed -i 's/--color=yes//' pyproject.toml

%build
# Do not install the monorepo but the metapackage
pushd projects/jupyter-collaboration
%pyproject_wheel
popd

%install
pushd projects/jupyter-collaboration
%pyproject_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test the whole stack
%pytest -p no:unraisableexception

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/jupyter_collaboration
%{python_sitelib}/jupyter_collaboration-%{version}.dist-info

%changelog
