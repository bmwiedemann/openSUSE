#
# spec file for package python-extra-platforms
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
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-extra-platforms
Version:        9.2.0
Release:        0
Summary:        Detect platforms and group them by family
License:        GPL-2.0-or-later
URL:            https://github.com/kdeldycke/extra-platforms
Source:         https://github.com/kdeldycke/extra-platforms/archive/refs/tags/v%{version}.tar.gz#/extra_platforms-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module uv-build}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION runtime requirements
BuildRequires:  %{python_module distro >= 1.9.0}
# /SECTION
# SECTION test requirements
BuildRequires:  openSUSE-release
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module myst-parser}
BuildRequires:  %{python_module pytest >= 8.3.5}
BuildRequires:  %{python_module pytest-randomly >= 3.16.0}
BuildRequires:  %{python_module pytest-xdist >= 3.8.0}
BuildRequires:  %{python_module requests >= 2.32.3 with %python-requests < 2.33}
BuildRequires:  %{python_module tabulate >= 0.9}
BuildRequires:  %{python_module tomli >= 2.3.0 if %python-base < 3.11}
BuildRequires:  %{python_module wcmatch >= 10.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-distro >= 1.9.0
BuildArch:      noarch
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
Detect platforms and group them by family

%prep
%autosetup -p1 -n extra-platforms-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/extra-platforms

%check
# remove coverage configuration
sed -i '/cov=/d' pyproject.toml
sed -i '/cov-report=/d' pyproject.toml
sed -i '/--cov-branch/d' pyproject.toml
sed -i '/--cov-precision=2/d' pyproject.toml
# do not run tests that try to connect to websites
rm -f tests/test_platform_data.py
# remove sphinx tests
rm -f tests/test_sphinx_crossrefs.py

IGNORED_CHECKS="test_pyproject_classifiers"
%pytest -k "not (${IGNORED_CHECKS})"

%if %{with libalternatives}
%pre
%python_libalternatives_reset_alternative extra-platforms
%else

%post
%python_install_alternative extra-platforms

%postun
%python_uninstall_alternative extra-platforms
%endif

%files %{python_files}
%python_alternative %{_bindir}/extra-platforms
%{python_sitelib}/extra_platforms
%{python_sitelib}/extra_platforms-%{version}.dist-info

%changelog
