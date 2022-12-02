#
# spec file for package python-daiquiri
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


%global skip_python2 1
Name:           python-daiquiri
Version:        3.2.1
Release:        0
Summary:        Library to configure Python logging
License:        Apache-2.0
URL:            https://github.com/jd/daiquiri
Source:         https://files.pythonhosted.org/packages/source/d/daiquiri/daiquiri-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-json-logger}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
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
%doc README.rst
%{python_sitelib}/daiquiri
%{python_sitelib}/daiquiri-%{version}*-info

%changelog
