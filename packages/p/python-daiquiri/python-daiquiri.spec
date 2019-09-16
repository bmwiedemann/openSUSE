#
# spec file for package python-daiquiri
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-daiquiri
Version:        1.6.0
Release:        0
Summary:        Library to configure Python logging
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/jd/daiquiri
Source:         https://files.pythonhosted.org/packages/source/d/daiquiri/daiquiri-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-json-logger}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-json-logger
BuildArch:      noarch
%python_subpackages

%description
The daiquiri library provides a way to configure logging. It also
provides some custom formatters and handlers.

%prep
%setup -q -n daiquiri-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest daiquiri/tests

%files %{python_files}
%license LICENSE
%doc AUTHORS ChangeLog README.rst
%{python_sitelib}/*

%changelog
