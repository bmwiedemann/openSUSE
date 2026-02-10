#
# spec file for package python-coherent.deps
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


Name:           python-coherent.deps
Version:        1.6.0
Release:        0
Summary:        Utilities for resolving imports to dependencies
License:        MIT
URL:            https://github.com/coherent-oss/coherent.deps
Source:         https://files.pythonhosted.org/packages/source/c/coherent.deps/coherent_deps-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jaraco.collections
Requires:       python-jaraco.compat
Requires:       python-jaraco.context
Requires:       python-jaraco.functools
Requires:       python-jaraco.mongodb
Requires:       python-jaraco.ui
Requires:       python-keyring
Requires:       python-more-itertools
Requires:       python-requests
Requires:       python-requests-file
Requires:       python-requests-toolbelt
Requires:       python-retry-requests
Requires:       python-tempora
Requires:       python-tqdm
Requires:       python-typer
Requires:       python-zipp
BuildArch:      noarch
%python_subpackages

%description
Coherent deps (dependencies) provides insights into the dependencies used by a code base, resolving imports to the dependencies that supply those imports. The Coherent OSS community presents this library to make the functionality available for a variety of uses.

%prep
%autosetup -p1 -n coherent_deps-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# there is no test suite

%files %{python_files}
%doc README.md
%license LICENSE
%dir %{python_sitelib}/coherent
%{python_sitelib}/coherent/deps
%{python_sitelib}/coherent_deps-%{version}.dist-info

%changelog
