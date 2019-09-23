#
# spec file for package python-jupyter_client
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
Name:           python-jupyter_client
Version:        5.3.1
Release:        0
Summary:        Jupyter protocol implementation and client libraries
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter_client
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_client/jupyter_client-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyter_client = %{version}
Requires:       python-entrypoints
Requires:       python-jupyter_core
Requires:       python-python-dateutil >= 2.1
Requires:       python-pyzmq >= 13
Requires:       python-tornado >= 4.1
Requires:       python-traitlets
BuildArch:      noarch
%python_subpackages

%description
This package contains the reference implementation of the Jupyter protocol.
It also provides client and kernel management APIs for working with kernels.

It also provides the jupyter kernelspec entrypoint for installing kernelspecs
for use with Jupyter frontends.

This package provides the python interface.

%package     -n jupyter-jupyter_client
Summary:        Jupyter protocol implementation and client libraries
Group:          Development/Languages/Python
Requires:       python3-jupyter_client = %{version}

%description -n jupyter-jupyter_client
This package contains the reference implementation of the Jupyter protocol.
It also provides client and kernel management APIs for working with kernels.

It also provides the jupyter kernelspec entrypoint for installing kernelspecs
for use with Jupyter frontends.

This package provides the jupyter components.

%prep
%setup -q -n jupyter_client-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING.md
%{python_sitelib}/jupyter_client-%{version}-py*.egg-info
%{python_sitelib}/jupyter_client/

%files -n jupyter-jupyter_client
%license COPYING.md
%doc CONTRIBUTING.md README.md
%{_bindir}/jupyter-kernel
%{_bindir}/jupyter-kernelspec
%{_bindir}/jupyter-run

%changelog
