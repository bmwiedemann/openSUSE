#
# spec file for package python-Keras-Preprocessing
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-Keras-Preprocessing
Version:        1.0.5
Release:        0
Summary:        Data preprocessing and augmentation package for deep learning models
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/keras-team/keras-preprocessing
Source0:        https://files.pythonhosted.org/packages/source/K/Keras_Preprocessing/Keras_Preprocessing-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/keras-team/keras-preprocessing/%{version}/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.9.1
Requires:       python-six >= 1.9.0
Recommends:     python-scipy >= 0.14
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.9.1}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.9.0}
# /SECTION
%python_subpackages

%description
Keras Preprocessing is the data preprocessing and data augmentation
module of the Keras deep learning library. It provides utilities for
working with image data, text data, and sequence data.

%prep
%setup -q -n Keras_Preprocessing-%{version}
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
