#
# spec file for package python-pendulum
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
# gh#python-pendulum/pendulum#844
%define skip_python313 1
Name:           python-pendulum
Version:        3.0.0
Release:        0
Summary:        Python datetimes made easy
License:        MIT
Group:          Development/Languages/Python
URL:            https://pendulum.eustace.io
# https://github.com/sdispater/pendulum/issues/453
Source0:        https://github.com/sdispater/pendulum/archive/%{version}.tar.gz#/pendulum-%{version}-gh.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.6}
BuildRequires:  %{python_module pytz >= 2022.1}
BuildRequires:  %{python_module time-machine >= 2.16.0}
BuildRequires:  %{python_module tzdata}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.6
Requires:       python-time-machine >= 2.16.0
Requires:       python-tzdata >= 2020.1
ExcludeArch:    %ix86 %arm32
%python_subpackages

%description
Python datetimes made easy

%prep
%autosetup -p1 -a1 -n pendulum-%{version}

%build
export CFLAGS="%{optflags}"
export CARGO_HOME=$PWD/rust/.cargo
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pendulum
%{python_sitearch}/pendulum-%{version}.dist-info

%changelog
