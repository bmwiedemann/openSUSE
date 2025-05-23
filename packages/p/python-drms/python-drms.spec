#
# spec file for package python-drms
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


%{?sle15_python_module_pythons}
Name:           python-drms
Version:        0.8.0
Release:        0
Summary:        Tool to access HMI, AIA and MDI data with Python
License:        MIT
URL:            https://github.com/sunpy/drms
Source:         https://files.pythonhosted.org/packages/source/d/drms/drms-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-pandas
Requires(postun): update-alternatives
Requires(post): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
The drms module provides an interface for accessing HMI, AIA and MDI
data with Python. It uses the publicly accessible JSOC DRMS server by
default, but can also be used with local NetDRMS sites.

%prep
%setup -q -n drms-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/drms
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative drms

%postun
%python_uninstall_alternative drms

%files %{python_files}
%doc CITATION.rst README.rst
%license LICENSE.rst
%python_alternative %{_bindir}/drms
%{python_sitelib}/drms
%{python_sitelib}/drms-%{version}.dist-info

%changelog
