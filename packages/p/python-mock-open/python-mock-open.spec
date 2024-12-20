#
# spec file for package python-mock-open
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


Name:           python-mock-open
Version:        1.4.0
Release:        0
Summary:        A better mock for file I/O
License:        MIT
URL:            https://github.com/nivbend/mock-open
Source:         https://files.pythonhosted.org/packages/source/m/mock-open/mock-open-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if 0%{?suse_version} <= 1500
BuildRequires:  python-mock
%endif
%ifpython2
Requires:       python-mock
%endif
%python_subpackages

%description
A better mock for file I/O

%prep
%setup -q -n mock-open-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v mock_open.test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/mock_open
%{python_sitelib}/mock_open-%{version}.dist-info

%changelog
