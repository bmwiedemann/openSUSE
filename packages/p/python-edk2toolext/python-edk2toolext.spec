#
# spec file for package python-edk2toolext
#
# Copyright (c) 2021 SUSE LLC
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

%define skip_python2 1

Name:           python-edk2toolext
Version:        0.14.0
Release:        0
Summary:	Tianocore Edk2 PyTool Extensions
License:        BSD-2-Clause-Patent
URL:            https://github.com/tianocore/edk2-pytool-extensions
Source:         https://files.pythonhosted.org/packages/source/e/edk2-pytool-extensions/edk2-pytool-extensions-%{version}.tar.gz
Group:          Development/Tools/Other
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  %{python_module py >= 1.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.2
Requires:       python-edk2toollib >= 0.10.13
Requires:       python-pefile >= 2019.4.18
Requires:       python-pyOpenSSL
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%python_subpackages

%description
Extensions to the edk2 build system allowing for a more robust and plugin based build system and tool execution environment

%prep
%setup -q -n edk2-pytool-extensions-%{version}
%autopatch -p1
dos2unix readme.md

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install

%python_clone -a %{buildroot}%{_bindir}/edk2_capsule_tool
%python_clone -a %{buildroot}%{_bindir}/firmware_policy_tool
%python_clone -a %{buildroot}%{_bindir}/nuget-publish
%python_clone -a %{buildroot}%{_bindir}/omnicache
%python_clone -a %{buildroot}%{_bindir}/sig_db_tool
%python_clone -a %{buildroot}%{_bindir}/stuart_build
%python_clone -a %{buildroot}%{_bindir}/stuart_ci_build
%python_clone -a %{buildroot}%{_bindir}/stuart_ci_setup
%python_clone -a %{buildroot}%{_bindir}/stuart_pr_eval
%python_clone -a %{buildroot}%{_bindir}/stuart_setup
%python_clone -a %{buildroot}%{_bindir}/stuart_update
%python_clone -a %{buildroot}%{_bindir}/versioninfo_tool

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative edk2_capsule_tool
%python_install_alternative firmware_policy_tool
%python_install_alternative nuget-publish
%python_install_alternative omnicache
%python_install_alternative sig_db_tool
%python_install_alternative stuart_build
%python_install_alternative stuart_ci_build
%python_install_alternative stuart_ci_setup
%python_install_alternative stuart_pr_eval
%python_install_alternative stuart_setup
%python_install_alternative stuart_update
%python_install_alternative versioninfo_tool

%postun
%python_uninstall_alternative edk2_capsule_tool
%python_uninstall_alternative firmware_policy_tool
%python_uninstall_alternative nuget-publish
%python_uninstall_alternative omnicache
%python_uninstall_alternative sig_db_tool
%python_uninstall_alternative stuart_build
%python_uninstall_alternative stuart_ci_build
%python_uninstall_alternative stuart_ci_setup
%python_uninstall_alternative stuart_pr_eval
%python_uninstall_alternative stuart_setup
%python_uninstall_alternative stuart_update
%python_uninstall_alternative versioninfo_tool

%files %{python_files}
%license LICENSE
%doc readme.md
%{python_sitelib}/*
%python_alternative %{_bindir}/edk2_capsule_tool
%python_alternative %{_bindir}/firmware_policy_tool
%python_alternative %{_bindir}/nuget-publish
%python_alternative %{_bindir}/omnicache
%python_alternative %{_bindir}/sig_db_tool
%python_alternative %{_bindir}/stuart_build
%python_alternative %{_bindir}/stuart_ci_build
%python_alternative %{_bindir}/stuart_ci_setup
%python_alternative %{_bindir}/stuart_pr_eval
%python_alternative %{_bindir}/stuart_setup
%python_alternative %{_bindir}/stuart_update
%python_alternative %{_bindir}/versioninfo_tool

%changelog
