#
# spec file for package python-audioop-lts
#
# Copyright (c) 2024 SUSE LLC
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


%define pythons python313
Name:           python-audioop-lts
Version:        0.2.1
Release:        0
Summary:        LTS Port of Python audioop
License:        PSF-2.0
URL:            https://github.com/AbstractUmbra/audioop
Source:         https://files.pythonhosted.org/packages/source/a/audioop-lts/audioop_lts-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
LTS Port of Python audioop

%prep
%autosetup -p1 -n audioop_lts-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch tests/test_audioop.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/audioop
%{python_sitearch}/audioop_lts-%{version}.dist-info

%changelog
