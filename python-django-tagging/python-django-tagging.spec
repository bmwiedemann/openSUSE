#
# spec file for package python-django-tagging
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
Name:           python-django-tagging
Version:        0.4.6
Release:        0
Summary:        A generic tagging application for Django projects
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/Fantomas42/django-tagging
Source:         https://files.pythonhosted.org/packages/source/d/django-tagging/django-tagging-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.8
BuildArch:      noarch
%python_subpackages

%description
A generic tagging application for Django projects,
which allows association of a number of tags
with any Model instance and makes retrieval of tags simple.

%prep
%setup -q -n django-tagging-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand %{_bindir}/django-admin.py-%{$python_bin_suffix} test --settings=tagging.tests.settings --pythonpath=`pwd`

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
