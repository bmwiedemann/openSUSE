#
# spec file for package python-msgfy
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-msgfy
Version:        0.2.1
Release:        0
Summary:        Converts python exception instance to human-readable error messages
License:        MIT
URL:            https://github.com/thombashi/msgfy
Source:         https://files.pythonhosted.org/packages/source/m/msgfy/msgfy-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Python library for convert Exception instance to a human-readable
error message.

%prep
%setup -q -n msgfy-%{version}
# fix spurious exec permissions
find . -type f -exec chmod -x {} \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/msgfy
%{python_sitelib}/msgfy-%{version}.dist-info

%changelog
