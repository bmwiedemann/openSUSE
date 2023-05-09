#
# spec file for package python-linkify-it-py
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-linkify-it-py
Version:        2.0.0
Release:        0
Summary:        Links recognition library with FULL unicode support
License:        MIT
URL:            https://github.com/tsutsu3/linkify-it-py
Source:         https://github.com/tsutsu3/linkify-it-py/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module uc-micro-py}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-uc-micro-py
BuildArch:      noarch
%python_subpackages

%description
Links recognition library with FULL unicode support. Focused on high quality link patterns detection in plain text.

Why it's awesome:
* Full unicode support, with astral characters!
* International domains support.
* Allows rules extension & custom normalizers.

%prep
%setup -q -n linkify-it-py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
