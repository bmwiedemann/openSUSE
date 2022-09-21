#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-keyring%{psuffix}
Version:        23.9.3
Release:        0
Summary:        System keyring service access from Python
License:        MIT AND Python-2.0
URL:            https://github.com/jaraco/keyring
Source:         https://files.pythonhosted.org/packages/source/k/keyring/keyring-%{version}.tar.gz
Patch0:         support-new-importlib.patch
BuildRequires:  %{python_module setuptools >= 17.1}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SecretStorage >= 3
Requires:       python-entrypoints
Requires:       python-importlib-metadata
Requires:       python-jaraco.classes
Requires:       python-jeepney >= 0.4.2
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module SecretStorage >= 3}
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module jaraco.classes}
BuildRequires:  %{python_module keyring = %{version}}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module toml}
%endif
%python_subpackages

%description
The Python keyring lib provides a way to access the system keyring service
from python. It can be used in any application that needs safe password storage.

%prep
%autosetup -p1 -n keyring-%{version}
echo "import setuptools; setuptools.setup()" > setup.py

%if 0%{?sle_version}
# keyring is not setting the egg version correctly without this:
sed -i -e '1a version=%{version}' setup.cfg
%endif
# For rpmlint warning: remove shebang from python library:
sed -i '/^#!/d' keyring/cli.py
sed -i -e 's,--flake8,,' -e 's,--black,,' -e 's,--cov,,' pytest.ini

%build
%python_build

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/keyring
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%post
%python_install_alternative keyring

%postun
%python_uninstall_alternative keyring

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE
%python_alternative %{_bindir}/keyring
%{python_sitelib}/keyring-%{version}-py*.egg-info
%{python_sitelib}/keyring/
%endif

%changelog
