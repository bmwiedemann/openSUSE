#
# spec file for package python-multipart
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


Name:           python-multipart
Version:        1.1.0
Release:        0
Summary:        Parser for multipart/form-data
License:        MIT
URL:            https://github.com/defnull/multipart
Source:         https://files.pythonhosted.org/packages/source/m/multipart/multipart-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module provides multiple parsers for RFC-7578 multipart/form-data, both
low-level for framework authors and high-level for WSGI application developers:

* PushMultipartParser: A low-level incremental SansIO <https://sans-io.readthedocs.io/>
  (non-blocking) parser suitable for asyncio and other time or memory constrained
  environments.
* MultipartParser: A streaming parser emitting memory- and disk-buffered
  MultipartPart instances.
* parse_form_data: A helper function to parse both multipart/form-data
  and application/x-www-form-urlencoded form submissions from a
  WSGI environment.

%prep
%autosetup -p1 -n multipart-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/multipart.py
%pycache_only %{python_sitelib}/__pycache__/multipart.*.pyc
%{python_sitelib}/multipart-%{version}.dist-info

%changelog
