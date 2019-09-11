#
# spec file for package python-selenium
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
Name:           python-selenium
Version:        3.141.0
Release:        0
Summary:        Python bindings for Selenium
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/SeleniumHQ/selenium
Source:         https://files.pythonhosted.org/packages/source/s/selenium/selenium-%{version}.tar.gz
#https://github.com/SeleniumHQ/selenium/issues/6246
Source1:        selenium-pytest.tar.bz2
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rdflib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-rdflib
Requires:       python-urllib3
ExclusiveArch:  %{ix86} x86_64
%python_subpackages

%description
Selenium Python Client Driver is a Python language binding for Selenium Remote
Control (version 1.0 and 2.0).

Currently, the remote protocol, Firefox and Chrome for Selenium 2.0 are
supported, as well as the Selenium 1.0 bindings.

%prep
%setup -q -n selenium-%{version} -a1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Avoid 64bit runtime dependencies on 32bit architectures:
%ifarch %{ix86}
%python_expand rm %{buildroot}%{$python_sitelib}/selenium/webdriver/firefox/amd64/x_ignore_nofocus.so
%endif

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_version} test/unit

%files %{python_files}
%doc README.rst CHANGES
%license LICENSE
%{python_sitelib}/selenium*

%changelog
