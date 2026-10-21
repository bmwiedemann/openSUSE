#
# spec file for package gcovr
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2019 Neal Gompa <ngompa13@gmail.com>.
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


# Single-flavour application: build with the primary interpreter so the
# install paths match the python3 macros (the pyproject default may
# otherwise pick a newer non-primary flavor)
%define pythons %{primary_python}
Name:           gcovr
Version:        8.6
Release:        0
Summary:        A code coverage report generator using GNU gcov
License:        BSD-3-Clause
URL:            https://gcovr.com/
Source0:        https://github.com/gcovr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Jinja2
BuildRequires:  python3-Pygments
BuildRequires:  python3-colorlog
BuildRequires:  python3-lxml
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(python3-embed)
# for %%{_bindir}/gcov
Requires:       gcc
Requires:       python3-Jinja2
Requires:       python3-Pygments
Requires:       python3-colorlog
Requires:       python3-lxml
BuildArch:      noarch
# Only build the documentation on Tumbleweed, as
# python3-sphinxcontrib-autoprogram has not yet landed in anything
# else
%if 0%{?suse_version} > 1500
BuildRequires:  python3-Jinja2
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-autoprogram
%endif

%description
Gcovr provides a utility for managing the use of the GNU gcov utility
and generating summarized code coverage results.

This command is inspired by the Python coverage.py package, which provides
a similar utility in Python. The gcovr command produces either compact
human-readable summary reports, machine readable XML reports
(in Cobertura format) or simple HTML reports. Thus, gcovr can be viewed
as a command-line alternative to the lcov utility, which runs gcov and
generates an HTML-formatted report.

%if 0%{?suse_version} > 1500
%package        doc
Summary:        Documentation of gcovr
BuildRequires:  python3-Jinja2
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-autoprogram

%description    doc
Gcovr provides a utility for managing the use of the GNU gcov utility
and generating summarized code coverage results.

This package contains the documentation of gcovr.
%endif

%prep
%autosetup

%build
# hatch-vcs derives the version from git, which the tarball lacks
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install

%if 0%{?suse_version} > 1500
# the documentation can only be build **after** gcovr is installed
# => need to set PATH, PYTHONPATH so that the installed binary & package are
# found
# also set PYTHON so that the sphinx Makefile picks up python3 instead of
# python2
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHON=python3

pushd doc

# Manpage
sphinx-build -b man source build/man
install -D -p -m 0644 build/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# html doc
sphinx-build -b html source build/html
rm build/html/.buildinfo
%fdupes -s build/html

popd
%endif

%fdupes -s %{buildroot}%{python3_sitelib}

%files
%license LICENSE.txt
%doc README.rst CHANGELOG.rst

%{_bindir}/%{name}
%{python3_sitelib}/%{name}*

%if 0%{?suse_version} > 1500
%{_mandir}/man1/%{name}.1%{?ext_man}

%files doc
%doc doc/build/html/*
%endif

%changelog
