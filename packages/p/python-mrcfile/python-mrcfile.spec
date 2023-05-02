#
# spec file for package python-mrcfile
#
# Copyright (c) 2023 SUSE LLC
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

Name:           python-mrcfile
Version:        1.4.3
Release:        0
Summary:        MRC file I/O library
License:        BSD-3-Clause
URL:            https://github.com/ccpem/mrcfile
Source:         https://github.com/ccpem/mrcfile/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.16.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-numpy >= 1.16.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
MRC file I/O library

%prep
%autosetup -p1 -n mrcfile-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mrcfile-header
%python_clone -a %{buildroot}%{_bindir}/mrcfile-validate
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_data_is_not_copied_unnecessarily: https://github.com/ccpem/mrcfile/issues/49
skip='test_data_is_not_copied_unnecessarily'
# test_data_is_not_read_if_dimensions_are_too_huge": https://github.com/ccpem/mrcfile/issues/53
skip="$skip or test_data_is_not_read_if_dimensions_are_too_huge"
%pytest -v -k "not ($skip)"

%post
%python_install_alternative mrcfile-header mrcfile-validate

%postun
%python_uninstall_alternative mrcfile-header

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/mrcfile-header
%python_alternative %{_bindir}/mrcfile-validate
%{python_sitelib}/mrcfile*

%changelog
