#
# spec file for package python-nosexcover
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
Name:           python-nosexcover
Version:        1.0.11
Release:        0
Summary:        Plugin extending nose.pluginscover with Cobertura-style XML reports
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/cmheisel/nose-xcover/
Source:         https://files.pythonhosted.org/packages/source/n/nosexcover/nosexcover-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/cmheisel/nose-xcover/master/LICENSE.txt
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coverage >= 3.4
Requires:       python-nose
BuildArch:      noarch
%python_subpackages

%description
A companion to the built-in nose.plugins.cover, this plugin will write out
an XML coverage report to a file named coverage.xml.

%prep
%setup -q -n nosexcover-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
