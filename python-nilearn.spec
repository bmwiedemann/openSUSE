#
# spec file for package python-nilearn
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-nilearn
Version:        0.6.0
Release:        0
License:        BSD-3-Clause
Summary:        Statistical learning tool for neuroimaging
Url:            http://nilearn.github.io
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/n/nilearn/nilearn-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module matplotlib >= 2.0}
BuildRequires:  %{python_module nibabel >= 2.0.2}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-learn >= 0.19}
BuildRequires:  %{python_module scipy >= 0.19}
# /SECTION
Requires:       python-joblib
Requires:       python-matplotlib >= 2.0
Requires:       python-nibabel >= 2.0.2
Requires:       python-scikit-learn >= 0.19
Requires:       python-scipy >= 0.19
BuildArch:      noarch

%python_subpackages

%description
Nilearn is a Python module for statistical learning on
NeuroImaging data.

%prep
%setup -q -n nilearn-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Disable tests that require a network connection
%pytest -v -k 'not test_fetch_ and not test_get_batch and not test_scroll_server_results and not test_simple_download and not test_fill_html_template and not test_temp_file_removing and not test_view_img_on_surf and not test_view_surf and not test_resample_img_segmentation_fault'

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
