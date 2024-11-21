#
# spec file for package python-swapper
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


%{?sle15_python_module_pythons}
Name:           python-swapper
Version:        1.4.0
Release:        0
Summary:        The unofficial Django swappable models API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wq/django-swappable-models
Source:         https://files.pythonhosted.org/packages/source/s/swapper/swapper-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.0
BuildArch:      noarch
%python_subpackages

%description
Swapper is an unofficial API for the undocumented but very
powerful Django feature: swappable models. Swapper facilitates
implementing arbitrary swappable models in your own reusable apps.

%prep
%setup -q -n swapper-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# can't use %%pyunittest: the SLE/Leap targets in d:l:p:django have old python-rpm-macros
%python_exec -m unittest -v tests.test_swapper

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/swapper
%{python_sitelib}/swapper-%{version}.dist-info

%changelog
