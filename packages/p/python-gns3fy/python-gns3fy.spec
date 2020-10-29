#
# spec file for package python-gns3fy
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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
%define skip_python2 1
Name:           python-gns3fy
Version:        0.7.1
Release:        0
Summary:        Python wrapper around GNS3 Server API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/davidban77/gns3fy
Source:         https://github.com/davidban77/gns3fy/archive/v%{version}.tar.gz#/gns3fy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pydantic >= 1.0
Requires:       python-requests >= 2.22
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pydantic >= 1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.22}
BuildRequires:  %{python_module requests-mock}
# /SECTION
%python_subpackages

%description
Python wrapper around GNS3 Server API. Its main objective is to
interact with the GNS3 server in a programatic way, so it can
be integrated with the likes of Ansible, docker and scripts.
https://gns3-server.readthedocs.io/en/latest/

%prep
%setup -q -n gns3fy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license docs/content/about/license.md
%doc README.md
%{python_sitelib}/gns3fy
%{python_sitelib}/gns3fy-%{version}*-info

%changelog
