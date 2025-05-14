#
# spec file
#
# Copyright (c) 2025 Dr. Axel Braun <DocB@opensuse.org>
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

%define modname pyorthanc
Name:           python-%{modname}
Version:        1.20.0
Release:        0
Summary:        A comprehensive Python client for Orthanc
License:        MIT
URL:            https://github.com/gacou54/pyorthanc
Source0:        https://files.pythonhosted.org/packages/source/p/pyorthanc/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

Requires:        python-pydicom
Requires:        python-httpx

%python_subpackages

%description
PyOrthanc is a comprehensive Python client for Orthanc, providing:

- Complete wrapping of the Orthanc REST API methods
- High-level utilities for common DICOM operations
- Asynchronous client support
- Helper functions for working with DICOM data
- Integration with the Orthanc Python plugin

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/pyorthanc*
%{python_sitelib}/pyorthanc-%{version}.*-info

%changelog
