#
# spec file for package python-awx-cli
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
Name:           python-awx-cli
Version:        24.6.1
Release:        0
Summary:        CLI for the AWX Ansible web platform
License:        Apache-2.0
URL:            https://github.com/ansible/awx/tree/devel/awxkit
Source:         awx-%{version}.tar.gz
Source1:        LICENSE.md
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
# SECTION
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module websocket-client}
# SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives

BuildArch:      noarch
%python_subpackages

%description
CLI to manage the AWX Ansible web platform

%prep
%autosetup -n awx-%{version}
cp %{SOURCE1} .
echo %{version} > VERSION

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/akit
%python_clone -a %{buildroot}%{_bindir}/awx
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative akit
%python_install_alternative awx

%postun
%python_uninstall_alternative akit
%python_uninstall_alternative awx

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/awxkit/
%{python_sitelib}/awxkit-%{version}.dist-info
%python_alternative %{_bindir}/akit
%python_alternative %{_bindir}/awx

%changelog
