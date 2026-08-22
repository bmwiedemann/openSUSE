#
# spec file for package python-datasets
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
Name:           python-datasets
Version:        5.0.1
Release:        0
Summary:        HuggingFace community-driven open-source library of datasets
License:        Apache-2.0
URL:            https://github.com/huggingface/datasets
Source:         https://files.pythonhosted.org/packages/source/d/datasets/datasets-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module dill >= 0.3.0}
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module fsspec >= 2023.1.0}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module huggingface-hub >= 0.25.0}
BuildRequires:  %{python_module multiprocess}
BuildRequires:  %{python_module numpy >= 1.17}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyarrow >= 21.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.32.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm >= 4.66.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xxhash}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-PyYAML >= 5.1
# aiohttp is not a direct install_requires as of 3.6.0, but fsspec[http] needs it
Requires:       python-aiohttp
Requires:       python-dill >= 0.3.0
Requires:       python-filelock
Requires:       python-fsspec >= 2023.1.0
Requires:       python-httpx
Requires:       python-huggingface-hub >= 0.25.0
Requires:       python-multiprocess
Requires:       python-numpy >= 1.17
Requires:       python-packaging
Requires:       python-pandas
Requires:       python-pyarrow >= 21.0.0
Requires:       python-requests >= 2.32.2
Requires:       python-tqdm >= 4.66.3
Requires:       python-xxhash
Suggests:       python-Pillow >= 9.4.0
Suggests:       python-SQLAlchemy
Suggests:       python-torch
Suggests:       python-zstandard
BuildArch:      noarch
%python_subpackages

%description
HuggingFace community-driven open-source library of datasets.
It provides one-line dataloaders for many public datasets and
efficient data pre-processing for audio, vision and NLP tasks.

%prep
%autosetup -p1 -n datasets-%{version}
# Library modules are not entry points; drop env shebangs so rpmlint
# does not treat them as scripts. The datasets-cli wrapper is generated.
sed -i '1{/^#!/d}' src/datasets/commands/datasets_cli.py \
    src/datasets/utils/_filelock.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/datasets-cli
%python_group_libalternatives datasets-cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The PyPI sdist omits tests/utils.py, tests/conftest.py, tests/fixtures/
# and tests/{features,io,packaged_modules,commands}/ (those live only in
# the GitHub tree). Modules that "from .utils import ..." cannot collect.
# Skip hub/S3/network tests. A Dataset.map + pickle smoke test covers the
# Python 3.14 Pickler._batch_setitems regression fixed in 4.4.0.
export HF_HUB_OFFLINE=1
export HF_DATASETS_OFFLINE=1
export HF_HOME=%{_tmppath}/hf-home-%{name}
mkdir -p "$HF_HOME"
%pytest tests/test_buckets.py tests/test_dataset_list.py tests/test_exceptions.py tests/test_experimental.py tests/test_filelock.py tests/test_info.py tests/test_info_utils.py tests/test_metadata_util.py tests/test_sharding_utils.py tests/test_splits.py tests/test_tqdm.py tests/test_version.py
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c 'from datasets import Dataset; import pickle; ds = Dataset.from_dict({"n": list(range(32))}); m = ds.map(lambda x: {"n": x["n"] + 1}); assert m[0]["n"] == 1; assert pickle.loads(pickle.dumps(ds))[7]["n"] == 7; assert m._fingerprint != ds._fingerprint'

%pre
%python_libalternatives_reset_alternative datasets-cli

%files %{python_files}
%doc AUTHORS README.md
%license LICENSE
%python_alternative %{_bindir}/datasets-cli
%{python_sitelib}/datasets
%{python_sitelib}/datasets-%{version}.dist-info

%changelog
