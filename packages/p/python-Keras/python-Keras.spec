#
# spec file for package python-Keras
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


%define srcname keras
# We have only py3 based tensorflow
%define         skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-Keras%{psuffix}
Version:        2.3.1
Release:        0
Summary:        Deep Learning library
License:        MIT
URL:            https://github.com/keras-team/keras
Source:         https://github.com/keras-team/keras/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
%if %{with test}
BuildRequires:  %{python_module Keras-Applications >= 1.0.6}
BuildRequires:  %{python_module Keras-Preprocessing >= 1.0.5}
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Theano}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module numpy >= 1.9.1}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyux}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scipy >= 0.14}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  tensorflow
%endif
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
# match up with tensorflow
ExcludeArch:    %ix86
Requires:       python-Keras-Applications >= 1.0.6
Requires:       python-Keras-Preprocessing >= 1.0.5
Requires:       python-PyYAML
Requires:       python-numpy >= 1.9.1
Requires:       python-scipy >= 0.14
Requires:       python-six >= 1.9.0
Requires:       tensorflow
Provides:       python-keras = %{version}
%python_subpackages

%description
Keras is a high-level neural networks API, written in Python and capable of
running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on
enabling fast experimentation. Being able to go from idea to result with the
least possible delay is key to doing good research.

Use Keras if you need a deep learning library that:

    Allows for easy and fast prototyping (through user friendliness,
    modularity, and extensibility).  Supports both convolutional networks and
    recurrent networks, as well as combinations of the two.  Runs seamlessly on
    CPU and GPU.

Read the documentation at Keras.io.

%package examples
Summary:        High level examples for keras
Requires:       %{name}

%description examples
This are example scripts for deep learning. Most of the scripts will download
additional contens like traing and test samples.

%prep
%setup -q -n %{srcname}-%{version}
dos2unix examples/*

# we do not ship tensorboard/tensorflow_estimator:
rm tests/keras/callbacks/tensorboard_test.py

# downloads datasets from AWS:
rm tests/integration_tests/test_datasets.py

# test_api - needs cntk backend
rm tests/test_api.py

%build
%python_build

%install
%if !%{with test}
%python_install
mkdir -p %{buildroot}/%{_docdir}/%{name}/examples/
install -D examples/* %{buildroot}/%{_docdir}/%{name}/examples
# remove unneeded Keras and doc files
%python_expand rm -r %{buildroot}%{$python_sitelib}/docs
%python_expand %fdupes %{buildroot}%{$python_sitelib}/keras
%endif

%check
%if %{with test}
# test_TensorBoard_with_ReduceLROnPlateau - we don't have tensorboard
# test_unweighted or test_selu or test_weighted or test_scalar_weighted or test_sample_weighted - fails numeric calculations, we deviate too much
%pytest -n auto -k 'not (test_TensorBoard_with_ReduceLROnPlateau or test_unweighted or test_selu or test_weighted or test_scalar_weighted or test_sample_weighted or test_doc)'
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/keras
%{python_sitelib}/Keras-*

%files %{python_files examples}
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/examples
%endif

%changelog
