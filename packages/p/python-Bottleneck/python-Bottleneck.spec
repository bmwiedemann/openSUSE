#
# spec file for package python-Bottleneck
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
Name:           python-Bottleneck
Version:        1.2.1
Release:        0
Summary:        A collection of fast NumPy array functions
License:        BSD-2-Clause and BSD-3-Clause
Group:          Development/Libraries/Python
Url:            http://berkeleyanalytics.com/bottleneck/
Source0:        https://files.pythonhosted.org/packages/source/B/Bottleneck/Bottleneck-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.9.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.9.1
%python_subpackages

%description
Bottleneck is a collection of fast NumPy array functions written in C

%prep
%setup -q -n Bottleneck-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%defattr(-,root,root)
%doc README.rst RELEASE.rst LICENSE
%{python_sitearch}/bottleneck/
%{python_sitearch}/Bottleneck-%{version}-py*.egg-info

%changelog
