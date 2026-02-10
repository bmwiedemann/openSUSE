#
# spec file for package python-jaraco.compat
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


Name:           python-jaraco.compat
Version:        4.3.1
Release:        0
Summary:        Modules providing forward compatibility across Python versions
License:        MIT
URL:            https://github.com/jaraco/jaraco.compat
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.compat/jaraco_compat-4.3.1.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 6}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Modules providing forward compatibility across Python versions

%prep
%autosetup -p1 -n jaraco_compat-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc NEWS.rst README.rst
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/compat
%{python_sitelib}/jaraco_compat-%{version}.dist-info

%changelog
