#
# spec file for package python-ara
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ara
Version:        1.0.1
Release:        0
Summary:        ARA Records Ansible
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
Url:            https://github.com/ansible-community/ara
Source:         https://files.pythonhosted.org/packages/source/a/ara/ara-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
Recommends:     python-Django >= 2.1.5
Recommends:     python-django-cors-headers
Recommends:     python-django-filter
Recommends:     python-djangorestframework >= 3.9.1
Recommends:     python-dynaconf
Recommends:     python-whitenoise
BuildArch:      noarch

%python_subpackages

%description
ARA saves playbook results to a local or remote database by using an
Ansible callback plugin and provides an API to integrate this data in
tools and interfaces.

%prep
%setup -q -n ara-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/ara-manage
%{python_sitelib}/*

%changelog
