#
# spec file for package python-comfyui-workflow-templates-media-assets-01
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

Name:           python-comfyui-workflow-templates-media-assets-01
Version:        0.1.38
Release:        0
Summary:        ComfyUI workflow template media assets bundle 01
# Legal-Review-Notice: sdist ships no LICENSE file; upstream
# Comfy-Org/workflow_templates is MIT
License:        MIT
URL:            https://github.com/Comfy-Org/workflow_templates
Source0:        https://files.pythonhosted.org/packages/source/c/comfyui_workflow_templates_media_assets_01/comfyui_workflow_templates_media_assets_01-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Media assets bundle 01 for ComfyUI workflow templates.

%prep
%autosetup -p1 -n comfyui_workflow_templates_media_assets_01-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/comfyui_workflow_templates_media_assets_01
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import comfyui_workflow_templates_media_assets_01"

%files %{python_files}
%{python_sitelib}/comfyui_workflow_templates_media_assets_01
%{python_sitelib}/comfyui_workflow_templates_media_assets_01-%{version}.dist-info

%changelog
