#
# spec file for package python-modelscope
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-modelscope
Version:        1.39.1
Release:        0
Summary:        ModelScope hub and library core (Model-as-a-Service SDK)
# Legal-Review-Notice: The sdist vendors non-free NVIDIA EG3D/StyleGAN
# (LicenseRef-NvidiaProprietary), Nvidia Source Code License-NC CUDA
# kernels, CC-BY-NC-4.0 StarGAN modules and an academic-NC dataset
# helper used only by optional cv/audio extras. Those files are deleted
# in %%prep and are not shipped. Remaining third-party snippets are MIT
# and BSD-3-Clause.
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            https://github.com/modelscope/modelscope
Source:         https://files.pythonhosted.org/packages/source/m/modelscope/modelscope-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module modelscope-hub >= 0.2.0}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.25}
BuildRequires:  %{python_module setuptools >= 69}
BuildRequires:  %{python_module tqdm >= 4.64.0}
BuildRequires:  %{python_module urllib3 >= 1.26}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-filelock
Requires:       python-modelscope-hub >= 0.2.0
Requires:       python-packaging
Requires:       python-requests >= 2.25
Requires:       python-setuptools
Requires:       python-tqdm >= 4.64.0
Requires:       python-urllib3 >= 1.26
# Optional extras (cv/nlp/audio/datasets) are huge and not enabled.
Suggests:       python-Pillow
Suggests:       python-datasets
Suggests:       python-transformers
BuildArch:      noarch
%python_subpackages

%description
ModelScope is a Model-as-a-Service SDK for browsing, downloading and
running models from ModelScope Hub. This package ships the hub/library
core only: the cv, nlp, audio and related extras are not required.
The modelscope and ms commands delegate to python-modelscope-hub.

%prep
%autosetup -p1 -n modelscope-%{version}
# Non-free NVIDIA EG3D/StyleGAN (LicenseRef-NvidiaProprietary)
rm -rf modelscope/models/cv/image_control_3d_portrait
rm -rf modelscope/ops/image_control_3d_portrait
# Nvidia Source Code License-NC CUDA kernels (and the loader that
# compiles them)
rm -rf modelscope/ops/human_image_generation
# CC-BY-NC-4.0 StarGAN modules and academic-NC dataset helper
rm -f modelscope/models/audio/ssr/models/Unet.py
rm -f modelscope/models/audio/vc/src/Starganv3.py
rm -f modelscope/msdatasets/dataset_cls/custom_datasets/language_guided_video_summarization_dataset.py

%build
%pyproject_wheel

%install
%pyproject_install
# Library modules ship env shebangs; they are not entry points.
%python_expand find %{buildroot}%{$python_sitelib}/modelscope -type f -name '*.py' -exec sed -i '1{/^#!/d}' {} +
# Optional extras ship C/CUDA kernels as package data (4knerf, ailut,
# quadtree_attention). They are not built here and trip
# devel-file-in-non-devel-package / spurious-executable-perm.
%{python_expand \
find %{buildroot}%{$python_sitelib}/modelscope -type f \( \
  -name '*.h' -o -name '*.hpp' -o -name '*.c' -o -name '*.cc' \
  -o -name '*.cpp' -o -name '*.cxx' -o -name '*.cu' -o -name '*.cuh' \) -delete
find %{buildroot}%{$python_sitelib}/modelscope -type f -exec chmod a-x {} +
}
%python_clone -a %{buildroot}%{_bindir}/modelscope
%python_clone -a %{buildroot}%{_bindir}/ms
%python_group_libalternatives modelscope
%python_group_libalternatives ms
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Full tests need network and downloaded models. import modelscope
# pulls modelscope_hub (mandatory).
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import modelscope, modelscope_hub; assert modelscope.__version__ == '%{version}'"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} %{buildroot}%{_bindir}/modelscope-%{$python_bin_suffix} --help

%pre
%python_libalternatives_reset_alternative modelscope
%python_libalternatives_reset_alternative ms

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/modelscope
%python_alternative %{_bindir}/ms
%{python_sitelib}/modelscope
%{python_sitelib}/modelscope-%{version}.dist-info

%changelog
