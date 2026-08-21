#
# spec file for package python-comfyui-embedded-docs
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

Name:           python-comfyui-embedded-docs
Version:        0.5.10
Release:        0
Summary:        Embedded documentation for ComfyUI nodes
License:        GPL-3.0-only
URL:            https://github.com/Comfy-Org/embedded-docs
Source0:        https://files.pythonhosted.org/packages/source/c/comfyui_embedded_docs/comfyui_embedded_docs-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Localized Markdown documentation and images for ComfyUI built-in
nodes, consumed by the ComfyUI frontend help pages.

%prep
%autosetup -p1 -n comfyui_embedded_docs-%{version}
# sdist ships many documentation files mode 0755
find . -type f -exec chmod a-x {} +

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/comfyui_embedded_docs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import comfyui_embedded_docs"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/comfyui_embedded_docs
%{python_sitelib}/comfyui_embedded_docs-%{version}.dist-info

%changelog
