#
# spec file for package python-diff_match_patch
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


Name:           python-diff_match_patch
Version:        20181111
Release:        0
Summary:        Python Diff, Match and Patch library for Plain Text
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/diff-match-patch-python/diff-match-patch
Source:         https://files.pythonhosted.org/packages/source/d/diff-match-patch/diff-match-patch-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Repackaging of Google's Diff Match and Patch libraries. Offers robust algorithms
to perform the operations required for synchronizing plain text

%prep

%setup -q -n diff-match-patch-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest -v diff_match_patch.tests

%files %{python_files}
%{python_sitelib}/diff_match_patch
%{python_sitelib}/diff_match_patch-%{version}-py%{py_ver}.egg-info

%changelog
