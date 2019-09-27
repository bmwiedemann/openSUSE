#
# spec file for package python-pip-tools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pip-tools
Version:        4.1.0
Release:        0
Summary:        Tool to keep pinned dependencies up to date
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/pip-tools/
Source:         https://files.pythonhosted.org/packages/source/p/pip-tools/pip-tools-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 6
Requires:       python-pip
Requires:       python-setuptools
Requires:       python-six
Requires:       python-wheel
Recommends:     git-core
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 6}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
pip-tools keeps pinned dependencies inside a project up to date.

%prep
%setup -q -n pip-tools-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# Skip internet tests https://github.com/jazzband/pip-tools/issues/887
# Also test_build_isolation_option and test_cert_option https://github.com/jazzband/pip-tools/issues/888
%pytest -k 'not (test_url_package or test_annotate_option or test_allow_unsafe_option or test_pre_option or test_editable_top_level_deps_preserved or test_editable_package or test_editable_package_vcs or test_generate_hashes_with_editable or test_generate_hashes_with_url or test_input_file_without_extension or test_generate_hashes_verbose or test_filter_pip_markers or test_no_candidates or test_no_candidates_pre or test_stdin or test_get_hashes_local_repository_cache_miss or test_generate_hashes_all_platforms or test_realistic_complex_sub_dependencies or test_locally_available_editable_package_is_not_archived_in_cache_dir or test_generate_hashes_without_interfering_with_each_other or test_build_isolation_option or test_cert_option)'

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%python3_only %{_bindir}/pip-compile
%python3_only %{_bindir}/pip-sync
%{python_sitelib}/*

%changelog
