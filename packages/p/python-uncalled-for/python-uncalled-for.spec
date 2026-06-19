#
# spec file for package python-uncalled-for
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


Name:           python-uncalled-for
Version:        0.3.2
Release:        0
Summary:        Async-friendly dependency injection for Python
License:        MIT
URL:            https://github.com/chrisguidry/uncalled-for
Source:         https://files.pythonhosted.org/packages/source/u/uncalled-for/uncalled_for-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A small, async-friendly dependency-injection helper for Python: declare
function parameters as dependencies and have them resolved automatically.

%prep
%autosetup -p1 -n uncalled_for-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/uncalled_for
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import uncalled_for"

%files %{python_files}
%doc README.md
%{python_sitelib}/uncalled_for
%{python_sitelib}/uncalled_for-%{version}.dist-info

%changelog
