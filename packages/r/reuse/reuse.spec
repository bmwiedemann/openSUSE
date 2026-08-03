#
# spec file for package reuse
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        6.2.0
Release:        0
Summary:        A tool for compliance with the REUSE recommendations
License:        Apache-2.0 AND CC-BY-SA-4.0 AND GPL-3.0-or-later AND CC0-1.0
URL:            https://git.fsfe.org/reuse/tool
Source:         https://files.pythonhosted.org/packages/source/r/reuse/reuse-%{version}.tar.gz
Patch0:         sphinx-docs.patch
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  python-rpm-macros
BuildRequires:  python3 >= 3.10
# runtime dependencies
BuildRequires:  python3-Jinja2 >= 3.0.0
# doc dependencies (manpage)
BuildRequires:  python3-Sphinx
BuildRequires:  python3-attrs >= 23.2
BuildRequires:  python3-click >= 8.1
BuildRequires:  python3-freezegun
BuildRequires:  python3-license-expression >= 21.6.14
BuildRequires:  python3-myst-parser
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core
# test dependencies
BuildRequires:  python3-chardet
BuildRequires:  python3-charset-normalizer
BuildRequires:  python3-pytest
BuildRequires:  python3-python-debian >= 0.1.48
BuildRequires:  python3-python-magic >= 0.4.12
BuildRequires:  python3-sphinxcontrib-apidoc
BuildRequires:  python3-tomlkit >= 0.8
# git-core for the vcs tests (spec-cleaner --perl wrongly explodes this into perl(Git::*))
BuildRequires:  git-core
Requires:       python3-Jinja2 >= 3.0.0
Requires:       python3-attrs >= 23.2
Requires:       python3-click >= 8.1
Requires:       python3-license-expression >= 21.6.14
Requires:       python3-python-debian >= 0.1.48
Requires:       python3-python-magic >= 0.4.12
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
# the docs use sphinxcontrib.apidoc/autodoc, which import the reuse modules;
# conf.py does not add src/ to sys.path, so do it here (the package is not yet
# installed — __init__ falls back to a hardcoded version when not installed)
export PYTHONPATH="$PWD/src"
# SPHINXOPTS= drops upstream's --fail-on-warning: the offline build cannot fetch
# the intersphinx python.org inventory, and that lone warning must not be fatal
%make_build -C docs man SPHINXOPTS=

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitearch}
install -D -m 0644 docs/_build/man/*.1 -t "%{buildroot}%{_mandir}/man1/"

%check
# TestEncodingModule spawns `python -c "import reuse.extract"`, which needs the
# installed package on PYTHONPATH; collect only tests/ so pytest does not also
# pick up src/reuse (which would clash with the installed copy)
export PYTHONPATH="%{buildroot}%{python3_sitearch}"
IGNORED_CHECKS="test_help_is_default"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_version"
%pytest -k "not (${IGNORED_CHECKS})" tests

%files
%doc README.md CHANGELOG.md
%{_mandir}/man1/*.1%{?ext_man}
%license LICENSES/*
%{_bindir}/reuse
%{python3_sitearch}/reuse/
%{python3_sitearch}/reuse-%{version}.dist-info

%changelog
