#
# spec file for package python-dask-image
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-dask-image
Version:        2025.11.0
Release:        0
Summary:        Distributed image processing
License:        BSD-3-Clause
URL:            https://image.dask.org
Source:         https://files.pythonhosted.org/packages/source/d/dask-image/dask_image-%{version}.tar.gz
Patch0:         support-numpy-2.4.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module setuptools_scm >= 8}
# SECTION test requirements
BuildRequires:  %{python_module dask-complete >= 2024.4.1}
BuildRequires:  %{python_module numpy >= 1.18}
BuildRequires:  %{python_module pandas >= 2.0.0}
BuildRequires:  %{python_module pims >= 0.4.1}
BuildRequires:  %{python_module scipy >= 1.7.0}
BuildRequires:  %{python_module tifffile >= 2018.10.18}
BuildRequires:  %{python_module coverage >= 7.2.1}
BuildRequires:  %{python_module flake8 >= 6.0.0}
BuildRequires:  %{python_module pytest >= 7.2.2}
BuildRequires:  %{python_module pytest-cov >= 4.0.0}
BuildRequires:  %{python_module pytest-flake8 >= 1.1.1}
BuildRequires:  %{python_module pytest-timeout >= 2.3.1}
# /SECTION
BuildRequires:  fdupes
Requires:       python-dask-complete >= 2024.4.1
Requires:       python-numpy >= 1.18
Requires:       python-pandas >= 2.0.0
Requires:       python-pims >= 0.4.1
Requires:       python-scipy >= 1.7.0
Requires:       python-tifffile >= 2018.10.18
Suggests:       python-cupy >= 9.0.0
BuildArch:      noarch
%python_subpackages

%description
Distributed image processing

%prep
%autosetup -p1 -n dask_image-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Remove docs and continuous_integration
%python_expand rm -r %{buildroot}%{$python_sitelib}/docs
%python_expand rm -r %{buildroot}%{$python_sitelib}/continuous_integration
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not (test_generic_filter_identity or test_generic_filter_comprehensions)'

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/dask_image
%{python_sitelib}/dask_image-%{version}.dist-info

%changelog
