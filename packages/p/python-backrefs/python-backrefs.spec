#
# spec file for package python-backrefs
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-backrefs
Version:        6.1
Release:        0
Summary:        A wrapper around re and regex that adds additional back references
License:        MIT
URL:            https://github.com/facelessuser/backrefs
Source:         https://files.pythonhosted.org/packages/source/b/backrefs/backrefs-%{version}.tar.gz
BuildRequires:  %{python_module hatchling >= 0.21.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-regex
BuildArch:      noarch
%python_subpackages

%description
Backrefs is a wrapper around Python's built-in [Re][re] and the 3rd party [Regex][regex] library.  Backrefs adds various
additional back references (and a couple other features) that are known to some regular expression engines, but not to
Python's Re and/or Regex.  The supported back references actually vary depending on the regular expression engine being
used as the engine may already have support for some.

```python
from backrefs import bre
>>> pattern = bre.compile(r'(\p{Letter}+)')
>>> pattern.sub(r'\C\1\E', 'sometext')
'SOMETEXT'
```

%prep
%autosetup -p1 -n backrefs-%{version}
# Fix build, remove build_data["tag"] to do not override the wheel
# filename, python-rpm-macros rely on the standard naming for multiflavor
sed -i '/build_data\[/d' hatch_build.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.md LICENSE.md
%{python_sitelib}/backrefs
%{python_sitelib}/backrefs-%{version}.dist-info

%changelog
