#
# spec file for package python-get-annotations
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

%{?sle15_python_module_pythons}
Name:           python-get-annotations
Version:        0.1.2
Release:        0
Summary:        A backport of Python 3.10's inspectget_annotation() function
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/shawwn/get-annotations
Source:         https://github.com/shawwn/get-annotations/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source:       https://files.pythonhosted.org/packages/source/g/get-annotations/get-annotations-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
## needed for tests
BuildRequires:  %{python_module pytest}
BuildArch:      noarch
%python_subpackages

%description
%summary.

%prep
%autosetup -p1 -n get-annotations-%{version}

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
%{python_sitelib}/get_annotations
%{python_sitelib}/get_annotations-%{version}.dist-info

%changelog
