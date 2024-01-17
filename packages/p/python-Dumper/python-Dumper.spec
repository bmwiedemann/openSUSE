#
# spec file for package python-Dumper
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Dumper
Version:        1.2.0
Release:        0
Summary:        Tool to conveniently describe any Python datastructure
License:        MIT
URL:            https://github.com/jric/Dumper.py
Source:         https://github.com/jric/Dumper.py/archive/refs/tags/%{version}.tar.gz#/Dumper.py-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Tool to conveniently describe any Python datastructure

%prep
%setup -q -n Dumper.py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python test.py
}

%files %{python_files}
%doc README.md
%{python_sitelib}/dumper/
%{python_sitelib}/Dumper-%{version}-py*.egg-info

%changelog
