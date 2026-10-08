#
# spec file for package python-comfyui-workflow-templates-core
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

Name:           python-comfyui-workflow-templates-core
Version:        0.3.369
Release:        0
Summary:        Core helpers for ComfyUI workflow templates
# Legal-Review-Notice: sdist ships no LICENSE file; upstream
# Comfy-Org/workflow_templates is MIT
License:        MIT
URL:            https://github.com/Comfy-Org/workflow_templates
Source0:        https://files.pythonhosted.org/packages/source/c/comfyui_workflow_templates_core/comfyui_workflow_templates_core-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# The manifest pins a sha256 per asset and names the owning bundle, so its
# entries resolve only against these floors: without them 23 of the 608
# entries name assets no installed bundle provides. Upstream rewrites the
# index files when building the json sdist, so the 13 declared hashes for
# those never match any published json build (upstream defect, not fixable
# here) -- these floors are necessary, not sufficient.
Requires:       python-comfyui-workflow-templates-json >= 0.1.102
Requires:       python-comfyui-workflow-templates-media-assets-02 >= 0.1.9
BuildArch:      noarch
%python_subpackages

%description
Core helpers for ComfyUI workflow templates: manifest loading, asset
path resolution and metadata used by the media bundles and the
comfyui-workflow-templates meta package.

%prep
%autosetup -p1 -n comfyui_workflow_templates_core-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/comfyui_workflow_templates_core
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The sdist ships tests/, but every test resolves a REPO_ROOT three levels
# above the package and reads bundles.json / scripts/sync/, none of which are
# in the sdist -- so only an import smoke test is possible here.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import comfyui_workflow_templates_core"

%files %{python_files}
%{python_sitelib}/comfyui_workflow_templates_core
%{python_sitelib}/comfyui_workflow_templates_core-%{version}.dist-info

%changelog
