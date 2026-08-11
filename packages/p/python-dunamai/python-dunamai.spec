#
# spec file for package python-dunamai
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
%bcond_without  libalternatives
%define         modname dunamai
Name:           python-dunamai
Version:        1.26.2
Release:        0
Summary:        Dynamic version generation
License:        MIT
URL:            https://github.com/mtkennerly/dunamai
Source0:        https://files.pythonhosted.org/packages/source/d/dunamai/dunamai-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  alts
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-packaging
BuildArch:      noarch
%python_subpackages

%description
Dunamai is a Python 3.5+ library and command line tool for producing dynamic,
standards-compliant version strings, derived from tags in your version
control system. This facilitates uniquely identifying nightly or per-commit
builds in continuous integration and releasing new versions of your software
simply by creating a tag.

%prep
%autosetup -p1 -n %{modname}-%{version}
dos2unix CHANGELOG.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/%{modname}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="git"
%pytest -k "not $donttest"

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/%{modname}
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}.dist-info

%changelog
