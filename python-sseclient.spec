#
# spec file for package python-sseclient
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


Name:           python-sseclient
Version:        0.0.27
Release:        0
Summary:        Python client library for reading Server Sent Event streams
License:        MIT
URL:            https://github.com/btubbs/sseclient
Source:         https://files.pythonhosted.org/packages/source/s/sseclient/sseclient-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
Requires:       python-requests >= 2.9
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This is a Python client library for iterating over http Server Sent Event (SSE)
streams (also known as EventSource, after the name of the Javascript interface
inside browsers). The SSEClient class accepts a url on init, and is then an
iterator over messages coming from the server.

%prep
%autosetup -p1 -n sseclient-%{version}
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python|g' sseclient.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand chmod u+x %{buildroot}%{$python_sitelib}/sseclient.py

%check
# Testsuite requires active internet connection

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/__pycache__/sseclient.*
%{python_sitelib}/sseclient.py
%{python_sitelib}/sseclient-%{version}.dist-info

%changelog
