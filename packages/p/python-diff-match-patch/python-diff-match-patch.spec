#
# spec file for package python-diff-match-patch
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-diff-match-patch
Version:        20200713
Release:        0
Summary:        Repackaging of Google's Diff Match and Patch libraries
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/diff-match-patch-python/diff-match-patch
Source:         https://files.pythonhosted.org/packages/source/d/diff-match-patch/diff-match-patch-%{version}.tar.gz
# PATCH-FIX-OPENSUSE make-tests-runable.patch -- running tests is too complicated to put that into the specfile
Patch0:         make-tests-runable.patch
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-diff_match_patch
Obsoletes:      python-diff_match_patch
BuildArch:      noarch
%python_subpackages

%description
Offers algorithms to perform the operations required for synchronizing plain text

%prep
%setup -q -n diff-match-patch-%{version}
find . -name "*.py" -type f -exec sed -i '1s/^#!.*//' {} \+
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest diff_match_patch.tests.run_all

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
