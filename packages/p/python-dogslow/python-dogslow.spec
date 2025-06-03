#
# spec file for package python-dogslow
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


Name:           python-dogslow
Version:        1.2
Release:        0
Summary:        A Django middleware that logs tracebacks of slow requests
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://bitbucket.org/evzijst/dogslow
Source:         https://files.pythonhosted.org/packages/source/d/dogslow/dogslow-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Django middleware that logs tracebacks of slow requests and allows further inspection.

%prep
%setup -q -n dogslow-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license COPYING.txt
%{python_sitelib}/dogslow
%{python_sitelib}/dogslow-%{version}.dist-info

%changelog
