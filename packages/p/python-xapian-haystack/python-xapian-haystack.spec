#
# spec file for package python-xapian-haystack
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020 Stasiek Michalski <hellcp@opensuse.org>.
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
%global modname xapian-haystack
Name:           python-%{modname}
Version:        3.1.0
Release:        0
Summary:        Backend of Django-Haystack for the Xapian search engine
License:        GPL-2.0-only
URL:            https://github.com/notanumber/xapian-haystack
Source:         https://files.pythonhosted.org/packages/source/x/xapian_haystack/%{modname}-%{version}.tar.gz
#PATCH-FIX-UPSTREAM https://github.com/notanumber/xapian-haystack/pull/181 Add Xapian Omega solution to haystack backend to fix long term issues
Patch:          python-xapian-haystack-term-too-long.patch
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module django-haystack >= 3.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-django-haystack >= 3.0
Requires:       python-filelock
BuildArch:      noarch
%python_subpackages

%description
Xapian-haystack is a backend of Django-Haystack for the Xapian search engine.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/xapian_backend.py
%pycache_only %{python_sitelib}/__pycache__/xapian_backend*.py*
%{python_sitelib}/xapian_haystack-%{version}.dist-info

%changelog
