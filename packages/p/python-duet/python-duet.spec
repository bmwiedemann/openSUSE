#
# spec file for package python-duet
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-duet
Version:        0.2.8
Release:        0
Summary:        A simple future-based async library for python
License:        Apache-2.0
URL:            https://github.com/google/duet
Source:         https://files.pythonhosted.org/packages/source/d/duet/duet-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions}
%if 0%{suse_version} <= 1500
BuildRequires:  %{python_module asyncio-contextmanager}
BuildRequires:  %{python_module contextvars}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions
%if %python_version_nodots <= 36
Requires:       python-asyncio-contextmanager
Requires:       python-contextvars
%endif
BuildArch:      noarch
%python_subpackages

%description
A simple future-based async library for python.

%prep
%setup -q -n duet-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/duet
%{python_sitelib}/duet-%{version}*-info

%changelog
