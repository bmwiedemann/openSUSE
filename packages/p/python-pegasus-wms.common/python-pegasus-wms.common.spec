#
# spec file for package python-pegasus-wms.common
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python2 1
Name:           python-pegasus-wms.common
Version:        5.0.3
Release:        0
Summary:        Pegasus Workflow Management System Python Commons
License:        Apache-2.0
URL:            https://pegasus.isi.edu
# SourceRepository: https://github.com/pegasus-isi/pegasus/packages/pegasus-python
Source:         pegasus-wms.common-gh-%{version}.tar.xz
# PATCH-FIX-OPENSUSE pegasus-wms-python3-to-sys.executable.patch code@bnavigator.de
Patch1:         pegasus-wms-python3-to-sys.executable.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML > 5.3}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML > 5.3
BuildArch:      noarch
%python_subpackages

%description
This package contains common files for the Python APIs for Pegasus WMS.

%prep
%autosetup -p1 -n pegasus-wms.common-gh-%{version}
sed -i 's/version=read_version(),/version="%{version}",/' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/Pegasus
%{python_sitelib}/pegasus_wms.common-%{version}.dist-info

%changelog
