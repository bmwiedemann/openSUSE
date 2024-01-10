#
# spec file for package python-diff-match-patch
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


Name:           python-diff-match-patch
Version:        20230430
Release:        0
Summary:        Repackaging of Google's Diff Match and Patch libraries
License:        Apache-2.0
URL:            https://github.com/diff-match-patch-python/diff-match-patch
Source:         https://files.pythonhosted.org/packages/source/d/diff-match-patch/diff-match-patch-%{version}.tar.gz
# PATCH-FIX-OPENSUSE make-tests-runable.patch -- running tests is too complicated to put that into the specfile
Patch0:         make-tests-runable.patch
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-diff_match_patch
Obsoletes:      python-diff_match_patch
BuildArch:      noarch
%python_subpackages

%description
Offers algorithms to perform the operations required for synchronizing plain text

%prep
%autosetup -p1 -n diff-match-patch-%{version}
find . -name "*.py" -type f -exec sed -i '1s/^#!.*//' {} \+

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest diff_match_patch.tests.run_all

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/diff_match_patch
%{python_sitelib}/diff_match_patch-%{version}.dist-info

%changelog
