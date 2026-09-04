#
# spec file for package audible-cli
#
# Copyright (c) 2022 SUSE LLC
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


Name:           audible-cli
Version:        0.6.0
Release:        0
Summary:        Command line interface (cli) for the audible package
License:        AGPL-3.0-only
URL:            https://github.com/mkb79/audible-cli
Source:         https://github.com/mkb79/audible-cli/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module Pillow >= 12.3.0}
BuildRequires:  %{python_module aiofiles}
BuildRequires:  %{python_module audible >= 0.12.0}
BuildRequires:  %{python_module click >= 8.4.2}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module httpx >= 0.27.2}
BuildRequires:  %{python_module packaging >= 26.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module questionary >= 2.1.1}
BuildRequires:  %{python_module tabulate >= 0.10.0}
BuildRequires:  %{python_module toml >= 0.10.2}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 12.3.0
Requires:       python-aiofiles
Requires:       python-audible >= 0.12.0
Requires:       python-click >= 8.4.2
Requires:       python-httpx >= 0.27.2
Requires:       python-packaging >= 26.2
Requires:       python-questionary >= 2.1.1
Requires:       python-tabulate >= 0.10.0
Requires:       python-toml >= 0.10.2
Requires:       python-tqdm
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-colorama >= 0.4.6
BuildArch:      noarch
%python_subpackages

%description
A command line interface for audible package. With the cli you can download your Audible books, cover, chapter files.

%prep
%setup -q -n audible-cli-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/audible
%python_clone -a %{buildroot}%{_bindir}/audible-quickstart
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative audible audible-quickstart

%postun
%python_uninstall_alternative audible

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/audible
%python_alternative %{_bindir}/audible-quickstart
%{python_sitelib}/audible_cli*

%changelog
