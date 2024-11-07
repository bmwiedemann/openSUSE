#
# spec file for package python-PyGithub
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-PyGithub
Version:        2.5.0
Release:        0
Summary:        Python library to use the GitHub API v3
License:        LGPL-3.0-or-later
URL:            https://github.com/PyGithub/PyGithub
Source:         https://files.pythonhosted.org/packages/source/p/pygithub/pygithub-%{version}.tar.gz
Source99:       python-PyGithub.rpmlintrc
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module PyJWT >= 2.4.0}
BuildRequires:  %{python_module PyNaCl >= 1.4.0}
BuildRequires:  %{python_module cryptography >= 3.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.14.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions >= 4.0.0}
BuildRequires:  %{python_module urllib3 >= 1.26.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Deprecated
Requires:       python-PyJWT >= 2.4.0
Requires:       python-PyNaCl >= 1.4.0
Requires:       python-cryptography >= 3.4
Requires:       python-requests >= 2.14.0
Requires:       python-typing-extensions >= 4.0.0
Requires:       python-urllib3 >= 1.26.0
Provides:       python-pygithub = %{version}-%{release}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module httpretty}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
PyGitHub is a Python library to access the GitHub REST API.
This library enables you to manage [GitHub] resources such as repositories,
user profiles, and organizations in your Python applications.

%prep
%autosetup -p1 -n pygithub-%{version}
sed -i s/--color=yes// pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING COPYING.LESSER
%doc README.md
%{python_sitelib}/github
%{python_sitelib}/PyGithub-%{version}.dist-info

%changelog
