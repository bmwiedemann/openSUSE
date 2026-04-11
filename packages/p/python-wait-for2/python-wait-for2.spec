#
# spec file for package python-wait-for2
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


%{?sle15_python_module_pythons}
Name:           python-wait-for2
Version:        0.4.1
Release:        0
Summary:        Asyncio wait_for that handles simultaneous cancellation and future completion
License:        Apache-2.0
URL:            https://github.com/Traktormaster/wait-for2
Source:         https://files.pythonhosted.org/packages/source/w/wait_for2/wait_for2-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Alternate implementation of asyncio.wait_for() that handles several
edge cases like simultaneous cancellation and completion of futures
consistently across Python versions.

%prep
%autosetup -p1 -n wait_for2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/wait_for2
%{python_sitelib}/wait_for2-%{version}.dist-info

%changelog
