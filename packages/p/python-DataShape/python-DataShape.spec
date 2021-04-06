#
# spec file for package python-DataShape
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python36 1
%bcond_without python2
Name:           python-DataShape
Version:        0.5.4
Release:        0
Summary:        A data description language
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/blaze/datashape/
Source:         https://github.com/blaze/datashape/archive/%{version}.tar.gz
BuildRequires:  %{python_module multipledispatch >= 0.4.7}
BuildRequires:  %{python_module numpy >= 1.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
%if %{with python2}
BuildRequires:  python2-mock
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-multipledispatch >= 0.4.7
Requires:       python-numpy >= 1.7
Requires:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
DataShape is a language for describing data. It is an extension of the
NumPy dtype with an emphasis on cross language support.

%prep
%setup -q -n datashape-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# marking xfail works differently nowadays -- https://github.com/blaze/datashape/issues/78
donttest+=" or test_arbitrary_string and (s4 or s5 or s6)"
# https://github.com/blaze/datashape/issues/232
donttest+=" or test_user and (test_validate or test_nested_iteratables or test_tuples_can_be_records_too)"
%pytest -k "not (${donttest:4})"

%files %{python_files}
%doc  README.rst
%license LICENSE
%{python_sitelib}/datashape-%{version}*-info
%{python_sitelib}/datashape/

%changelog
