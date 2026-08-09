#
# spec file for package python-ezgb
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-ezgb
Version:        0.2.0
Release:        0
Summary:        Python library for git-bug
License:        GPL-2.0-or-later
URL:            https://git.kernel.org/pub/scm/utils/ezgb/ezgb.git/
Source0:        https://git.kernel.org/pub/scm/utils/ezgb/ezgb.git/snapshot/ezgb-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pygit2}
BuildRequires:  %{python_module pytest}
BuildRequires: ca-certificates
BuildRequires: ca-certificates-mozilla
# /SECTION
Requires:       python-pygit2
%python_subpackages

%description
A standalone Python library for working with https://github.com/git-bug/git-bug
repositories. It lets you list, create, query, and update bugs that are stored
as native git objects -- no external database required.

%prep
%autosetup -n ezgb-%{version}

# drop invalid shebangs
sed -i '1{/^#!/d}' src/ezgb/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/ezgb

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.md
%license COPYING
%{python_sitelib}/ezgb
%{python_sitelib}/ezgb-%{version}*-info

%changelog
