#
# spec file for package python-griffecli
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


%bcond_without libalternatives
Name:           python-griffecli
# Must be upgraded in lockstep with griffelib and griffe
Version:        2.4.1
Release:        0
Summary:        Signatures for Python programs (CLI module)
License:        ISC
URL:            https://mkdocstrings.github.io/griffe/
Source0:        https://files.pythonhosted.org/packages/source/g/griffecli/griffecli-%{version}.tar.gz
Source99:       python-griffecli.rpmlintrc
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-dynamic-versioning}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-colorama >= 0.4
Requires:       python-griffelib = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module colorama >= 0.4}
BuildRequires:  %{python_module griffelib == %{version}}
# /SECTION
%python_subpackages

%description
Griffecli is the command line interface for Griffe. It extracts the
structure, frame, and skeleton of Python programs using static and dynamic
analysis, allowing tools like mkdocstrings to generate API documentation and
detect breaking API changes between versions.

%prep
%autosetup -p1 -n griffecli-%{version}

%build
export UV_DYNAMIC_VERSIONING_BYPASS="%{version}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/griffecli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative griffecli

%postun
%python_uninstall_alternative griffecli

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE LICENSE
%python_alternative %{_bindir}/griffecli
%{python_sitelib}/griffecli
%{python_sitelib}/griffecli-%{version}.dist-info

%changelog
