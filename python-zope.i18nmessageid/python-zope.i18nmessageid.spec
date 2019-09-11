#
# spec file for package python-zope.i18nmessageid
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
Name:           python-zope.i18nmessageid
Version:        4.3.1
Release:        0
Summary:        Zope Location
License:        ZPL-2.1
Group:          Development/Languages/Python
Url:            http://www.python.org/pypi/zope.i18nmessageid
Source:         https://files.pythonhosted.org/packages/source/z/zope.i18nmessageid/zope.i18nmessageid-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION documentation requirements
BuildRequires:  %{python_module Sphinx}
Requires:       python-six
# /SECTION
%python_subpackages

%description
In Zope3, i18nmessageid are special objects that has a structural i18nmessageid.

%package     -n %{name}-doc
Summary:        Zope Location
Group:          Development/Languages/Python
Provides:       %{python_module zope.i18nmessageid-doc = %{version}}
Requires:       %{name} = %{version}

%description -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n zope.i18nmessageid-%{version}
rm -rf zope.i18nmessageid.egg-info

%build
%python_build
%__python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo build/sphinx/html/objects.inv

%install
%python_install
# don't bother with development files
%{python_expand rm -f %{buildroot}%{$python_sitearch}/zope/i18nmessageid/_zope_i18nmessageid_message.c
  %fdupes -s %{buildroot}%{$python_sitearch}
}

%check
%python_exec setup.py test

%files %{python_files}
%defattr(-,root,root)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{python_sitearch}/*

%files -n %{name}-doc
%defattr(-,root,root)
%doc build/sphinx/html/

%changelog
