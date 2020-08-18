#
# spec file for package python-hcloud
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-hcloud
Version:        1.8.1
Release:        0
Summary:        Hetzner Cloud Python library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hetznercloud/hcloud-python
Source:         https://files.pythonhosted.org/packages/source/h/hcloud/hcloud-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future >= 0.17.1
Requires:       python-python-dateutil >= 2.7.5
Requires:       python-requests >= 2.20
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module future >= 0.17.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.7.5}
BuildRequires:  %{python_module requests >= 2.20}
# /SECTION
%python_subpackages

%description
Official Hetzner Cloud Python library.

%prep
%setup -q -n hcloud-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest tests/unit/

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
