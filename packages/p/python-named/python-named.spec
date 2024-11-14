#
# spec file for package python-named
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


Name:           python-named
Version:        1.4.2
Release:        0
Summary:        Named types
License:        MIT
URL:            https://github.com/nekitdev/named
Source:         https://github.com/nekitdev/named/archive/refs/tags/v%{version}.tar.gz#/named-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.9.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing-extensions
BuildArch:      noarch
%python_subpackages

%description
Named types.

This library defines the Named protocol for types that contain the __name__
attribute, abstracting the attribute itself away.

%prep
%autosetup -p1 -n named-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/named
%{python_sitelib}/named-%{version}.dist-info

%changelog
