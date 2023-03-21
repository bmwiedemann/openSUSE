#
# spec file for package python-translation-finder
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2019-2021 Matthias Fehring <buschmann23@opensuse.org>
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
%define modname translation-finder
%define skip_python2 1
Name:           python-translation-finder
Version:        2.15
Release:        0
Summary:        Translation Files Finder
License:        GPL-3.0-or-later
URL:            https://github.com/WeblateOrg/translation-finder
# test_data/linked has to be symlink, hance using github tar ball
Source:         https://github.com/WeblateOrg/translation-finder/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module twine}
BuildRequires:  %{python_module weblate-language-data >= 2021.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ruamel.yaml
Requires:       python-setuptools
Requires:       python-weblate-language-data >= 2021.2
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A translation file finder for Weblate, translation tool with tight version control integration.

%prep
%setup -q -n %{modname}-%{version}
sed -i -e '/pytest-runner/d' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/weblate-discover
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# remove test data
%python_expand rm -r %{buildroot}%{$python_sitelib}/translation_finder/test_data

%post
%python_install_alternative weblate-discover

%postun
%python_uninstall_alternative weblate-discover

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/weblate-discover
%{python_sitelib}/*

%changelog
