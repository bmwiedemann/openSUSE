#
# spec file for package python-nilearn
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-nilearn
Version:        0.10.1
Release:        0
Summary:        Statistical learning tool for neuroimaging
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/nilearn/nilearn
Source:         https://files.pythonhosted.org/packages/source/n/nilearn/nilearn-%{version}.tar.gz
# PATCH-FIX-UPSTREAM numpy-1.25.patch gh#nilearn/nilearn#3746
Patch0:         numpy-1.25.patch
# PATCH-FIX-UPSTREAM warning-based-sklearn-version.patch gh#nilearn/nilearn#3763
Patch1:         warning-based-sklearn-version.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-joblib >= 1.0.0
Requires:       python-matplotlib >= 3.3.0
Requires:       python-nibabel >= 3.2.0
Requires:       python-numpy >= 1.19
Requires:       python-packaging
Requires:       python-pandas >= 1.1.5
Requires:       python-requests >= 2
Requires:       python-scikit-learn >= 1.0.0
Requires:       python-scipy >= 1.6.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module joblib >= 1.0.0}
BuildRequires:  %{python_module matplotlib >= 3.3.0}
BuildRequires:  %{python_module nibabel >= 3.2.0}
BuildRequires:  %{python_module numpy >= 1.19}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas >= 1.1.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2}
BuildRequires:  %{python_module scikit-learn >= 1.0.0}
BuildRequires:  %{python_module scipy >= 1.6.0}
# /SECTION
%python_subpackages

%description
Nilearn is a Python module for statistical learning on
NeuroImaging data.

%prep
%autosetup -p1 -n nilearn-%{version}
chmod -x nilearn/datasets/tests/data/localizer_index.json
sed -i '1{/env python/d}' nilearn/glm/tests/test_utils.py nilearn/plotting/glass_brain_files/plot_align_svg.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Test try to build the doc and run examples...
rm -rf doc/ examples/
# sporadic race condition in pytest-xdist
donttest="test_with_globbing_patterns_with_single_subject"
# sporadic unknown failure (on all architectures): https://github.com/nilearn/nilearn/issues/2607
donttest+=" or test_check_niimg_wildcard"
# https://github.com/nilearn/nilearn/issues/2608
donttest+=" or test_clean_confounds"
# https://github.com/nilearn/nilearn/issues/2610
donttest+=" or test_reorder_img_mirror"
# ppc64 https://github.com/nilearn/nilearn/issues/3363
donttest+=" or (test_load_confounds and test_nilearn_standardize)"
# x86_64 https://github.com/nilearn/nilearn/issues/3382
donttest+=" or test_tfce_smoke"
donttest+=" or test_load_uniform_ball_cloud"

if [[ $(getconf LONG_BIT) -eq 64 ]]; then
    # this is a noarch rpm package but the pure python code is only intended for 64-bit architectures
%pytest -k "not ($donttest)"
fi

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/nilearn
%{python_sitelib}/nilearn-%{version}*-info

%changelog
