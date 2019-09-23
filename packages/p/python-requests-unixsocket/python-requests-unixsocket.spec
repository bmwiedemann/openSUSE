#
# spec file for package python-requests-unixsocket
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
Name:           python-requests-unixsocket
Version:        0.2.0
Release:        0
Summary:        UNIX domain socket backend for python-requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/msabramo/requests-unixsocket
Source:         https://files.pythonhosted.org/packages/source/r/requests-unixsocket/requests-unixsocket-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 1.1
Requires:       python-urllib3 >= 1.8
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 1.1}
BuildRequires:  %{python_module urllib3 >= 1.8}
BuildRequires:  %{python_module waitress}
# /SECTION
%python_subpackages

%description
With this module, python-requests is enhanced by the ability to talk
HTTP via a UNIX domain socket.

%prep
%setup -q -n requests-unixsocket-%{version}
# do not require additional test deps
sed -i -e '/addopts/d' pytest.ini 

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest requests_unixsocket/tests

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
