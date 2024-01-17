#
# spec file for package python-pyPEG2
#
# Copyright (c) 2020 SUSE LLC
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
%define oldpython python
%define _name   pyPEG2
Name:           python-pyPEG2
Version:        2.15.2
Release:        0
Summary:        PEG Parser-Interpreter framework for Python
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://fdik.org/pyPEG2
Source:         https://files.pythonhosted.org/packages/source/p/%{_name}/%{_name}-%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  python-rpm-macros
Requires:       python-lxml
BuildArch:      noarch
%ifpython2
# python-pyPEG2 was last used in openSUSE Leap 14.2.
Provides:       %{oldpython}-pyPEG2 = %{version}
Obsoletes:      %{oldpython}-pyPEG2 < %{version}
%endif

%description
pyPEG is a plain and simple intrinsic parser interpreter framework
for Python. It is based on Parsing Expression Grammar, PEG.
With pyPEG you can parse many formal languages in a very easy way.

%python_subpackages

%prep
%setup -q -n %{_name}-%{version}

%build
%python_build

%install
%python_install

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.txt README.txt
%{python_sitelib}/pypeg2/
%{python_sitelib}/%{_name}-%{version}-py%{python_version}.egg-info

%changelog
