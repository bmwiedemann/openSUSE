#
# spec file for package python-pipreqs
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-pipreqs
Version:        0.5.0
Release:        0
Summary:        Pip requirements generator based on imports in project
License:        Apache-2.0
URL:            https://github.com/bndr/pipreqs
Source:         https://github.com/bndr/pipreqs/archive/refs/tags/v%{version}.tar.gz#/pipreqs-%{version}-gh.tar.gz
Patch1:         allow-newer-python.patch
BuildRequires:  %{python_module ipython >= 8.12.3}
BuildRequires:  %{python_module nbconvert >= 7.11.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docopt
Requires:       python-ipython >= 8.12.3
Requires:       python-nbconvert >= 7.11.0
Requires:       python-yarg
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module ipython >= 8.12.3}
BuildRequires:  %{python_module nbconvert >= 7.11.0}
BuildRequires:  %{python_module yarg}
# /SECTION
%python_subpackages

%description
Pip requirements.txt generator based on imports in project.

%prep
%autosetup -p1 -n pipreqs-%{version}
chmod a-x pipreqs/pipreqs.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pipreqs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Ignore tests that require network access
%pytest -k 'not (test_get_imports_info or test_ignored_directory or test_init or test_init_overwrite or teset_init_savepath or test_omit_version or test_clean or test_dynamic_version or test_output_requirements or test_pipreqs_get_imports_from_pyw_file)'

%post
%python_install_alternative pipreqs

%postun
%python_uninstall_alternative pipreqs

%pre
%python_libalternatives_reset_alternative pipreqs

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/pipreqs
%{python_sitelib}/pipreqs
%{python_sitelib}/pipreqs-%{version}.dist-info

%changelog
