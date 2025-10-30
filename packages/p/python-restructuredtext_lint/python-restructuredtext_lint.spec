#
# spec file for package python-restructuredtext_lint
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-restructuredtext_lint
Version:        1.4.0
Release:        0
Summary:        Linter for reStructuredText
License:        Unlicense
Group:          Development/Languages/Python
URL:            https://github.com/twolfson/restructuredtext-lint
Source:         https://files.pythonhosted.org/packages/source/r/restructuredtext_lint/restructuredtext_lint-%{version}.tar.gz
# PATCH-FIX-UPSTREAM set-pub-at-inst.patch gh#twolfson/restructuredtext-lint!64 mcepl@suse.com
# make the package compatible with docutils 0.22
Patch0:         set-pub-at-inst.patch
# PATCH-FIX-OPENSUSE skip-failing-test-66.patch gh#twolfson/restructuredtext-lint#66 mcepl@suse.com
# skip failing test (upstream has more complex solution)
Patch1:         skip-failing-test-66.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-docutils >= 0.11
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module docutils >= 0.11}
# /SECTION
%python_subpackages

%description
Linter for reStructuredText.

This was created out of frustration with PyPI; it sucks finding out
your reST is invalid **after** uploading it. It is being developed
in junction with a Sublime Text linter.

%prep
%autosetup -p1 -n restructuredtext_lint-%{version}

find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rst-lint
%python_clone -a %{buildroot}%{_bindir}/restructuredtext-lint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m unittest discover -v
}

%pre
%python_libalternatives_reset_alternative rst-lint
%python_libalternatives_reset_alternative restructuredtext-lint

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license UNLICENSE
%python_alternative %{_bindir}/restructuredtext-lint
%python_alternative %{_bindir}/rst-lint
%{python_sitelib}/restructuredtext_lint
%{python_sitelib}/restructuredtext_lint-%{version}*-info

%changelog
