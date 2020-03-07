#
# spec file for package python-Keras-Applications
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-Keras-Applications%{psuffix}
Version:        1.0.8
Release:        0
Summary:        Reference implementations of deep learning models
License:        MIT
URL:            https://github.com/keras-team/keras-applications
Source0:        https://files.pythonhosted.org/packages/source/K/Keras_Applications/Keras_Applications-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-h5py
Requires:       python-numpy >= 1.9.1
# It won't work without it but we don't want a build loop in OBS
Recommends:     python-Keras
# match up with tensorflow
ExcludeArch:    %{ix86}
%if %{with test}
BuildRequires:  %{python_module Keras}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module numpy >= 1.9.1}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Keras Applications is the applications module of the Keras deep
learning library. It provides model definitions and pre-trained
weights for a number of archictures, such as VGG16, ResNet50,
Xception, MobileNet, and more.

%prep
%setup -q -n Keras_Applications-%{version}
# these fetch tensorflow data from aws sadly
rm tests/applications_test.py

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# test_decode_predictions - online test (fetches from google cloud)
%pytest -k 'not test_decode_predictions'
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
