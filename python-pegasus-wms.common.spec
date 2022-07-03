#
# spec file for package python-pegasus-wms.common
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-pegasus-wms.common
Version:        5.0.2
Release:        0
Summary:        Pegasus Workflow Management System Python Commons
License:        Apache-2.0
URL:            https://pegasus.isi.edu
Source:         pegasus-wms.common-gh-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module PyYAML > 5.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-mock}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML > 5.3
BuildArch:      noarch
%python_subpackages

%description
This package contains common files for the Python APIs for Pegasus WMS.

%prep
%setup -q -n pegasus-wms.common-gh-%{version}
sed -i 's/version=read_version(),/version="%{version}",/' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/Pegasus
%{python_sitelib}/pegasus_wms.common-%{version}*-info

%changelog
