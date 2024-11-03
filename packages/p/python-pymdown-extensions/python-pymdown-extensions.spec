#
# spec file for package python-pymdown-extensions
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


Name:           python-pymdown-extensions
Version:        10.12
Release:        0
Summary:        Extension pack for Python Markdown
License:        MIT
URL:            https://github.com/facelessuser/pymdown-extensions
Source:         https://github.com/facelessuser/pymdown-extensions/archive/refs/tags/%{version}.tar.gz#/pymdown-extensions-%{version}.tar.gz
BuildRequires:  %{python_module Markdown >= 3.6}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# test requirements
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module Pygments >= 2.12}
BuildRequires:  %{python_module pytest}
#
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Markdown >= 3.6
Requires:       python-PyYAML >= 3.10
Recommends:     python-Pygments >= 2.12
BuildArch:      noarch
%python_subpackages

%description
PyMdown Extensions is a collection of extensions for Python Markdown.

They were originally written to make writing documentation more enjoyable.
Covering a wide range of solutions, and while not every extension is needed
by all people, there is usually at least one useful extension for anybody.

%prep
%autosetup -p1 -n pymdown-extensions-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
find %{buildroot} -type f -name "*.py" -exec chmod a-x {} +
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/pymdownx
%{python_sitelib}/pymdown_extensions-%{version}.dist-info

%changelog
