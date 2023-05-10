#
# spec file for package python-jaraco.tidelift
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


Name:           python-jaraco.tidelift
Version:        1.5.1
Release:        0
Summary:        Tools to work with Tidelift
License:        MIT
URL:            https://github.com/jaraco/jaraco.tidelift
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.tidelift/jaraco.tidelift-%{version}.tar.gz
BuildRequires:  %{python_module autocommand}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module importlib-resources >= 1.6}
BuildRequires:  %{python_module keyring}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-autocommand
Requires:       python-importlib-resources >= 1.6
Requires:       python-keyring
Requires:       python-requests-toolbelt
BuildArch:      noarch
%python_subpackages

%description
jaraco.tidelift Tools for Tidelift

%prep
%setup -q -n jaraco.tidelift-%{version}
rm -rf jaraco.tidelift.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# there are no unittests or doctest-modules

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/tidelift
%{python_sitelib}/jaraco.tidelift-%{version}*-info

%changelog
