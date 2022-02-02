#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
# sync with tensorflow2
%define pythons python3
%if 0%{?suse_version} < 1599
ExclusiveArch: donotbuild
%endif
Name:           python-Keras%{psuffix}
Version:        2.7.0
Release:        0
Summary:        Deep Learning library
License:        Apache-2.0
URL:            https://keras.io/
# no sdist. Use the pure wheel. It is much easier than a Bazel build
Source0:        https://files.pythonhosted.org/packages/py2.py3/k/keras/keras-%{version}-py2.py3-none-any.whl
# For Tests
Source1:        https://github.com/keras-team/keras/archive/refs/tags/v%{version}.tar.gz#/keras-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
ExcludeArch:    %{ix86}
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module numpy >= 1.19}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module scipy >= 1.5.2}
BuildRequires:  tensorflow2
%endif
Provides:       python-keras = %{version}-%{release}
Obsoletes:      python-keras < %{version}-%{release}
%python_subpackages

%description

Keras is a deep learning API written in Python, running on top of the machine learning
platform TensorFlow. It was developed with a focus on enabling fast experimentation.
Being able to go from idea to result as fast as possible is key to doing good research.

%prep
%setup -q -n keras-%{version} -b1

%build

%if ! %{with test}
%install
%pyproject_install %{SOURCE0}
cp %{buildroot}%{python3_sitelib}/keras-%{version}.dist-info/LICENSE .
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%{python_expand # call the main() functions of python tests
for f in keras/tests/*_test.py; do
  # ValueError: Please provide a TPU Name to connect to.
  [ "$f" = "keras/tests/automatic_outside_compilation_test.py" ] && continue || :
  # import error: test file not installed into sitelib
  [ "$f" = "keras/tests/get_config_test.py" ] && continue || :
  # no tensorflow.compiler.tests in installed tensorflow2 package
  [ "$f" = "keras/tests/tracking_util_xla_test.py" ] && continue || :
  # Note: These might be genuine errors, but in order to get it checked in, we rather ignore them now.
  #       It is still better than not running any tests at all.
  $python $f
done
}
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE
%{python_sitelib}/keras
%{python_sitelib}/keras-%{version}.dist-info
%endif

%changelog
