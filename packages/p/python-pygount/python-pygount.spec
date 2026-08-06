#
# spec file for package python-pygount
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


Name:           python-pygount
Version:        3.2.0
Release:        0
Summary:        Count source lines of code (SLOC) using pygments
License:        BSD-3-Clause
URL:            https://github.com/roskakori/pygount
Source:         https://files.pythonhosted.org/packages/source/p/pygount/pygount-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module GitPython >= 3.1}
BuildRequires:  %{python_module chardet >= 5}
BuildRequires:  %{python_module pygments >= 2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich >= 14}
# /SECTION
BuildRequires:  fdupes
Requires:       python-GitPython >= 3.1
Requires:       python-chardet >= 5
Requires:       python-pygments >= 2
Requires:       python-rich >= 14
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Pygount is a command line tool to scan folders for source code files and
count the number of source code lines in it. It is similar to tools like
[sloccount](https://www.dwheeler.com/sloccount/) and
[cloc](https://github.com/AlDanial/cloc) but uses the
[pygments](https://pygments.org/)
package to analyze the source code and consequently can analyze any
[programming language supported by pygments](https://pygments.org/languages/).

The name is a combination of pygments and count.

%prep
%autosetup -p1 -n pygount-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pygount
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Requires network
donttest="test_can_find_files_from_mixed_cloned_git_remote_url_and_local"
donttest+=" or test_can_extract_and_close_and_find_files_from_cloned_git_remote_url_with_revision"
donttest+=" or test_succeeds_on_not_git_extension"
%pytest -k "not ($donttest)"

%post
%python_install_alternative pygount

%postun
%python_uninstall_alternative pygount

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE.txt
%python_alternative %{_bindir}/pygount
%{python_sitelib}/pygount
%{python_sitelib}/pygount-%{version}.dist-info

%changelog
