#
# spec file for package python-bobodoctestumentation
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
%bcond_without test
Name:           python-bobodoctestumentation
Version:        2.4.0
Release:        0
Summary:        Bobo tests and documentation
License:        ZPL-2.1
Group:          Development/Languages/Python
Url:            http://www.python.org/pypi/bobodoctestumentation
# pypi package is outdated
Source:         https://github.com/zopefoundation/bobo/archive/2.4.0.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module zope.testing}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-WebTest
Requires:       python-manuel
Requires:       python-six
Requires:       python-zope.testing
BuildArch:      noarch

%python_subpackages

%description
The bobo documentation and tests are broken out into a separate project
to keep the bobo distribution as small as possible.

This package provides documentation and tests for the bobo package.

%prep
%setup -q -n bobo-%{version}/bobodoctestumentation

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*

%changelog
