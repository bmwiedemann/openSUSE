#
# spec file for package python-zope.cachedescriptors
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-zope.cachedescriptors
Version:        6.0
Release:        0
Summary:        Method and property caching decorators
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.cachedescriptors
Source:         https://files.pythonhosted.org/packages/source/z/zope.cachedescriptors/zope_cachedescriptors-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.testrunner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
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
%setup -q -n zope_cachedescriptors-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} zope-testrunner-%{$python_bin_suffix} --test-path=src

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/zope/cachedescriptors
%{python_sitelib}/zope[_.]cachedescriptors-%{version}.dist-info

%changelog
