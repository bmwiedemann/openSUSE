#
# spec file for package python-selenium
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
Name:           python-selenium
Version:        4.25.0
Release:        0
Summary:        Python bindings for Selenium
License:        Apache-2.0
URL:            https://github.com/SeleniumHQ/selenium
Source:         https://files.pythonhosted.org/packages/source/s/selenium/selenium-%{version}.tar.gz
# https://github.com/SeleniumHQ/selenium/issues/6246
Source1:        selenium-pytest.tar.bz2
Source2:        vendor.tar.xz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module certifi >= 2021.10.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rdflib}
BuildRequires:  %{python_module setuptools-rust}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions >= 4.9}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module websocket-client >= 1.8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi >= 2021.10.8
Requires:       python-trio >= 0.17
Requires:       python-trio-websocket >= 0.9
Requires:       python-typing-extensions >= 4.9
Requires:       python-urllib3
Requires:       python-websocket-client >= 1.8
ExclusiveArch:  %{ix86} x86_64 %arm aarch64 riscv64
%python_subpackages

%description
Selenium Python Client Driver is a Python language binding for Selenium Remote
Control (version 1.0 and 2.0).

Currently, the remote protocol, Firefox and Chrome for Selenium 2.0 are
supported, as well as the Selenium 1.0 bindings.

%prep
%setup -q -n selenium-%{version} -a1 -a2

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch test/unit

%files %{python_files}
%doc README.rst CHANGES
%license LICENSE
%{python_sitearch}/selenium
%{python_sitearch}/selenium-%{version}.dist-info

%changelog
