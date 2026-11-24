#
# spec file for package python-formerly
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-formerly
Version:        0.1.0
Release:        0
Summary:        Deprecate a class that users inherit from
License:        BSD-3-Clause
URL:            https://github.com/scrapy/formerly
Source:         https://files.pythonhosted.org/packages/source/f/formerly/formerly-%{version}.tar.gz
BuildRequires:  %{python_module hatchling >= 1.27.0}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
formerly renames a class that users inherit from, without breaking them.

%prep
%autosetup -p1 -n formerly-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/formerly
%{python_sitelib}/formerly-%{version}.dist-info

%changelog
