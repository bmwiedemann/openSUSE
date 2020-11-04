#
# spec file for package python-DataShape
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without tests

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-DataShape
Version:        0.5.4
Release:        0
Summary:        A data description language
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/blaze/datashape/
Source:         https://github.com/blaze/datashape/archive/%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module multipledispatch >= 0.4.7}
BuildRequires:  %{python_module numpy-devel >= 1.7}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with tests}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
%endif
Requires:       python-multipledispatch >= 0.4.7
Requires:       python-numpy >= 1.7
Requires:       python-python-dateutil
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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

%files %{python_files}
%defattr(-,root,root,-)
%doc  README.rst
%license LICENSE
%{python_sitelib}/datashape-%{version}-py*.egg-info
%{python_sitelib}/datashape/

%changelog
