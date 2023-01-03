#
# spec file for package python-mediafile
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-mediafile
Version:        0.11.0
Release:        0
Summary:        Handles low-level interfacing for files' tags Wraps Mutagen to
License:        MIT
URL:            https://github.com/beetbox/mediafile
Source:         https://files.pythonhosted.org/packages/source/m/mediafile/mediafile-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit >= 2}
BuildRequires:  %{python_module mutagen >= 1.45}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.9}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mutagen >= 1.45
Requires:       python-six >= 1.9
BuildArch:      noarch
%python_subpackages

%description
Handles low-level interfacing for files' tags. Wraps Mutagen to

%prep
%setup -q -n mediafile-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/mediafile.py
%{python_sitelib}/mediafile-%{version}*-info/
%{python_sitelib}/__pycache__/mediafile*

%changelog
