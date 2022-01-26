#
# spec file for package python-autoray
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


%define packagename autoray
%define skip_python2 1
%{?!python_module:%define python_module() python3-%{**}}
Name:           python-autoray
Version:        0.2.5
Release:        0
Summary:        A lightweight python automatic-array library
License:        Apache-2.0
URL:            https://github.com/jcmgray/autoray
Source:         https://github.com/jcmgray/autoray/archive/%{version}.tar.gz#/autoray-%{version}.tar.gz
BuildRequires:  %{python_module dask-array if %python-base < 3.10}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Recommends:     python-dask-array
Recommends:     python-scipy
BuildArch:      noarch
%python_subpackages

%description
Write backend agnostic numeric code compatible with any numpy-ish array library.

%prep
%setup -q -n autoray-%{version}
sed -i -e '/addopt/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# flaky test (failed 2 out of 6 times on x86_64 during preparation for submit)
donttest="(test_linalg_solve and float32-numpy)"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{packagename}-%{version}*-info
%{python_sitelib}/%{packagename}

%changelog
