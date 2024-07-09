#
# spec file for package python-flexmock
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


%{?sle15_python_module_pythons}
Name:           python-flexmock
Version:        0.12.1
Release:        0
Summary:        Testing library for creating mocks, stubs and fakes
License:        BSD-2-Clause
URL:            https://github.com/bkabrda/flexmock
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Flexmock is a testing library for Python for creating mocks,
stubs and fakes. The API is inspired by a Ruby library of the same name, but
Python flexmock is not a clone of the Ruby version. It omits a number of
redundancies in the Ruby flexmock API, alters some defaults, and introduces
a number of Python-only features.

%prep
%autosetup -n flexmock-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/flexmock
%{python_sitelib}/flexmock-%{version}-py*.egg-info

%changelog
