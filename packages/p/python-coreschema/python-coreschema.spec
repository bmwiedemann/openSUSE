#
# spec file for package python-coreschema
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-coreschema
Version:        0.0.4
Release:        0
Summary:        Core Schema for Core API
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/core-api/python-coreschema
Source:         https://github.com/core-api/python-coreschema/archive/0.0.4.tar.gz#/coreschema-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
BuildArch:      noarch
%python_subpackages

%description
Core Schema for Core API, a format-independent Document Object Model for
representing Web APIs.

%prep
%setup -q -n python-coreschema-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pytest

%files %{python_files}
%{python_sitelib}/coreschema/
%{python_sitelib}/coreschema-%{version}-py*.egg-info

%changelog
