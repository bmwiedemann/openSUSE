#
# spec file for package reuse
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017 Free Software Foundation Europe e.V.
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


%define pythons python3

Name:           reuse
Version:        5.0.2
Release:        0
Summary:        A tool for compliance with the REUSE recommendations
License:        Apache-2.0 AND CC-BY-SA-4.0 AND GPL-3.0-or-later AND CC0-1.0
Group:          Development/Languages/Python
URL:            https://git.fsfe.org/reuse/tool
Source:         https://files.pythonhosted.org/packages/source/r/reuse/reuse-%{version}.tar.gz
Patch:          sphinx-docs.patch
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
BuildRequires:  python3 >= 3.9
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core
# doc dependencies (manpage)
BuildRequires:  python3-Sphinx
BuildRequires:  python3-myst-parser
BuildRequires:  python3-sphinxcontrib-apidoc
# test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-freezegun
# runtime dependencies
BuildRequires:  python3-Jinja2 >= 3.0.0
BuildRequires:  python3-attrs >= 21.3
BuildRequires:  python3-binaryornot >= 0.4.4
BuildRequires:  python3-boolean.py >= 3.8
BuildRequires:  python3-click >= 8.0
BuildRequires:  python3-license-expression >= 1.0
BuildRequires:  python3-python-debian >= 0.1.34
BuildRequires:  python3-tomlkit >= 0.8
Requires:       python3-Jinja2 >= 3.0.0
Requires:       python3-attrs >= 21.3
Requires:       python3-binaryornot >= 0.4.4
Requires:       python3-boolean.py >= 3.8
Requires:       python3-click >= 8.0
Requires:       python3-license-expression >= 1.0
Requires:       python3-python-debian >= 0.1.34
Requires:       python3-tomlkit >= 0.8
Recommends:     git-core

%description
A tool for compliance with the REUSE recommendations.  Essentially,
it is a linter that checks for a project's compliance, and a compiler that
generates a project's bill of materials.

%prep
%autosetup -p 1

%build
%pyproject_wheel
make -C docs man

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitearch}
install -D -m 0644 docs/_build/man/*.1 -t "%{buildroot}%{_mandir}/man1/"

%check
IGNORED_CHECKS="test_help_is_default"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_version"
%pytest -k "not (${IGNORED_CHECKS})"

%files
%doc README.md CHANGELOG.md
%{_mandir}/man1/*.1%{ext_man}
%license LICENSES/*
%{_bindir}/reuse
%{python3_sitearch}/reuse/
%{python3_sitearch}/reuse-%{version}.dist-info

%changelog
