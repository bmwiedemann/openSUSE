#
# spec file for package python-yara
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-yara
Version:        3.7.0
Release:        0
Summary:        Python Bindings for YARA (from Virus Total)
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/VirusTotal/yara-python
Source:         https://github.com/VirusTotal/yara-python/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(yara) >= 3.7
%python_subpackages

%description
python bindings for libyara.
YARA is a tool to identify and classify malware samples.

%prep
%setup -q -n yara-python-%{version}

%build
%python_build --dynamic-linking

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python tests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
