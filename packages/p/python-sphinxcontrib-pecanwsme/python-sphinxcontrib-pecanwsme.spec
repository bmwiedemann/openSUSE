#
# spec file for package python-sphinxcontrib-pecanwsme
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


Name:           python-sphinxcontrib-pecanwsme
Version:        0.11.0
Release:        0
Summary:        Extension to Sphinx for documenting APIs built with Pecan and WSME
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/dreamhost/sphinxcontrib-pecanwsme
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-pecanwsme/sphinxcontrib-pecanwsme-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinxcontrib-httpdomain}
BuildRequires:  python-rpm-macros
Requires:       python-sphinxcontrib-httpdomain
BuildArch:      noarch

%python_subpackages

%description
Extension to Sphinx for documenting APIs built with Pecan and WSME

%prep
%autosetup -p1 -n sphinxcontrib-pecanwsme-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/sphinxcontrib
%{python_sitelib}/sphinxcontrib_pecanwsme*

%changelog
