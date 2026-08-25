#
# spec file for package python-comfyui-workflow-templates
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

Name:           python-comfyui-workflow-templates
Version:        0.11.46
Release:        0
Summary:        ComfyUI workflow templates meta package
License:        MIT
URL:            https://github.com/Comfy-Org/workflow_templates
Source0:        https://files.pythonhosted.org/packages/source/c/comfyui_workflow_templates/comfyui_workflow_templates-%{version}.tar.gz
BuildRequires:  %{python_module comfyui-workflow-templates-core >= 0.3.320}
BuildRequires:  %{python_module comfyui-workflow-templates-json >= 0.1.55}
BuildRequires:  %{python_module comfyui-workflow-templates-media-api >= 0.3.84}
BuildRequires:  %{python_module comfyui-workflow-templates-media-assets-01 >= 0.1.33}
BuildRequires:  %{python_module comfyui-workflow-templates-media-image >= 0.3.160}
BuildRequires:  %{python_module comfyui-workflow-templates-media-other >= 0.3.229}
BuildRequires:  %{python_module comfyui-workflow-templates-media-video >= 0.3.101}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Upstream pins the bundles with '==', but that is a release-train lockfile,
# not an API constraint: this package's only code imports five stable helpers
# from -core, and the bundles are additive asset stores. The real requirement
# is one-directional -- a bundle older than the manifest core ships means a
# missing asset -- so a floor expresses it exactly, while '=' additionally
# forbids the harmless newer direction and makes this package uninstallable
# on every independent bundle release.
Requires:       python-comfyui-workflow-templates-core >= 0.3.320
Requires:       python-comfyui-workflow-templates-json >= 0.1.55
Requires:       python-comfyui-workflow-templates-media-api >= 0.3.84
Requires:       python-comfyui-workflow-templates-media-assets-01 >= 0.1.33
Requires:       python-comfyui-workflow-templates-media-image >= 0.3.160
Requires:       python-comfyui-workflow-templates-media-other >= 0.3.229
Requires:       python-comfyui-workflow-templates-media-video >= 0.3.101
BuildArch:      noarch
%python_subpackages

%description
Meta package that re-exports the ComfyUI workflow template helpers
and pulls in the core, JSON and media asset bundles at the versions
this release is pinned to.

%prep
%autosetup -p1 -n comfyui_workflow_templates-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/comfyui_workflow_templates
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import comfyui_workflow_templates"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/comfyui_workflow_templates
%{python_sitelib}/comfyui_workflow_templates-%{version}.dist-info

%changelog
