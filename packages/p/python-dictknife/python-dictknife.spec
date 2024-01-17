#
# spec file for package python-dictknife
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


%{?sle15_python_module_pythons}
Name:           python-dictknife
Version:        0.14.0
Release:        0
Summary:        Army knife of handling data
License:        MIT
URL:            https://github.com/podhmo/dictknife
Source:         https://github.com/podhmo/dictknife/archive/%{version}.tar.gz#/dictknife-%{version}.tar.gz
Patch0:         support-python-310.patch
BuildRequires:  %{python_module google-api-python-client}
BuildRequires:  %{python_module google-auth-oauthlib}
BuildRequires:  %{python_module jsonpatch}
BuildRequires:  %{python_module magicalimport}
BuildRequires:  %{python_module prestring}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       python-ruamel.yaml
Suggests:       python-google-api-python-client
Suggests:       python-google-auth-oauthlib
Suggests:       python-jsonpatch
Suggests:       python-magicalimport
Suggests:       python-prestring
BuildArch:      noarch
%python_subpackages

%description
Army knife of handling data, able to read and write JSON, YAML and TOML,
and transform, merge and diff datasets.

Includes jsonknife for splitting files and dereferencing JSON using
JSON pointer syntax.

%prep
%autosetup -p1 -n dictknife-%{version}

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
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/dictknife
%python_alternative %{_bindir}/jsonknife
%python_alternative %{_bindir}/swaggerknife
%{python_sitelib}/dictknife
%{python_sitelib}/dictknife-%{version}*-info

%changelog
