#
# spec file for package python-binaryornot
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
# Tests run too slowly on some architectures
%ifarch %{ix86} x86_64  ppc64 ppc64le
%bcond_without  test
%else
%bcond_with     test
%endif
Name:           python-binaryornot
Version:        0.6.0
Release:        0
Summary:        Python package to check if a file is binary or text
License:        MIT
URL:            https://github.com/audreyr/binaryornot
Source:         https://files.pythonhosted.org/packages/source/b/binaryornot/binaryornot-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
Pure Python package to guess whether a file is binary or text.
It uses three layers of detection:
1. Extension check: Recognizes 131 file types by name for instant classification.
2. File signatures: Checks headers against known magic-byte signatures.
3. Content analysis: Uses a trained decision tree for statistical classification.

%prep
%autosetup -p1 -n binaryornot-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/binaryornot
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python tests/test_check.py
}
%endif

%post
%python_install_alternative binaryornot

%postun
%python_uninstall_alternative binaryornot

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/binaryornot
%{python_sitelib}/binaryornot
%{python_sitelib}/binaryornot-%{version}.dist-info

%changelog
