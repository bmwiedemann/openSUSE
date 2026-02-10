#
# spec file for package python-jaraco.services
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


Name:           python-jaraco.services
Version:        4.0.0
Release:        0
Summary:        Service orchestration and pytest plugins
License:        MIT
URL:            https://github.com/jaraco/jaraco.services
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.services/jaraco_services-4.0.0.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module jaraco.classes}
BuildRequires:  %{python_module path}
BuildRequires:  %{python_module portend}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tempora}
# /SECTION
BuildRequires:  fdupes
Requires:       python-jaraco.classes
Requires:       python-path
Requires:       python-portend
Requires:       python-tempora
BuildArch:      noarch
%python_subpackages

%description
Service orchestration and pytest plugins

%prep
%autosetup -p1 -n jaraco_services-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/services
%{python_sitelib}/jaraco_services-%{version}.dist-info

%changelog
