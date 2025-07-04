#
# spec file for package python-requests-ftp
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


Name:           python-requests-ftp
Version:        0.3.1
Release:        0
Summary:        FTP Transport Adapter for Requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Lukasa/requests-ftp
Source:         https://files.pythonhosted.org/packages/source/r/requests-ftp/requests-ftp-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Requests-FTP is an implementation of a very stupid FTP transport adapter for
use with the `Requests` Python library.

This library is *not* intended to be an example of Transport Adapters best
practices. This library was cowboyed together in about 4 hours of total work,
has no tests, and relies on a few ugly hacks. Instead, it is intended as both
a starting point for future development and an example for how to
implement transport adapters.

%prep
%setup -q -n requests-ftp-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/requests[-_]ftp
%{python_sitelib}/requests[-_]ftp-%{version}*-info

%changelog
