#
# spec file for package python-edk2toolext
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
Name:           python-edk2toolext
Version:        0.31.1
Release:        0
Summary:        Tianocore Edk2 PyTool Extensions
License:        BSD-2-Clause-Patent
URL:            https://github.com/tianocore/edk2-pytool-extensions
Source:         https://github.com/tianocore/edk2-pytool-extensions/archive/refs/tags/v%{version}.tar.gz#/edk2-pytool-extensions-%{version}.tar.gz
# PATCH-FIX-OPENSUSE include submodules when building wheels
Patch0:         include-submodules.patch
# PATCH-FIX-OPENSUSE use sys.executable in the testsuite, not "python"
Patch1:         do-not-use-bare-python.patch
BuildRequires:  %{python_module GitPython >= 3.1.30}
BuildRequires:  %{python_module PyYAML >= 6.0}
BuildRequires:  %{python_module XlsxWriter >= 3.0.9}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module edk2toollib >= 0.23.10}
BuildRequires:  %{python_module openpyxl >= 3.1.2}
BuildRequires:  %{python_module pefile >= 2023.2.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module semantic_version >= 2.10}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-GitPython >= 3.1.30
Requires:       python-PyYAML >= 6.0
Requires:       python-XlsxWriter >= 3.0.9
Requires:       python-edk2toollib >= 0.23.10
Requires:       python-openpyxl >= 3.1.2
Requires:       python-pefile >= 2023.2.7
Requires:       python-semantic_version >= 2.10
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%python_subpackages

%description
Extensions to the edk2 build system allowing for a more robust and plugin based build system and tool execution environment

%prep
%autosetup -p1 -n edk2-pytool-extensions-%{version}
dos2unix readme.md

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/edk2_capsule_tool
%python_clone -a %{buildroot}%{_bindir}/firmware_policy_tool
%python_clone -a %{buildroot}%{_bindir}/fpdt_parser
%python_clone -a %{buildroot}%{_bindir}/nuget-publish
%python_clone -a %{buildroot}%{_bindir}/omnicache
%python_clone -a %{buildroot}%{_bindir}/patch_var_store_tool
%python_clone -a %{buildroot}%{_bindir}/perf_report_generator
%python_clone -a %{buildroot}%{_bindir}/sig_db_tool
%python_clone -a %{buildroot}%{_bindir}/statuscode_processor
%python_clone -a %{buildroot}%{_bindir}/stuart_build
%python_clone -a %{buildroot}%{_bindir}/stuart_ci_build
%python_clone -a %{buildroot}%{_bindir}/stuart_ci_setup
%python_clone -a %{buildroot}%{_bindir}/stuart_pr_eval
%python_clone -a %{buildroot}%{_bindir}/stuart_setup
%python_clone -a %{buildroot}%{_bindir}/stuart_update
%python_clone -a %{buildroot}%{_bindir}/versioninfo_tool
%python_clone -a %{buildroot}%{_bindir}/secureboot_audit
%python_clone -a %{buildroot}%{_bindir}/stuart_parse
%python_clone -a %{buildroot}%{_bindir}/stuart_report
%python_clone -a %{buildroot}%{_bindir}/validate_image_tool

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_flavored_alternatives
# Requires network
donttest="TestNugetDependency or test_nuget_publish "
donttest+="or test_bad_ext_dep or test_duplicate_ext_deps_skip_dir "
donttest+="or test_multiple_duplicate_ext_deps_skip_dir "
donttest+="or test_multiple_extdeps or test_one_level_recursive "
donttest+="or test_sha256_ or test_single_file or test_unpack_zip_file_attr "
donttest+="or test_log_error_on_missing_host_specific_folder "
donttest+="or test_can_download_nuget or test_omnicache_convert "
donttest+="or test_omnicache_fetch "
ignore="--ignore tests.unit/test_edk2_setup.py "
ignore+="--ignore tests.unit/test_git_dependency.py "
ignore+="--ignore tests.unit/test_repo_resolver.py"
# Requires azure-cli
donttest+="or test_az_tool_environment "
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -Bm pytest $ignore -k "not ($donttest)"
}

%post
%python_install_alternative edk2_capsule_tool
%python_install_alternative firmware_policy_tool
%python_install_alternative fpdt_parser
%python_install_alternative nuget-publish
%python_install_alternative omnicache
%python_install_alternative patch_var_store_tool
%python_install_alternative perf_report_generator
%python_install_alternative sig_db_tool
%python_install_alternative statuscode_processor
%python_install_alternative stuart_build
%python_install_alternative stuart_ci_build
%python_install_alternative stuart_ci_setup
%python_install_alternative stuart_pr_eval
%python_install_alternative stuart_setup
%python_install_alternative stuart_update
%python_install_alternative versioninfo_tool
%python_install_alternative secureboot_audit
%python_install_alternative stuart_parse
%python_install_alternative stuart_report
%python_install_alternative validate_image_tool

%postun
%python_uninstall_alternative edk2_capsule_tool
%python_uninstall_alternative firmware_policy_tool
%python_uninstall_alternative fpdt_parser
%python_uninstall_alternative nuget-publish
%python_uninstall_alternative omnicache
%python_uninstall_alternative patch_var_store_tool
%python_uninstall_alternative perf_report_generator
%python_uninstall_alternative sig_db_tool
%python_uninstall_alternative statuscode_processor
%python_uninstall_alternative stuart_build
%python_uninstall_alternative stuart_ci_build
%python_uninstall_alternative stuart_ci_setup
%python_uninstall_alternative stuart_pr_eval
%python_uninstall_alternative stuart_setup
%python_uninstall_alternative stuart_update
%python_uninstall_alternative versioninfo_tool
%python_uninstall_alternative secureboot_audit
%python_uninstall_alternative stuart_parse
%python_uninstall_alternative stuart_report
%python_uninstall_alternative validate_image_tool

%files %{python_files}
%license LICENSE
%doc readme.md
%{python_sitelib}/edk2toolext
%{python_sitelib}/edk2_pytool_extensions-%{version}.dist-info
%python_alternative %{_bindir}/edk2_capsule_tool
%python_alternative %{_bindir}/firmware_policy_tool
%python_alternative %{_bindir}/fpdt_parser
%python_alternative %{_bindir}/nuget-publish
%python_alternative %{_bindir}/omnicache
%python_alternative %{_bindir}/patch_var_store_tool
%python_alternative %{_bindir}/perf_report_generator
%python_alternative %{_bindir}/sig_db_tool
%python_alternative %{_bindir}/statuscode_processor
%python_alternative %{_bindir}/stuart_build
%python_alternative %{_bindir}/stuart_ci_build
%python_alternative %{_bindir}/stuart_ci_setup
%python_alternative %{_bindir}/stuart_pr_eval
%python_alternative %{_bindir}/stuart_setup
%python_alternative %{_bindir}/stuart_update
%python_alternative %{_bindir}/versioninfo_tool
%python_alternative %{_bindir}/secureboot_audit
%python_alternative %{_bindir}/stuart_parse
%python_alternative %{_bindir}/stuart_report
%python_alternative %{_bindir}/validate_image_tool

%changelog
