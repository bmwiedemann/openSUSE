#
# spec file for package python-pytest-toolbox
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


%define skip_python2 1
Name:           python-pytest-toolbox
Version:        0.4
Release:        0
Summary:        Numerous plugins for pytest
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/samuelcolvin/pytest-toolbox
Source:         https://github.com/samuelcolvin/pytest-toolbox/archive/v%{version}.tar.gz#/pytest-toolbox-%{version}.tar.gz
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-py
Requires:       python-pytest >= 3.5
Recommends:     python-pydantic
BuildArch:      noarch
%python_subpackages

%description
Numerous useful plugins for pytest.

%prep
%setup -q -n pytest-toolbox-%{version}
sed -i '/addopts/d;/timeout/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst HISTORY.rst
%license LICENSE
%{python_sitelib}/pytest_toolbox
%{python_sitelib}/pytest_toolbox-%{version}*-info

%changelog
