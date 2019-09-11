#
# spec file for package python-GeoIP
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
%define _name   GeoIP
Name:           python-GeoIP
Version:        1.3.2
Release:        0
Summary:        Python bindings for the GeoIP geographical lookup libraries
License:        LGPL-2.1+
Group:          Development/Languages/Python
Url:            https://github.com/maxmind/geoip-api-python
Source:         https://files.pythonhosted.org/packages/source/G/%{_name}/%{_name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  libGeoIP-devel
BuildRequires:  python-rpm-macros
%ifpython2
# python-GeoIP was last used in openSUSE Leap 14.2.
Provides:       %{oldpython}-GeoIP = %{version}
Obsoletes:      %{oldpython}-GeoIP < %{version}
%endif

%description
This package contains the Python bindings for the GeoIP API,
allowing IP to location lookups to country, city and organisation
level within Python code.

%python_subpackages

%prep
%setup -q -n %{_name}-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root)
%doc LICENSE README.rst
%doc examples/
%{python_sitearch}/%{_name}*.so
%{python_sitearch}/%{_name}-%{version}-py%{python_version}.egg-info

%changelog
