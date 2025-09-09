#
# spec file for package python-lazy-imports
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
Name:           python-lazy-imports
Version:        1.0.1
Release:        0
Summary:        Tool to support lazy imports
License:        Apache-2.0
URL:            https://github.com/bachorp/lazy-imports
Source:         https://github.com/bachorp/lazy-imports/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This python utility package helps to create *lazy modules*.
A lazy module defers loading (some of) its attributes until these attributes are first accessed.
The module's lazy attributes in turn are attributes of other modules.
These other modules will be imported/loaded only when (and if) associated attributes are used.
A lazy import strategy can drastically reduce runtime and memory consumption.

Additionally, this package provides a utility for *optional imports* with which one can import a module globally while triggering associated import errors only at use-sites (when and if a dependency is actually required, for example in the context of a specific functionality).

%prep
%autosetup -p1 -n lazy-imports-%{version}

%build
%pyproject_wheel

%check
%pytest

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/lazy_imports
%{python_sitelib}/lazy_imports-%{version}.dist-info

%changelog
