#
# spec file for package python-python-rpm-spec
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-python-rpm-spec
Version:        0.16.0
Release:        0
Summary:        Python module for parsing RPM spec files
License:        MIT
URL:            https://github.com/bkircher/python-rpm-spec
Source0:        https://files.pythonhosted.org/packages/source/p/python_rpm_spec/python_rpm_spec-%{version}.tar.gz
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Conflicts:      python-pyrpm
BuildArch:      noarch
%python_subpackages

%description
python-rpm-spec is a Python module for parsing RPM spec files. RPMs are build
from a package's sources along with a spec file. The spec file controls how the
RPM is built. This module allows you to parse spec files and gives you simple
access to various bits of information that is contained in the spec file.

%prep
%autosetup -p1 -n python_rpm_spec-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/pyrpm
%{python_sitelib}/python_rpm_spec-%{version}.dist-info

%changelog
