#
# spec file for package python-remoto
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
Name:           python-remoto
Version:        1.1.4
Release:        0
Summary:        Remote command executor using ssh and Python in the remote end
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/alfredodeza/remoto
Source0:        https://files.pythonhosted.org/packages/source/r/remoto/remoto-%{version}.tar.gz
BuildRequires:  %{python_module execnet}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
Requires:       python-execnet
Requires:       python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# SECTION build requirements
BuildRequires:  %{python_module mock >= 1.0b1}
BuildRequires:  %{python_module pytest >= 2.1.3}
# /SECTION
%python_subpackages

%description
Remote command executor using ssh and Python in the remote end. This
package is primarily built to support the ceph-deploy project.
python-remoto is built upon python-execnet which manages the
connections and processes.

%prep
%setup -q -n remoto-%{version}

%build
export REMOTO_NO_VENDOR=no
%python_build

%install
export REMOTO_NO_VENDOR=no
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
