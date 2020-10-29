#
# spec file for package python-pendulum
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
%define skip_python2 1
Name:           python-pendulum
Version:        2.1.2
Release:        0
Summary:        Python datetimes made easy
License:        MIT
Group:          Development/Languages/Python
URL:            https://pendulum.eustace.io
# https://github.com/sdispater/pendulum/issues/453
Source:         https://github.com/sdispater/pendulum/archive/%{version}.tar.gz#/pendulum-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.6}
BuildRequires:  %{python_module pytz >= 2020.1}
BuildRequires:  %{python_module pytzdata >= 2020.1}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.6
Requires:       python-pytz >= 2020.1
Requires:       python-pytzdata >= 2020.1
Requires:       python-typing
%python_subpackages

%description
Python datetimes made easy

%prep
%setup -q -n pendulum-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%{python_expand # remove source files
find %{buildroot}%{$python_sitearch} -name '*.c' -delete
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pendulum
%{python_sitearch}/pendulum-%{version}*-info

%changelog
