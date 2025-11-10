#
# spec file for package python-hcloud
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

%{?sle15_python_module_pythons}
Name:           python-hcloud
Version:        2.10.0
Release:        0
Summary:        Hetzner Cloud Python library
License:        MIT
URL:            https://github.com/hetznercloud/hcloud-python
Source:         https://files.pythonhosted.org/packages/source/h/hcloud/hcloud-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.7.5
Requires:       python-requests >= 2.20
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.7.5}
BuildRequires:  %{python_module requests >= 2.20}
# /SECTION
%python_subpackages

%description
Official Hetzner Cloud Python library.

%prep
%autosetup -p1 -n hcloud-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest tests/unit/

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/hcloud
%{python_sitelib}/hcloud-%{version}.dist-info

%changelog
