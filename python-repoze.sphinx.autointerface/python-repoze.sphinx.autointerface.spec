#
# spec file for package python
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%global modname repoze.sphinx.autointerface
Name:           python-%{modname}
Version:        0.8
Release:        0
Summary:        Sphinx extension: auto-generates API docs from Zope interfaces
License:        SUSE-Repoze
Group:          Development/Languages/Python
URL:            http://www.repoze.org
Source:         https://files.pythonhosted.org/packages/source/r/repoze.sphinx.autointerface/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
Requires:       python-zope.interface
BuildArch:      noarch
%python_subpackages

%description
Thie package defines an extension for the Sphinx documentation system. The
extension allows generation of API documentation by introspection of
zope.interface instances in code.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.rst
%{python_sitelib}/*

%changelog
