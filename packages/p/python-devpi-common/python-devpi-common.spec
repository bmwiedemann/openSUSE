#
# spec file for package python-devpi-common
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
Name:           python-devpi-common
Version:        4.0.2
Release:        0
Summary:        Utilities jointly used by devpi-server and devpi-client
License:        MIT
URL:            https://github.com/devpi/devpi
Source:         https://files.pythonhosted.org/packages/source/d/devpi-common/devpi-common-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lazy
Requires:       python-packaging
Requires:       python-requests >= 2.3.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module py >= 1.4.20}
BuildRequires:  %{python_module lazy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.3.0}
# /SECTION
%python_subpackages

%description
Utilities jointly used by devpi-server and devpi-client.

%prep
%autosetup -p1 -n devpi-common-%{version}
rm tox.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/devpi_common
%{python_sitelib}/devpi_common-%{version}.dist-info

%changelog
