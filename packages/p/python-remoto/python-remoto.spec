#
# spec file for package python-remoto
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-remoto
Version:        1.2.1
Release:        0
Summary:        Remote command executor using ssh and Python in the remote end
License:        MIT
URL:            https://github.com/alfredodeza/remoto
Source0:        https://files.pythonhosted.org/packages/source/r/remoto/remoto-%{version}.tar.gz
# https://github.com/alfredodeza/remoto/commit/aa74f65bb59dc46998e72e4bdcd070287e4e2af6
Patch0:         python-remoto-no-mock.patch
# PATCH-FIX-UPSTREAM gh#alfredodeza/remoto#69
Patch1:         support-pytest-8.patch
BuildRequires:  %{python_module execnet}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-execnet
BuildArch:      noarch
# SECTION build requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Remote command executor using ssh and Python in the remote end. This
package is primarily built to support the ceph-deploy project.
python-remoto is built upon python-execnet which manages the
connections and processes.

%prep
%autosetup -p1 -n remoto-%{version}

%build
export REMOTO_NO_VENDOR=no
%pyproject_wheel

%install
export REMOTO_NO_VENDOR=no
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/remoto
%{python_sitelib}/remoto-%{version}.dist-info

%changelog
