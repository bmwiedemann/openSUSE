#
# spec file for package python-selectors2
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
Name:           python-selectors2
Version:        2.0.1
Release:        0
Summary:        Back-ported, durable, and portable selectors
License:        MIT
Group:          Development/Languages/Python
Url:            https://www.github.com/SethMichaelLarson/selectors2
Source:         https://files.pythonhosted.org/packages/source/s/selectors2/selectors2-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Back-ported, durable, and portable selectors

%prep
%setup -q -n selectors2-%{version}
# bump the tolerance
sed -i -e 's:TOLERANCE = 1:TOLERANCE = 2:g' tests/support.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
