#
# spec file for package python-asv_runner
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
Name:           python-asv-runner
Version:        0.2.1
Release:        0
Summary:        Core Python benchmark code for ASV
License:        BSD-3-Clause
URL:            https://asv.readthedocs.io/projects/asv-runner/en/latest/
Source:         https://files.pythonhosted.org/packages/source/a/asv_runner/asv_runner-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module importlib-metadata}
# /SECTION
BuildRequires:  fdupes
Requires:       python-importlib-metadata
BuildArch:      noarch
%python_subpackages

%description
Core Python benchmark code for asv.

This package shall not have any dependencies on external packages and
must be compatible with all Python versions greater than or equal to
3.7. For other functionality, refer to the asv package or consider
writing an extension.

%prep
%autosetup -p1 -n asv_runner-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/asv_runner
%{python_sitelib}/asv_runner-%{version}.dist-info

%changelog
