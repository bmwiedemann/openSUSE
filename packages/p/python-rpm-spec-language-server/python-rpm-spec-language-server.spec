#
# spec file for package python-rpm-spec-language-server
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define skip_python39 1
%define skip_python310 1
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-rpm-spec-language-server
Version:        0.0.2
Release:        0
Summary:        Language Server for RPM spec files
License:        GPL-2.0-or-later
URL:            https://github.com/dcermak/rpm-spec-language-server
# Source:         https://files.pythonhosted.org/packages/source/r/rpm-spec-language-server/rpm_spec_language_server-%%{version}.tar.gz
Source:         rpm-spec-language-server-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
# SECTION test requirements
BuildRequires:  %{python_module lsprotocol}
BuildRequires:  %{python_module pygls}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module specfile}
BuildRequires:  %{python_module typeguard}
# /SECTION
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pygls
Requires:       python-requests
Requires:       python-specfile
Requires:       rpm
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
This is a proof of concept implementation of a server
implementing the Language Server Protocol for RPM Spec files.

%prep
%autosetup -p1 -n rpm-spec-language-server-%{version}

%build
%pyproject_wheel

%check
# Skip tests which require an internet connection
%pytest -k "not (upstream or test_cache_creation)"

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rpm_lsp_server
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative rpm_lsp_server

%postun
%python_uninstall_alternative rpm_lsp_server

%files %{python_files}
%python_alternative %{_bindir}/rpm_lsp_server
%{python_sitelib}/rpm_spec_language_server
%{python_sitelib}/rpm_spec_language_server-%{version}.dist-info

%changelog
