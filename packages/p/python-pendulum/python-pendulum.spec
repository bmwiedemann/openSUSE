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
Name:           python-pendulum
Version:        2.1.0
Release:        0
Summary:        Python datetimes made easy
License:        MIT
Group:          Development/Languages/Python
URL:            https://pendulum.eustace.io
# https://github.com/sdispater/pendulum/issues/453
Source:         https://github.com/sdispater/pendulum/archive/%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.6}
BuildRequires:  %{python_module pytz >= 2018.3}
BuildRequires:  %{python_module pytzdata >= 2018.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  python-dephell-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  python3-dephell
Requires:       python-python-dateutil >= 2.6
Requires:       python-pytz >= 2018.3
Requires:       python-pytzdata >= 2018.3
Requires:       python-typing
%python_subpackages

%description
Python datetimes made easy

%prep
%setup -q -n pendulum-%{version}
%dephell_gensetup

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
