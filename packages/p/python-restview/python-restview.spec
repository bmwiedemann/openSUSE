#
# spec file for package python-restview
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-restview
Version:        3.0.1
Release:        0
Summary:        ReStructuredText viewer
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://mg.pov.lt/restview/
Source:         https://files.pythonhosted.org/packages/source/r/restview/restview-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-tests.patch gh#mgedmin/restview@5033eacb1d55
Patch0:         fix-tests.patch
# PATCH-FIX-UPSTREAM fix_tests.patch gh#mgedmin/restview@6a1d6b44ee40
Patch1:         fix_tests.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-docutils
Requires:       python-pygments
Requires:       python-readme_renderer
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module readme_renderer}
# /SECTION
%python_subpackages

%description
A viewer for ReStructuredText documents that renders them on the fly.

%prep
%autosetup -p1 -n restview-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/restview
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative restview

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/restview
%{python_sitelib}/restview
%{python_sitelib}/restview-%{version}*-info

%changelog
