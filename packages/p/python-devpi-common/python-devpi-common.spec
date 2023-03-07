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


Name:           python-devpi-common
Version:        3.7.2
Release:        0
Summary:        Utilities jointly used by devpi-server and devpi-client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/devpi/devpi
Source:         https://files.pythonhosted.org/packages/source/d/devpi-common/devpi-common-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-py >= 1.4.20
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
%setup -q -n devpi-common-%{version}
rm tox.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Doesn't work with latest packaging module because invalid version
donttest="test_noversion_sameproject or test_sort_sameproject_links"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/devpi_common
%{python_sitelib}/devpi_common-%{version}*-info

%changelog
