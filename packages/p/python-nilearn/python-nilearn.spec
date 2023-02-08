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


%define         skip_python2 1
Name:           python-nilearn
Version:        0.10.0
Release:        0
Summary:        Statistical learning tool for neuroimaging
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/nilearn/nilearn
Source:         https://github.com/nilearn/nilearn/archive/%{version}.tar.gz#/nilearn-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-joblib >= 0.15
Requires:       python-matplotlib >= 3.0
Requires:       python-nibabel >= 3.0
Requires:       python-numpy >= 1.18
Requires:       python-requests >= 2
Requires:       python-scikit-learn >= 0.22
Requires:       python-scipy >= 1.5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module joblib >= 0.15}
BuildRequires:  %{python_module matplotlib >= 3.0}
BuildRequires:  %{python_module nibabel >= 3.0}
BuildRequires:  %{python_module numpy >= 1.18}
BuildRequires:  %{python_module pandas >= 1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2}
BuildRequires:  %{python_module scikit-learn >= 0.22}
BuildRequires:  %{python_module scipy >= 1.5}
# /SECTION
%python_subpackages

%description
Nilearn is a Python module for statistical learning on
NeuroImaging data.

%prep
%setup -n nilearn-%{version}
sed -i '/durations/d' setup.cfg
chmod -x nilearn/datasets/tests/data/localizer_index.json
sed -i '1{/env python/d}' nilearn/glm/tests/test_utils.py nilearn/plotting/glass_brain_files/plot_align_svg.py

%build
%python_build

%install
%python_install
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
