#
# spec file for package python-girder-client
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-girder-client
Version:        2.4.0
Release:        0
Summary:        Python Girder client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://girder.readthedocs.org/en/latest/python-client.html
Source:         https://files.pythonhosted.org/packages/source/g/girder-client/girder-client-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 6.7
Requires:       python-diskcache
Requires:       python-requests >= 2.4.2
Requires:       python-requests-toolbelt
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 6.7}
BuildRequires:  %{python_module diskcache}
BuildRequires:  %{python_module requests >= 2.4.2}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Girder is a web-based data management platform.

This package provides the client for interacting
with Girder servers

%prep
%setup -q -n girder-client-%{version}
sed -i -e '/^#!\//, 1d' girder_client/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%python3_only %{_bindir}/girder-cli
%python3_only %{_bindir}/girder-client
%{python_sitelib}/*

%changelog
