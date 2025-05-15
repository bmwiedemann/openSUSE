#
# spec file for package python-akismet
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017 Matthias Fehring <buschmann23@opensuse.org>
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


%define mod_name akismet
Name:           python-%{mod_name}
Version:        1.2.1
Release:        0
Summary:        Interface to the Akismet Anti Comment-Spam API
License:        BSD-3-Clause
URL:            https://github.com/ubernostrum/akismet
Source0:        https://files.pythonhosted.org/packages/source/a/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
A Python interface to the Akismet anti comment-spam API.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Can't run the tests as they need working server API
#%%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/akismet.py
%{python_sitelib}/akismet-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/akismet*

%changelog
