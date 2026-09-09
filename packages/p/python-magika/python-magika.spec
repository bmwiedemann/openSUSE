#
# spec file for package python-magika
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


%bcond_without libalternatives
Name:           python-magika
Version:        1.0.3
Release:        0
Summary:        Python module for ML content-type detection
License:        Apache-2.0
URL:            https://github.com/google/magika
Source0:        https://files.pythonhosted.org/packages/source/m/magika/magika-%{version}.tar.gz
# PyPI sdist has no LICENSE file; text from the matching python-v tag
Source1:        https://raw.githubusercontent.com/google/magika/python-v%{version}/LICENSE
BuildRequires:  %{python_module click >= 8.1.7}
BuildRequires:  %{python_module hatchling}
# onnxruntime floors: 3.13 >= 1.21, 3.14 >= 1.24.1 (Factory 1.27 covers both)
BuildRequires:  %{python_module onnxruntime >= 1.21.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-click >= 8.1.7
Requires:       python-onnxruntime >= 1.21.0
BuildArch:      noarch
# python-onnxruntime is only built on these arches (source package
# onnxruntime); elsewhere this noarch package is unresolvable.
ExclusiveArch:  x86_64 aarch64
%python_subpackages

%description
Magika is an AI-powered file type detection tool. It uses a small
deep-learning model (a few MiB) to identify 200+ binary and textual
content types, typically within milliseconds on a single CPU.

This package provides the Python module and magika-python-client.
The primary magika command is the separate Rust CLI and is not
shipped here.

%prep
%autosetup -p1 -n magika-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
# /usr/bin/magika is the Rust CLI; the sdist stub only warns it is missing
%python_expand rm -f %{buildroot}%{_bindir}/magika %{buildroot}%{_bindir}/magika-%{$python_bin_suffix}
%python_clone -a %{buildroot}%{_bindir}/magika-python-client
%python_group_libalternatives magika-python-client
# modules are imported, not executed; drop env shebang + exec bit
%python_expand sed -i '1{/^#!/d}' %{buildroot}%{$python_sitelib}/magika/cli/*.py
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/magika/cli/*.py
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/magika
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# sdist has no monorepo tests_data/ fixtures; skip those tests and the 10GB one
donttest="test_magika_module_with_one_test_file"
donttest="$donttest or test_magika_module_with_explicit_model_dir"
donttest="$donttest or test_magika_module_with_basic_tests"
donttest="$donttest or test_magika_module_with_all_models"
donttest="$donttest or test_magika_module_with_previously_missdetected"
donttest="$donttest or test_magika_module_with_really_many_files"
donttest="$donttest or test_magika_module_with_big_file"
%pytest tests --ignore=tests/test_features_extraction_vs_reference.py --ignore=tests/test_inference_vs_reference.py -k "not ($donttest)"

%pre
%python_libalternatives_reset_alternative magika-python-client

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/magika-python-client
%{python_sitelib}/magika
%{python_sitelib}/magika-%{version}.dist-info

%changelog
