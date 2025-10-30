#
# spec file for package python-flynt
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


%{?sle15_python_module_pythons}
Name:           python-flynt
Version:        1.0.6
Release:        0
Summary:        CLI tool to convert a python project's %-formatted strings to f-strings
License:        MIT
URL:            https://github.com/ikamensh/flynt
Source:         https://github.com/ikamensh/flynt/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires(post): update-alternatives
Requires(preun): update-alternatives
%python_subpackages

%description
CLI tool to convert a python project's %-formatted strings to f-strings.

%prep
%autosetup -p1 -n flynt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/flynt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative flynt

%postun
%python_uninstall_alternative flynt

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/flynt
%{python_sitelib}/flynt
%{python_sitelib}/flynt-%{version}.dist-info

%changelog
