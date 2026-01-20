#
# spec file for package python-requirements-detector
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


Name:           python-requirements-detector
Version:        1.3.2
Release:        0
Summary:        Python tool to find and list requirements of a Python project
License:        MIT
URL:            https://github.com/landscapeio/requirements-detector
Source:         https://github.com/landscapeio/requirements-detector/archive/%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astroid >= 3.0
Requires:       python-packaging >= 21.3
Requires:       python-semver >= 3
Requires:       python-toml >= 0.10
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module astroid >= 3.0}
BuildRequires:  %{python_module packaging >= 21.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module semver >= 3}
BuildRequires:  %{python_module toml >= 0.10}
# /SECTION
%python_subpackages

%description
Requirements-detector is a Python tool which attempts to find and list
the requirements of a Python project.

When run from the root of a Python project, it will try to ascertain
which libraries and the versions of those libraries that the project
depends on.

%prep
%autosetup -p1 -n requirements-detector-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/detect-requirements
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative detect-requirements

%postun
%python_uninstall_alternative detect-requirements

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/requirements_detector
%{python_sitelib}/requirements_detector-%{version}.dist-info
%python_alternative %{_bindir}/detect-requirements

%changelog
