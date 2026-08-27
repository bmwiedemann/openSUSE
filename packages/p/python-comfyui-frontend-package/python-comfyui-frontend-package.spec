#
# spec file for package python-comfyui-frontend-package
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

Name:           python-comfyui-frontend-package
Version:        1.51.9
Release:        0
Summary:        Official ComfyUI frontend as a Python package
# Legal-Review-Notice: sdist ships no LICENSE file; upstream
# Comfy-Org/ComfyUI_frontend declares GPL-3.0-only in package.json
License:        GPL-3.0-only
URL:            https://github.com/Comfy-Org/ComfyUI_frontend
Source0:        https://files.pythonhosted.org/packages/source/c/comfyui_frontend_package/comfyui_frontend_package-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Official ComfyUI frontend static assets (HTML, JavaScript, CSS and
related files) shipped as a Python package for installation next to
the ComfyUI backend.

%prep
%autosetup -p1 -n comfyui_frontend_package-%{version}

%build
# setup.py reads the release from this env var (else 0.1.0)
export COMFYUI_FRONTEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/comfyui_frontend_package
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import comfyui_frontend_package"

%files %{python_files}
%doc README.md
%{python_sitelib}/comfyui_frontend_package
%{python_sitelib}/comfyui_frontend_package-%{version}.dist-info

%changelog
