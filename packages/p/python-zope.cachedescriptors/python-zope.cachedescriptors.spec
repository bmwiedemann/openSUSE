#
# spec file for package python-zope.cachedescriptors
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-zope.cachedescriptors
Version:        5.0
Release:        0
Summary:        Method and property caching decorators
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://github.com/zopefoundation/zope.cachedescriptors
Source:         https://files.pythonhosted.org/packages/source/z/zope.cachedescriptors/zope.cachedescriptors-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Cached descriptors cache their output.  They take into account
instance attributes that they depend on, so when the instance
attributes change, the descriptors will change the values they
return.

Cached descriptors cache their data in _v_ attributes, so they are
also useful for managing the computation of volatile attributes for
persistent objects.

%prep
%setup -q -n zope.cachedescriptors-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd build/lib
%{python_expand \
$python -m unittest -v zope.cachedescriptors.tests
$python -m doctest -v zope/cachedescriptors/*.rst
}

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
