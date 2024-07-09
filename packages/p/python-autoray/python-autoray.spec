#
# spec file for package python-autoray
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-autoray
Version:        0.6.12
Release:        0
Summary:        A lightweight python automatic-array library
License:        Apache-2.0
URL:            https://github.com/jcmgray/autoray
Source:         https://files.pythonhosted.org/packages/source/a/autoray/autoray-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module numpy < 2}
BuildRequires:  %{python_module opt-einsum}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Write backend agnostic numeric code compatible with any numpy-ish array library.

%prep
%setup -q -n autoray-%{version}
sed -i -e '/addopts/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# flaky test (failed 2 out of 6 times on x86_64 during preparation for submit)
donttest="(test_linalg_solve and float32-numpy)"
# 32 bit not supported upstream: this one fails because it cannot cast int64 to int32 on 32-bit
[ $(getconf LONG_BIT) -eq 32 ] && donttest="$donttest or (test_take and numpy)"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/autoray
%{python_sitelib}/autoray-%{version}.dist-info

%changelog
