#
# spec file for package comfyui
#
# Copyright (c) 2026 SUSE LLC
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


# Single-flavour application (not an importable multi-flavour library).
# Follow %%{primary_python} so the interpreter tracks the distro primary.
%define pythons %{primary_python}
Name:           comfyui
Version:        0.33.3
Release:        0
Summary:        Modular node-graph engine for local AI content creation
License:        GPL-3.0-only
URL:            https://github.com/Comfy-Org/ComfyUI
Source0:        https://github.com/Comfy-Org/ComfyUI/archive/refs/tags/v%{version}.tar.gz#/ComfyUI-%{version}.tar.gz
Source1:        comfyui.sh
Source2:        comfyui-packaged-paths.yaml
# PATCH-FIX-UPSTREAM comfyui-create-custom-nodes-directory.patch gh#Comfy-Org/ComfyUI#8110 gh#Comfy-Org/ComfyUI#8434 mpluskal@suse.com -- create custom_nodes under --base-directory, main.py lists it before the server starts
Patch0:         comfyui-create-custom-nodes-directory.patch
# PATCH-FIX-UPSTREAM comfyui-fall-back-to-cpu-without-accelerator.patch mpluskal@suse.com -- start on the CPU when no accelerator is present, instead of raising AssertionError while importing
Patch1:         comfyui-fall-back-to-cpu-without-accelerator.patch
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Runtime stack. Cone packages (torchsde/vision/audio, comfy-*,
# comfyui-frontend-package, …) may still be unpublished; Requires stay
# honest so the package is unresolvable until they land.
Requires:       %{primary_python}-Pillow
Requires:       %{primary_python}-PyYAML
Requires:       %{primary_python}-SQLAlchemy >= 2.0.0
Requires:       %{primary_python}-aiohttp >= 3.11.8
Requires:       %{primary_python}-alembic
Requires:       %{primary_python}-av >= 16.0.0
Requires:       %{primary_python}-blake3
Requires:       %{primary_python}-comfy-aimdo = 0.4.14
Requires:       %{primary_python}-comfy-kitchen = 0.2.31
Requires:       %{primary_python}-comfyui-embedded-docs >= 0.5.9
Requires:       %{primary_python}-comfyui-frontend-package = 1.50.6
Requires:       %{primary_python}-comfyui-workflow-templates = 0.11.44
Requires:       %{primary_python}-einops
Requires:       %{primary_python}-filelock
Requires:       %{primary_python}-numpy >= 1.25.0
Requires:       %{primary_python}-psutil
Requires:       %{primary_python}-pydantic >= 2
Requires:       %{primary_python}-pydantic-settings >= 2
Requires:       %{primary_python}-requests
Requires:       %{primary_python}-safetensors >= 0.4.2
Requires:       %{primary_python}-scipy
Requires:       %{primary_python}-sentencepiece
Requires:       %{primary_python}-simpleeval >= 1.0.0
Requires:       %{primary_python}-tokenizers >= 0.13.3
Requires:       %{primary_python}-torch
Requires:       %{primary_python}-torchaudio
Requires:       %{primary_python}-torchsde
Requires:       %{primary_python}-torchvision
Requires:       %{primary_python}-tqdm
Requires:       %{primary_python}-transformers >= 4.50.3
Requires:       %{primary_python}-yarl >= 1.18.0
# Non-essential extras (kornia/spandrel/comfy-angle/opengl): missing
# optional modules must not block installing the tool.
Recommends:     %{primary_python}-comfy-angle
Recommends:     %{primary_python}-kornia >= 0.7.1
Recommends:     %{primary_python}-opengl >= 3.1.8
Recommends:     %{primary_python}-spandrel
BuildArch:      noarch

%description
ComfyUI is a node-graph engine for local AI content creation. Workflows
are assembled from nodes that load diffusion models, encoders, LoRAs and
other assets, and can produce images, video, audio and 3D output. A local
HTTP API and a browser UI are included.

The packaged tree is read-only. Models, custom nodes, input, output, temp
and user state live under the per-user --base-directory (default:
$XDG_DATA_HOME/comfyui or ~/.local/share/comfyui); the custom nodes shipped
with ComfyUI itself are loaded from the package tree as well.
ComfyUI-Manager is not enabled.

%prep
%autosetup -p1 -n ComfyUI-%{version}

%build
# ComfyUI has no [build-system] and is not a pip-installable library.
# Ship the application tree and a wrapper; do not %%pyproject_wheel it.

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/comfyui
cp -a . %{buildroot}%{_datadir}/comfyui
# Drop VCS/CI/tests and per-user writable state (models/output/input/user/temp
# belong under --base-directory). LICENSE/README/example yaml go to %%doc.
rm -rf %{buildroot}%{_datadir}/comfyui/.ci \
       %{buildroot}%{_datadir}/comfyui/.github \
       %{buildroot}%{_datadir}/comfyui/.coderabbit.yaml \
       %{buildroot}%{_datadir}/comfyui/.gitattributes \
       %{buildroot}%{_datadir}/comfyui/.gitignore \
       %{buildroot}%{_datadir}/comfyui/.spectral.yaml \
       %{buildroot}%{_datadir}/comfyui/tests \
       %{buildroot}%{_datadir}/comfyui/tests-unit \
       %{buildroot}%{_datadir}/comfyui/pytest.ini \
       %{buildroot}%{_datadir}/comfyui/models \
       %{buildroot}%{_datadir}/comfyui/output \
       %{buildroot}%{_datadir}/comfyui/input \
       %{buildroot}%{_datadir}/comfyui/user \
       %{buildroot}%{_datadir}/comfyui/temp \
       %{buildroot}%{_datadir}/comfyui/CODEOWNERS \
       %{buildroot}%{_datadir}/comfyui/AGENTS.md
rm -f %{buildroot}%{_datadir}/comfyui/LICENSE \
      %{buildroot}%{_datadir}/comfyui/README.md \
      %{buildroot}%{_datadir}/comfyui/CONTRIBUTING.md \
      %{buildroot}%{_datadir}/comfyui/extra_model_paths.yaml.example \
      %{buildroot}%{_datadir}/comfyui/blueprints/put_blueprints_here
# Modules are imported, not executed: strip leftover shebangs and +x.
find %{buildroot}%{_datadir}/comfyui -type f -name '*.py' \
     -exec sed -i '1{/^#!/d}' {} +
find %{buildroot}%{_datadir}/comfyui -type f -exec chmod a-x {} +
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{_datadir}/comfyui
sed -e 's|@@PYTHON@@|%{_bindir}/python3|g' \
    -e 's|@@DATADIR@@|%{_datadir}/comfyui|g' \
    %{SOURCE1} > %{buildroot}%{_bindir}/comfyui
chmod 0755 %{buildroot}%{_bindir}/comfyui
# --base-directory moves the custom_nodes search path into the user profile;
# register the packaged one as an additional path so both are loaded.
sed -e 's|@@DATADIR@@|%{_datadir}/comfyui|g' \
    %{SOURCE2} > %{buildroot}%{_datadir}/comfyui/comfyui-packaged-paths.yaml
%fdupes %{buildroot}%{_datadir}/comfyui

%check
# argparse --help is handled in comfy.cli_args at import and only needs
# stdlib plus the installed tree (no torch / unpublished cone packages).
# --quick-test-for-ci imports comfy_aimdo and torch; skip it until those
# BuildRequires resolve in this project.
sh -n %{buildroot}%{_bindir}/comfyui
%python_expand $python %{buildroot}%{_datadir}/comfyui/main.py --help
# The launcher must not touch the filesystem for a query-only invocation.
xdg=$(mktemp -d)
XDG_DATA_HOME="$xdg" sh %{buildroot}%{_bindir}/comfyui --help >/dev/null 2>&1 || :
test -z "$(ls -A "$xdg")"
rm -rf "$xdg"
# The extra search path must resolve to the packaged custom nodes.
grep -q '^  custom_nodes: %{_datadir}/comfyui/custom_nodes$' \
     %{buildroot}%{_datadir}/comfyui/comfyui-packaged-paths.yaml
test -f %{buildroot}%{_datadir}/comfyui/custom_nodes/websocket_image_save.py

%files
%license LICENSE
%doc README.md extra_model_paths.yaml.example
%{_bindir}/comfyui
%{_datadir}/comfyui

%changelog
