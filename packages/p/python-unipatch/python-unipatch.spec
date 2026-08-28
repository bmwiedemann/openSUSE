#
# spec file for package python-unipatch
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


%{?sle15_python_module_pythons}
Name:           python-unipatch
Version:        1.0.0
Release:        0
Summary:        Apply unified diffs in memory, compatible with GNU patch
License:        MIT
URL:            https://github.com/adamchainz/unipatch
Source:         https://github.com/adamchainz/unipatch/archive/refs/tags/%{version}.tar.gz#/unipatch-%{version}.tar.gz
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module uv-build}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Apply unified diffs in memory, compatible with GNU patch.

unipatch follows the behaviour of the GNU ``patch`` commandline utility, verified by differentially testing against it with randomized inputs:

* Hunks may apply at an *offset* from the line numbers stated in their ``@@`` headers, matching by content, with a found offset carrying forward to later hunks.

* A *fuzz factor* ignores up to two mismatching context lines at the edges of a hunk. Ignored context lines are left as they are in the source.
  A hunk with less context on one side, as ``diff`` produces at the start or end of a file, only applies at that edge of the source.

* Oddities are tolerated like GNU ``patch``:

  * Hunks cut short at the end of the patch
  * Context lines that have lost their leading space (empty and tab-led lines)
  * ``\ No newline at end of file`` markers

Only unified diff format is supported, not the older context or ``ed`` formats.
Hence the name is ``unipatch``.

%prep
%autosetup -p1 -n unipatch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/unipatch
%{python_sitelib}/unipatch-%{version}.dist-info

%changelog
