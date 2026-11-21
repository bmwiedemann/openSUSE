#
# spec file for package python-awx-cli
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
Name:           python-awx-cli
Version:        24.6.1
Release:        0
Summary:        CLI for the AWX Ansible web platform
License:        Apache-2.0
URL:            https://github.com/ansible/awx/tree/devel/awxkit
Source:         awx-%{version}.tar.gz
Source1:        LICENSE.md
# PATCH-FIX-UPSTREAM awxkit-drop-distutils-pkg_resources.patch gh#ansible/awx#15441 gh#ansible/awx#16208
Patch0:         awxkit-drop-distutils-pkg_resources.patch
# PATCH-FIX-UPSTREAM awxkit-argparse-python313.patch gh#ansible/awx#15692
Patch1:         awxkit-argparse-python313.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
# SECTION
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module websocket-client}
# SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-packaging
Requires:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives

BuildArch:      noarch
%python_subpackages

%description
CLI to manage the AWX Ansible web platform

%prep
%autosetup -p1 -n awx-%{version}
cp %{SOURCE1} .
echo %{version} > VERSION

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/akit
%python_clone -a %{buildroot}%{_bindir}/awx
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the CLI must start: no distutils / pkg_resources, argparse on python >= 3.12.8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c 'import awxkit.awx, awxkit.cli.options; from awxkit.cli import run; run(argv=["awx", "--version"])'

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
