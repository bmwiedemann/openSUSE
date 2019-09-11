#
# spec file for package python-Deprecated
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
Name:           python-Deprecated
Version:        1.2.6
Release:        0
Summary:        Python @deprecated decorator
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tantale/deprecated
Source:         https://files.pythonhosted.org/packages/source/D/Deprecated/Deprecated-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wrapt >= 1.10}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-wrapt >= 1.10
BuildArch:      noarch
%python_subpackages

%description
If you need to mark a function or a method as deprecated,
you can use the ``@deprecated`` decorator.

%prep
%setup -q -n Deprecated-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.md
%license LICENSE.rst
%{python_sitelib}/*

%changelog
