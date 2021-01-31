#
# spec file for package python-nilearn
#
# Copyright (c) 2021 SUSE LLC
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
%define         skip_python2 1
# SciPy 1.6.0 dropped support for Python 3.6
%define         skip_python36 1
Name:           python-nilearn
Version:        0.7.0
Release:        0
Summary:        Statistical learning tool for neuroimaging
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/nilearn/nilearn
Source:         https://github.com/nilearn/nilearn/archive/%{version}.tar.gz#/nilearn-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - https://github.com/nilearn/nilearn/pull/2606
Patch1:         nilearn-fix-aarch64.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-joblib >= 0.12
Requires:       python-matplotlib >= 2.0
Requires:       python-nibabel >= 2.0.2
Requires:       python-numpy >= 1.11
Requires:       python-requests
Requires:       python-scikit-learn >= 0.19
Requires:       python-scipy >= 0.19
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module joblib >= 0.12}
BuildRequires:  %{python_module matplotlib >= 2.0}
BuildRequires:  %{python_module nibabel >= 2.0.2}
BuildRequires:  %{python_module numpy >= 1.11}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-learn >= 0.19}
BuildRequires:  %{python_module scipy >= 0.19}
# /SECTION
%python_subpackages

%description
Nilearn is a Python module for statistical learning on
NeuroImaging data.

%prep
%setup -q -n nilearn-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Test try to build the doc and run examples...
rm -rf doc/ examples/
# Disable tests that require a network connection
# Disable tests requiring to be executed without xdist (serialization issue): test_tikhonov_regularization_vs_graph_net or test_connectivity_measure_outputs or test_canica_square_img or test_with_globbing_patterns_with_single_subject or test_dict_learning
# Disable tests failing with new numpy (conversions to float fail): test_plot_surf_stat_map test_plot_surf_roi
# https://github.com/nilearn/nilearn/issues/2608 - test_clean_confounds
# https://github.com/nilearn/nilearn/issues/2610 - test_reorder_img_mirror
%pytest -n auto -k 'not (test_fetch_ or test_get_batch or test_scroll_server_results or test_simple_download or test_fill_html_template or test_temp_file_removing or test_view_img_on_surf or test_view_surf or test_resample_img_segmentation_fault or test_tikhonov_regularization_vs_graph_net or test_connectivity_measure_outputs or test_canica_square_img or test_with_globbing_patterns_with_single_subject or test_dict_learning or test_plot_surf_stat_map or test_plot_surf_roi or test_clean_confounds or test_reorder_img_mirror)'

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/nilearn
%{python_sitelib}/nilearn-%{version}*-info

%changelog
