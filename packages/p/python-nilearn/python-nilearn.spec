#
# spec file for package python-nilearn
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


# Run tests in parallel with pytest-xdist. On by default.
%bcond_without pytest_xdist
Name:           python-nilearn
Version:        0.11.1
Release:        0
Summary:        Statistical learning tool for neuroimaging
License:        BSD-3-Clause
URL:            https://github.com/nilearn/nilearn
Source:         https://files.pythonhosted.org/packages/source/n/nilearn/nilearn-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/nilearn/nilearn/pull/5044 [FIX] updates to fix some tests failures with sklearn 1.6.1
Patch:          sklearn-1.16.1.patch
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-joblib >= 1.2.0
Requires:       python-lxml
Requires:       python-nibabel >= 5.2.0
Requires:       python-numpy >= 1.22.4
Requires:       python-packaging
Requires:       python-pandas >= 2.2.0
Requires:       python-requests >= 2.25.0
Requires:       python-scikit-learn >= 1.4.0
Requires:       python-scipy >= 1.8.0
Recommends:     python-matplotlib >= 3.3
Recommends:     python-plotly
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module joblib >= 1.2.0}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module nibabel >= 5.2.0}
BuildRequires:  %{python_module numpy >= 1.22.4}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas >= 2.2.0}
%{?with_pytest_xdist:BuildRequires:  %{python_module pytest-xdist}}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.25.0}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module scikit-learn >= 1.4.0}
BuildRequires:  %{python_module scipy >= 1.8.0}
# /SECTION
%python_subpackages

%description
Nilearn is a Python module for statistical learning on
NeuroImaging data.

%prep
%autosetup -p1 -n nilearn-%{version}
chmod -x nilearn/datasets/tests/data/localizer_index.json nilearn/plotting/glass_brain_files/plot_align_svg.py
sed -i '1{/env python/d}' nilearn/glm/tests/test_utils.py nilearn/plotting/glass_brain_files/plot_align_svg.py
chmod +x nilearn/externals/install_tempita.sh

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Test try to build the doc and run examples...
rm -rf doc/ examples/
# https://github.com/nilearn/nilearn/issues/2608
donttest="test_clean_confounds"
# ppc64 https://github.com/nilearn/nilearn/issues/3363 https://github.com/nilearn/nilearn/issues/3232
donttest+=" or (test_load_confounds and test_nilearn_standardize)"
# x86_64 https://github.com/nilearn/nilearn/issues/3382, last tested 2024-02-21 with nilearn 0.10.3, still failing
donttest+=" or test_tfce_smoke"
donttest+=" or test_load_uniform_ball_cloud"
# flaky test
donttest+=" or test_resample_img_segmentation_fault"

# unresolvable documentation package requirement docstring_parser
ignorefiles="--ignore maint_tools/check_glossary_term.py"
# ignore cache files too
ignorefiles+=" --ignore nilearn_cache"

# we have our own pytest preffered markers
sed -i '/addopts.*$/d' pyproject.toml

if [[ $(getconf LONG_BIT) -eq 64 ]]; then
# this is a noarch rpm package but the pure python code is only intended for 64-bit architectures
%pytest %{?with_pytest_xdist:-n auto} -s -k "not ($donttest)" $ignorefiles && rm -r nilearn_cache
fi

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/nilearn
%{python_sitelib}/nilearn-%{version}.dist-info

%changelog
