#
# spec file for package python-huggingface-hub
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
Name:           python-huggingface-hub
Version:        1.24.0
Release:        0
Summary:        Client library for interaction with the huggingface hub
License:        Apache-2.0
URL:            https://github.com/huggingface/huggingface_hub
Source:         https://files.pythonhosted.org/packages/source/h/huggingface_hub/huggingface_hub-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module click >= 8.1.7}
BuildRequires:  %{python_module filelock >= 3.10.0}
BuildRequires:  %{python_module fsspec >= 2023.5.0}
BuildRequires:  %{python_module httpx >= 0.23.0}
BuildRequires:  %{python_module packaging >= 20.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm >= 4.42.1}
BuildRequires:  %{python_module typing-extensions >= 4.1.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.1
Requires:       python-click >= 8.1.7
Requires:       python-filelock >= 3.10.0
Requires:       python-fsspec >= 2023.5.0
Requires:       python-httpx >= 0.23.0
Requires:       python-packaging >= 20.9
Requires:       python-tqdm >= 4.42.1
Requires:       python-typing-extensions >= 4.1.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Client library to download and publish models, datasets and other repos on the huggingface.co hub

%prep
%setup -q -n huggingface_hub-%{version}
# hf-xet is the optional Rust Xet storage accelerator and is not packaged for
# openSUSE; huggingface_hub imports it lazily so it stays fully functional
# without it. Drop the hard dependency so the package remains installable.
sed -i '/HF_XET_VERSION/d' setup.py
# The click >= 8.4.2 pin only avoids a broken fish completion script shipped in
# 8.4.0/8.4.1; relax it to the click version available in the distribution.
sed -i 's/click>=8.4.2,<9.0.0/click>=8.1.7,<9.0.0/' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/hf
%python_clone -a %{buildroot}%{_bindir}/huggingface-cli
%python_clone -a %{buildroot}%{_bindir}/tiny-agents
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The upstream test suite talks to the Hugging Face Hub over the network, so it
# cannot run in the build environment. Restrict %%check to an import smoke test
# that exercises the freshly built package under every configured Python flavour.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import huggingface_hub"

%post
%python_install_alternative hf
%python_install_alternative huggingface-cli
%python_install_alternative tiny-agents

%postun
%python_uninstall_alternative hf
%python_uninstall_alternative huggingface-cli
%python_uninstall_alternative tiny-agents

%files %{python_files}
%python_alternative %{_bindir}/hf
%python_alternative %{_bindir}/huggingface-cli
%python_alternative %{_bindir}/tiny-agents
%{python_sitelib}/huggingface_hub
%{python_sitelib}/huggingface_hub-%{version}.dist-info

%changelog
