#
# spec file for package python-Keras-Preprocessing
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
Name:           python-Keras-Preprocessing%{psuffix}
Version:        1.1.0
Release:        0
Summary:        Data preprocessing and augmentation package for deep learning models
License:        MIT
URL:            https://github.com/keras-team/keras-preprocessing
Source0:        https://files.pythonhosted.org/packages/source/K/Keras_Preprocessing/Keras_Preprocessing-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.9.1
Requires:       python-six >= 1.9.0
# It won't work without it but we don't want a build loop in OBS
Recommends:     python-Keras
# match up with tensorflow
ExcludeArch:    %{ix86}
%if %{with test}
BuildRequires:  %{python_module Keras}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module numpy >= 1.9.1}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.9.0}
%endif
%python_subpackages

%description
Keras Preprocessing is the data preprocessing and data augmentation
module of the Keras deep learning library. It provides utilities for
working with image data, text data, and sequence data.

%prep
%setup -q -n Keras_Preprocessing-%{version}
# do not add extra opts for pytest
rm setup.cfg

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest -k 'not test_doc'
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
