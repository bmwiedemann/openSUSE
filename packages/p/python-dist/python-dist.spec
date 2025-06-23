#
# spec file for package python-dist
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
Name:           python-dist
Version:        1.0.3
Release:        0
Summary:        Compute distance between two coordinates on the map
License:        MIT
URL:            https://github.com/duboviy/dist
Source:         https://github.com/duboviy/dist/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#duboviy/dist#dc41696801eb78ce47ef3964fd5e057ef4a971b5
Patch0:         fix-version-number.patch
# https://github.com/duboviy/dist/issues/8
Patch1:         python-dist-no-six.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
%python_subpackages

%description
As more and more apps are using maps, the more demand for geolocation capabilities increase.
Geolocation is about the reporting of your location to other users,
as well as associating real-world locations (such as landmarks) to your location.
This repo helps to accurately calculate the distance between two locations
and presents a time efficient practical solution,
that is almost 3 times faster than similar fast pure python implementation.

%prep
%autosetup -p1 -n dist-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python tests/test_performance.py

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitearch}/dist.cpython-*-linux-gnu.so
%{python_sitearch}/dist-%{version}.dist-info

%changelog
