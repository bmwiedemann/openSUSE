#
# spec file for package python-parfive
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


%{?sle15_python_module_pythons}
Name:           python-parfive
Version:        2.2.0
Release:        0
Summary:        A HTTP and FTP parallel file downloader
License:        MIT
URL:            https://parfive.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/p/parfive/parfive-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Do not use return inside a finally block
Patch0:         support-python314.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module aioftp >= 0.17.1}
BuildRequires:  %{python_module aiofiles}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest-socket}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tqdm >= 4.27.0}
# /SECTION
Requires:       python-aiohttp
Requires:       python-tqdm
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-aiofiles
Recommends:     python-aioftp
BuildArch:      noarch

%python_subpackages

%description
Parfive is a library for downloading files, its objective is to
provide an API for queuing files for download and then providing
feedback to the user about the downloads in progress. It also
provides an interface for inspecting any failed downloads.

%prep
%autosetup -p1 -n parfive-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/parfive

%check
# Disable tests that require a network connection
%pytest -k 'not test_ftp and not test_ftp_http'

%post
%python_install_alternative parfive

%postun
%python_uninstall_alternative parfive

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/parfive
%{python_sitelib}/parfive-%{version}.dist-info
%python_alternative %{_bindir}/parfive

%changelog
