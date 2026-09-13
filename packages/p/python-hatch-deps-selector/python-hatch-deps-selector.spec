#
# spec file for package python-deps-selector
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


Name:           python-hatch-deps-selector
Version:        0.1.2
Release:        0
Summary:        Hatch plugin for configuring "variants" of dependencies
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-book/hatch-deps-selector
Source:         https://github.com/jupyter-book/hatch-deps-selector/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-hatch_deps_selector = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Hatch plugin for configuring "variants" of dependencies according to an environment variable.
This can be used e.g. to change the package dependencies for conda-forge vs PyPI builds.

%prep
%setup -q -n hatch-deps-selector-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # There are no upstream tests
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import hatch_deps_selector'
}

%files %{python_files}
%doc README.md
%{python_sitelib}/hatch_deps_selector
%{python_sitelib}/hatch_deps_selector-%{version}.dist-info

%changelog
