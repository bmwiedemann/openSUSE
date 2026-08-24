#
# spec file for package python-modelscope-hub
#
# Copyright (c) 2026 SUSE LLC
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-modelscope-hub
Version:        0.2.0
Release:        0
Summary:        Official Python client for ModelScope Hub
License:        Apache-2.0
URL:            https://github.com/modelscope/modelscope_hub
Source:         https://files.pythonhosted.org/packages/source/m/modelscope_hub/modelscope_hub-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module filelock >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.28}
BuildRequires:  %{python_module responses >= 0.20}
BuildRequires:  %{python_module setuptools >= 68.0}
BuildRequires:  %{python_module tqdm >= 4.64.0}
BuildRequires:  %{python_module urllib3 >= 1.26}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  timezone
Requires:       alts
Requires:       python-filelock >= 3.9
Requires:       python-requests >= 2.28
Requires:       python-tqdm >= 4.64.0
Requires:       python-urllib3 >= 1.26
BuildArch:      noarch
%python_subpackages

%description
Python SDK and CLI to download, upload and manage models, datasets,
Studio spaces, skills and MCP servers on ModelScope Hub. Provides a
HubApi class and the modelscope-hub and ms-hub commands.

%prep
%autosetup -p1 -n modelscope_hub-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/modelscope-hub
%python_clone -a %{buildroot}%{_bindir}/ms-hub
%python_group_libalternatives modelscope-hub
%python_group_libalternatives ms-hub
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Offline mock-mode tests (HTTP mocked with responses). Skip @remote
# tests that need live Hub credentials.
%pytest -m "not remote"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import modelscope_hub"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} %{buildroot}%{_bindir}/ms-hub-%{$python_bin_suffix} --help

%pre
%python_libalternatives_reset_alternative modelscope-hub
%python_libalternatives_reset_alternative ms-hub

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/modelscope-hub
%python_alternative %{_bindir}/ms-hub
%{python_sitelib}/modelscope_hub
%{python_sitelib}/modelscope_hub-%{version}.dist-info

%changelog
