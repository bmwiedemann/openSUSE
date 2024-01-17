#
# spec file for package python-jaraco.develop
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
Name:           python-jaraco.develop
Version:        8.6.0
Release:        0
Summary:        Development utilities by jaraco
License:        MIT
URL:            https://github.com/jaraco/jaraco.develop
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.develop/jaraco.develop-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module autocommand}
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module jaraco.collections}
BuildRequires:  %{python_module jaraco.context}
BuildRequires:  %{python_module jaraco.ui}
BuildRequires:  %{python_module jaraco.vcs >= 1.1}
BuildRequires:  %{python_module keyring}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module path}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module subprocess-tee}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyNaCl
Requires:       python-autocommand
Requires:       python-build
Requires:       python-jaraco.collections
Requires:       python-jaraco.context
Requires:       python-jaraco.ui
Requires:       python-jaraco.vcs >= 1.1
Requires:       python-keyring
Requires:       python-packaging
Requires:       python-path
Requires:       python-requests-toolbelt
Requires:       python-setuptools
Requires:       python-subprocess-tee
BuildArch:      noarch
%python_subpackages

%description
Development utilities by jaraco

%prep
%autosetup -p1 -n jaraco.develop-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# *-github*.py and towncrier.get_version: No source repo or suitable VCS version found
# git.resolve: needs internet
# git.URLScheme: needs pytest plugin we don't have yet
%pytest --ignore-glob "*-github-*.py" -k "not (URLScheme or resolve or towncrier.get_version)"

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/jaraco/develop
%{python_sitelib}/jaraco.develop-%{version}.dist-info

%changelog
