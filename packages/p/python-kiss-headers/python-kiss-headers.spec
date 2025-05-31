#
# spec file for package python-kiss-headers
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


Name:           python-kiss-headers
Version:        2.3.1
Release:        0
Summary:        Python package for parsing HTTP/1.1 style headers to objects
License:        MIT
URL:            https://www.kiss-headers.tech/
Source0:        https://files.pythonhosted.org/packages/source/k/kiss-headers/kiss-headers-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
A Python package for object-oriented HTTP/1.1 style headers. It includes
a parser and serializer for HTTP headers.

%prep
%autosetup -n kiss-headers-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no test files available in the tarball

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/kiss_headers
%{python_sitelib}/kiss_headers-%{version}*-info

%changelog
