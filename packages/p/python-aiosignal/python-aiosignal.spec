#
# spec file for package python-aiosignal
#
# Copyright (c) 2025 SUSE LLC
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
%{?sle15_python_module_pythons}
Name:           python-aiosignal
Version:        1.3.2
Release:        0
Summary:        a list of registered asynchronous callbacks
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiosignal
Source:         https://files.pythonhosted.org/packages/source/a/aiosignal/aiosignal-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-frozenlist >= 1.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module frozenlist >= 1.1.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A project to manage callbacks in asyncio projects.
Signal is a list of registered asynchronous callbacks.

%prep
%setup -q -n aiosignal-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/aiosignal
%{python_sitelib}/aiosignal-%{version}*-info

%changelog
