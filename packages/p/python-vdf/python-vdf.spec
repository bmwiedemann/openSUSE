#
# spec file for package python-vdf
#
# Copyright (c) 2019 Matthias Fehring <buschmann23@opensuse.org>
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

%if 0%{?suse_version} > 1500
%define skip_python2 1
%endif

Name:           python-vdf
Version:        3.4
Release:        0
Summary:        Python Parser for VDF Files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ValvePython/vdf
Source:         %{name}-%{version}.tar.xz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
# START TESTING SECION
BuildRequires:  %{python_module pytest}
# END TESTING SECION
BuildArch:      noarch
%python_subpackages

%description
Pure python module for (de)serialization to and from VDF that works just like json.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand rm -f .coverage vdf/*.pyc tests/*.pyc
PYTHONHASHSEED=0 $python -m pytest tests
}

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
