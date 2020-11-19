#
# spec file for package python-marshmallow-enum
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-marshmallow-enum
Version:        1.5.1
Release:        0
Summary:        Enum field for Marshmallow
License:        MIT
URL:            https://github.com/justanr/marshmallow_enum
Source:         https://files.pythonhosted.org/packages/source/m/marshmallow-enum/marshmallow-enum-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/justanr/marshmallow_enum/master/tests/test_enum_field.py
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module marshmallow >= 2.0.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-marshmallow >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Enum field for Marshmallow.

%prep
%setup -q -n marshmallow-enum-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG README.md
%license LICENSE
%{python_sitelib}/*

%changelog
