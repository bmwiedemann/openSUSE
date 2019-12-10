#
# spec file for package python-dist
#
# Copyright (c) 2019 SUSE LLC
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
Name:           python-dist
Version:        1.0.3
Release:        0
Summary:        Compute distance between two coordinates on the map
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/duboviy/dist
Source:         https://github.com/duboviy/dist/archive/%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
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
%setup -q -n dist-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python tests/test_performance.py

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitearch}/*

%changelog
