#
# spec file for package python-nose-exclude
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Weberhofer GmbH, Austria
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
Name:           python-nose-exclude
Version:        0.5.0
Release:        0
Summary:        Nose plugin to exclude specific directories from nosetests runs
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
Url:            https://bitbucket.org/kgrandis/nose-exclude/overview
Source0:        https://files.pythonhosted.org/packages/source/n/nose-exclude/nose-exclude-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-nose
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
nose-exclude is a Nose plugin that allows you to easily specify
directories to be excluded from testing.

%prep
%setup -q -n nose-exclude-%{version}

%build
%python_build

%check
%python_exec setup.py -q test

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*

%changelog
