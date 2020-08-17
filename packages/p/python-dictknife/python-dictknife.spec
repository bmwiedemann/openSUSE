#
# spec file for package python-dictknife
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-dictknife
Version:        0.13.0
Release:        0
Summary:        Army knife of handling data
License:        MIT
URL:            https://github.com/podhmo/dictknife
Source:         https://github.com/podhmo/dictknife/archive/%{version}.tar.gz#/dictknife-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module google-api-python-client}
BuildRequires:  %{python_module jsonpatch}
BuildRequires:  %{python_module magicalimport}
BuildRequires:  %{python_module oauth2client}
BuildRequires:  %{python_module prestring}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-PyYAML
Suggests:       python-google-api-python-client
Suggests:       python-jsonpatch
Suggests:       python-magicalimport
Suggests:       python-oauth2client
Suggests:       python-prestring
Suggests:       python-toml
BuildArch:      noarch
%python_subpackages

%description
Army knife of handling data, able to read and write JSON, YAML and TOML,
and transform, merge and diff datasets.

Includes jsonknife for splitting files and dereferencing JSON using
JSON pointer syntax.

%prep
%setup -q -n dictknife-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/dictknife
%python_clone -a %{buildroot}%{_bindir}/jsonknife
%python_clone -a %{buildroot}%{_bindir}/swaggerknife
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative dictknife
%python_install_alternative jsonknife
%python_install_alternative swaggerknife

%postun
%python_uninstall_alternative dictknife
%python_uninstall_alternative jsonknife
%python_uninstall_alternative swaggerknife

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/dictknife
%python_alternative %{_bindir}/jsonknife
%python_alternative %{_bindir}/swaggerknife
%{python_sitelib}/*

%changelog
