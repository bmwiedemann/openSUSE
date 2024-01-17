#
# spec file for package python-django-requests-debug-toolbar
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


%{?sle15_python_module_pythons}
Name:           python-django-requests-debug-toolbar
Version:        0.0.5
Release:        0
Summary:        A Django Debug Toolbar panel for Requests
License:        MIT
URL:            https://github.com/marceltschoppch/django-requests-debug-toolbar
Source:         https://files.pythonhosted.org/packages/de/15/82c597cc0d7017323a09d2dac5ad0a2818ab278140a063ac0a329690fd6c/django-requests-debug-toolbar-0.0.5.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Django Requests Debug Toolbar tracks all HTTP requests made with the popular
requests library.

%prep
%autosetup -p1 -n django-requests-debug-toolbar-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# The project doesn't provide any tests
#%%check
#%%pytest

%files %{python_files}
%{python_sitelib}/*

%changelog
