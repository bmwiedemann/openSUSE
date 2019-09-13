#
# spec file for package python-Keras-Applications
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
Name:           python-Keras-Applications
Version:        1.0.6
Release:        0
Summary:        Reference implementations of deep learning models
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/keras-team/keras-applications
Source0:        https://files.pythonhosted.org/packages/source/K/Keras_Applications/Keras_Applications-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/keras-team/keras-applications/%{version}/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-h5py
Requires:       python-numpy >= 1.9.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module numpy >= 1.9.1}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Keras Applications is the applications module of the Keras deep
learning library. It provides model definitions and pre-trained
weights for a number of archictures, such as VGG16, ResNet50,
Xception, MobileNet, and more.

%prep
%setup -q -n Keras_Applications-%{version}
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
