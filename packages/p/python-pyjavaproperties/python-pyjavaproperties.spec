#
# spec file for package python-pyjavaproperties
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Abel Luck <abel@guardianproject.info>
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


Name:           python-pyjavaproperties
Version:        0.7
Release:        0
Summary:        Python library for parsing Java properties
License:        MIT
Group:          Development/Languages/Python
URL:            https://bitbucket.org/skeptichacker/pyjavaproperties
Source0:        https://files.pythonhosted.org/packages/source/p/pyjavaproperties/pyjavaproperties-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base
BuildArch:      noarch
%python_subpackages

%description
A python library for parsing Java properties files.

%prep
%setup -q -n pyjavaproperties-%{version}
sed -i '/^#!/d' pyjavaproperties.py pyjavaproperties_test.py

%build
%python_build

%install
%python_install
# Upstream patch to not install test module
# https://bitbucket.org/skeptichacker/pyjavaproperties/pull-requests/1
%{python_expand rm %{buildroot}%{$python_sitelib}/pyjavaproperties_test.py
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%python_exec pyjavaproperties_test.py

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.txt
%{python_sitelib}/*

%changelog
