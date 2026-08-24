#
# spec file for package python-gguf
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
Name:           python-gguf
Version:        0.19.0
Release:        0
Summary:        Read and write ML models in GGUF for GGML
License:        MIT
URL:            https://github.com/ggml-org/llama.cpp
Source:         https://files.pythonhosted.org/packages/source/g/gguf/gguf-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module numpy >= 1.17}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module requests >= 2.25}
BuildRequires:  %{python_module tqdm >= 4.27}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-PyYAML >= 5.1
Requires:       python-numpy >= 1.17
Requires:       python-requests >= 2.25
Requires:       python-tqdm >= 4.27
BuildArch:      noarch
%python_subpackages

%description
Python library for reading and writing ML models in the GGUF (GGML
Universal File) format used by GGML-based inference engines such as
llama.cpp. It also ships command-line tools to dump metadata, edit
metadata values, copy a GGUF file with new metadata, and convert
endianness.

%prep
%autosetup -p1 -n gguf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Library modules ship an env shebang; they are not entry points.
# Strip the shebang and the executable bit so they are not treated
# as scripts.
%python_expand sed -i '1s|^#!.*||' %{buildroot}%{$python_sitelib}/gguf/scripts/*.py
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/gguf/scripts/*.py
# The gguf-editor-gui extra requires PySide6, which is not in Factory.
# Drop the entry point so the package does not ship a non-functional GUI.
rm -f %{buildroot}%{_bindir}/gguf-editor-gui
%python_expand rm -f %{buildroot}%{_bindir}/gguf-editor-gui-%{$python_bin_suffix}
%python_expand sed -i '/^gguf-editor-gui/d' %{buildroot}%{$python_sitelib}/gguf-%{version}.dist-info/entry_points.txt
%python_clone -a %{buildroot}%{_bindir}/gguf-convert-endian
%python_clone -a %{buildroot}%{_bindir}/gguf-dump
%python_clone -a %{buildroot}%{_bindir}/gguf-new-metadata
%python_clone -a %{buildroot}%{_bindir}/gguf-set-metadata
%python_group_libalternatives gguf-convert-endian
%python_group_libalternatives gguf-dump
%python_group_libalternatives gguf-new-metadata
%python_group_libalternatives gguf-set-metadata
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The PyPI sdist ships no tests (they live only in the llama.cpp git tree).
# Smoke-test the import and a writer/reader round-trip instead.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import gguf, os, tempfile, numpy; fd, p = tempfile.mkstemp(suffix='.gguf'); os.close(fd); w = gguf.GGUFWriter(p, 'llama'); w.add_uint32('answer', 42); w.add_tensor('tensor1', numpy.ones((32,), dtype=numpy.float32)); w.write_header_to_file(); w.write_kv_data_to_file(); w.write_tensors_to_file(); w.close(); r = gguf.GGUFReader(p); assert r.tensors[0].name == 'tensor1'; os.remove(p)"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} %{buildroot}%{_bindir}/gguf-dump-%{$python_bin_suffix} --help

%pre
%python_libalternatives_reset_alternative gguf-convert-endian
%python_libalternatives_reset_alternative gguf-dump
%python_libalternatives_reset_alternative gguf-new-metadata
%python_libalternatives_reset_alternative gguf-set-metadata

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/gguf-convert-endian
%python_alternative %{_bindir}/gguf-dump
%python_alternative %{_bindir}/gguf-new-metadata
%python_alternative %{_bindir}/gguf-set-metadata
%{python_sitelib}/gguf
%{python_sitelib}/gguf-%{version}.dist-info

%changelog
