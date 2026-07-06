#
# spec file for package python-yara
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-yara
Version:        4.5.4
Release:        0
Summary:        Python Bindings for YARA (from Virus Total)
License:        Apache-2.0
URL:            https://github.com/VirusTotal/yara-python
Source:         https://github.com/VirusTotal/yara-python/archive/v%{version}.tar.gz
# PATCH-FIX-OPENSUSE Specify dynamic linking in setup.cfg
Patch0:         use-dynamic-linking.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(yara) >= 4.0
%python_subpackages

%description
python bindings for libyara.
YARA is a tool to identify and classify malware samples.

%prep
%autosetup -p1 -n yara-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python tests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/yara.cpython*.so
%{python_sitearch}/yara_python-%{version}.dist-info

%changelog
