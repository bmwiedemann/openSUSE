#
# spec file for package python-keyring
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-keyring%{psuffix}
Version:        25.7.0
Release:        0
Summary:        System keyring service access from Python
License:        MIT
URL:            https://github.com/jaraco/keyring
Source:         https://files.pythonhosted.org/packages/source/k/keyring/keyring-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SecretStorage >= 3.2
Requires:       python-jaraco.classes
Requires:       python-jaraco.context
Requires:       python-jaraco.functools
Requires:       python-jeepney >= 0.4.2
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if 0%{python_version_nodots} < 310
Requires:       python-importlib-resources
%endif
%if 0%{python_version_nodots} < 312
Requires:       python-importlib-metadata >= 4.11.4
%endif
%if %{with test}
BuildRequires:  %{python_module keyring = %{version}}
BuildRequires:  %{python_module pyfakefs}
BuildRequires:  %{python_module pytest >= 3.5}
%endif
%python_subpackages

%description
The Python keyring lib provides a way to access the system keyring service
from python. It can be used in any application that needs safe password storage.

%prep
%autosetup -p1 -n keyring-%{version}

# For rpmlint warning: remove shebang from python library:
sed -i '/^#!/d' keyring/cli.py

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
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

%pre
%python_libalternatives_reset_alternative keyring

%files %{python_files}
%doc README.rst NEWS.rst
%license LICENSE
%python_alternative %{_bindir}/keyring
%{python_sitelib}/keyring-%{version}*-info
%{python_sitelib}/keyring/
%endif

%changelog
