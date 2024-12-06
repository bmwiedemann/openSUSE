#
# spec file for package python-huggingface-hub
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
Name:           python-huggingface-hub
Version:        0.26.3
Release:        0
Summary:        Client library for interaction with the huggingface hub
License:        Apache-2.0
URL:            https://github.com/huggingface/huggingface_hub
Source:         https://github.com/huggingface/huggingface_hub/archive/refs/tags/v%{version}.tar.gz#/huggingface_hub-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module fsspec >= 2023.5.0}
BuildRequires:  %{python_module packaging >= 20.9}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm >= 4.42.1}
BuildRequires:  %{python_module typing-extensions >= 3.7.4.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.1
Requires:       python-filelock
Requires:       python-fsspec >= 2023.5.0
Requires:       python-packaging >= 20.9
Requires:       python-requests
Requires:       python-tqdm >= 4.42.1
Requires:       python-typing-extensions >= 3.7.4.3
BuildArch:      noarch
%python_subpackages

%description
Client library to download and publish models, datasets and other repos on the huggingface.co hub

%prep
%setup -q -n huggingface_hub-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/huggingface-cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative huggingface-cli

%postun
%python_uninstall_alternative huggingface-cli

%files %{python_files}
%python_alternative %{_bindir}/huggingface-cli
%{python_sitelib}/huggingface_hub
%{python_sitelib}/huggingface_hub-%{version}*info

%changelog
