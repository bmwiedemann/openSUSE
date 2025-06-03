#
# spec file for package python-duckduckgo-search
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


%{?sle15_python_module_pythons}
Name:           python-duckduckgo-search
Version:        8.0.2
Release:        0
Summary:        Search using the DuckDuckGo.com search engine
License:        MIT
URL:            https://github.com/deedy5/duckduckgo_search
Source:         https://files.pythonhosted.org/packages/source/d/duckduckgo-search/duckduckgo_search-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module click >= 8.1.8}
BuildRequires:  %{python_module primp >= 0.15.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click >= 8.1.8
Requires:       python-lxml >= 5.3.0
Requires:       python-primp >= 0.15.0
Suggests:       python-mypy >= 1.14.1
Suggests:       python-pytest >= 8.3.4
Suggests:       python-pytest-dependency >= 0.6.0
Suggests:       python-ruff >= 0.9.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Search for words, documents, images, news, maps and text translation using the DuckDuckGo.com search engine. Downloading files and images to a local hard drive.

%prep
%autosetup -p1 -n duckduckgo_search-%{version}
chmod 0644 README.md
chmod 0644 LICENSE.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ddgs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# NOTE: disable running tests as they require internet access by making calls to
# https://duckduckgo.com

%post
%python_install_alternative ddgs

%postun
%python_uninstall_alternative ddgs

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/ddgs
%{python_sitelib}/duckduckgo_search
%{python_sitelib}/duckduckgo_search-%{version}.dist-info

%changelog
