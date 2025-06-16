#
# spec file for package python-trakit
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-trakit
Version:        0.2.2
Release:        0
Summary:        Guess additional information from track titles
License:        MIT
URL:            https://github.com/ratoaq2/trakit
Source0:        https://github.com/ratoaq2/trakit/archive/refs/tags/%{version}.tar.gz#/trakit-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
# TEST requirements
BuildRequires:  %{python_module PyYAML >= 6.0}
BuildRequires:  %{python_module Unidecode}
BuildRequires:  %{python_module babelfish >= 0.6.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rebulk >= 3.1.0}
# /TEST
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-babelfish >= 0.6.0
Requires:       python-rebulk >= 3.1.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-PyYAML >= 6.0
BuildArch:      noarch
%python_subpackages

%description
TrakIt is a track name parser created to solve a common, yet very specific
problem, that is vagueness in metadata information.

%prep
%autosetup -n trakit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/trakit
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_generate_config'

%post
%python_install_alternative trakit

%postun
%python_uninstall_alternative trakit

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/trakit
%{python_sitelib}/trakit
%{python_sitelib}/trakit-%{version}.dist-info

%changelog
