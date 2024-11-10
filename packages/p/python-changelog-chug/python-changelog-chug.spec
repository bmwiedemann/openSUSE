#
# spec file for package python-changelog-chug
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


Name:           python-changelog-chug
Version:        0.0.3
Release:        0
Summary:        Parser library for project Change Log documents
License:        AGPL-3.0-or-later
URL:            https://git.sr.ht/~bignose/changelog-chug
Source:         https://files.pythonhosted.org/packages/source/c/changelog-chug/changelog_chug-%{version}.tar.gz
BuildRequires:  %{python_module docutils >= 0.21.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module semver >= 3.0.0}
BuildRequires:  %{python_module setuptools >= 62.4.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  %{python_module testtools}
# /SECTION
BuildRequires:  fdupes
Requires:       python-docutils >= 0.21.0
Requires:       python-semver >= 3.0.0
Suggests:       python-mccabe >= 0.7
BuildArch:      noarch
%python_subpackages

%description
changelog-chug is a parser for project Change Log documents.

%prep
%autosetup -p1 -n changelog_chug-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%doc README ChangeLog
%license LICENSE.AGPL-3 COPYING
%{python_sitelib}/chug
%{python_sitelib}/changelog_chug-%{version}.dist-info

%changelog
