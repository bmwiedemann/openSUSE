#
# spec file for package python-FormEncode
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-FormEncode
Version:        1.3.1
Release:        0
Summary:        HTML form validation, generation, and conversion package
License:        Python-2.0
Group:          Development/Languages/Python
URL:            http://formencode.org
Source:         https://files.pythonhosted.org/packages/source/F/FormEncode/FormEncode-%{version}.tar.gz
Patch0:         remove-online-tests.patch
Patch1:         new-pycountry.patch
Patch2:         six.patch
# https://github.com/formencode/formencode/pull/154
Patch3:         python-FormEncode-remove-nose.patch
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module pycountry}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dnspython
Requires:       python-pycountry
Requires:       python-six
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-formencode = %{version}
Obsoletes:      %{oldpython}-formencode < %{version}
%endif
%python_subpackages

%description
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%prep
%setup -q -n FormEncode-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
dos2unix README.rst

%build
%python_build

%install
%python_install

# remove misplaced documentation
%python_expand rm -r %{buildroot}%{$python_sitelib}/docs

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# excluded tests poll dns
%pytest -k 'not (test_cyrillic_email or test_unicode_ascii_subgroup)' formencode/tests

%files %{python_files}
%doc README.rst
%{python_sitelib}/*

%changelog
