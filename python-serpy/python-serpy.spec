#
# spec file for package python-serpy
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
Name:           python-serpy
Version:        0.3.1
Release:        0
Summary:        Object serialization for Python
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/clarkduvall/serpy
# https://github.com/clarkduvall/serpy/issues/70
Source:         https://github.com/clarkduvall/serpy/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
Serpy is an object serialization framework. Serpy serializes complex
datatypes (Django Models, custom
classes, ...) to simple native types (dicts, lists, strings, ...).
The native types can easily be converted to JSON or any other format
needed.

Since serializers are class based, they can be combined,
extended and customized with little code duplication. Compared
to other Python serialization frameworks like marshmallow or
Django Rest Framework Serializers, serpy is an order of
magnitude faster.

%prep
%setup -q -n serpy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
