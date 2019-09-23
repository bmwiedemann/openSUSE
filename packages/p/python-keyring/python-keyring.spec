#
# spec file for package python-keyring
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
Name:           python-keyring
Version:        18.0.1
Release:        0
Summary:        System keyring service access from Python
License:        Python-2.0 AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/keyring
Source:         https://files.pythonhosted.org/packages/source/k/keyring/keyring-%{version}.tar.gz
BuildRequires:  %{python_module SecretStorage}
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module setuptools >= 17.1}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SecretStorage
Requires:       python-entrypoints
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
The Python keyring lib provides a way to access the system keyring service
from python. It can be used in any application that needs safe password storage.

%prep
%setup -q -n keyring-%{version}
# For rpmlint warning: remove shebang from python library:
sed -i '/^#!/d' keyring/cli.py
sed -i -e 's,--flake8,,' pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# sadly most tests need running dbus to communicate with secretstorage/etc
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix} --ignore=_build.python2 --ignore=_build.python3
}

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE
%python3_only %{_bindir}/keyring
%{python_sitelib}/keyring-%{version}-py*.egg-info
%{python_sitelib}/keyring/

%changelog
