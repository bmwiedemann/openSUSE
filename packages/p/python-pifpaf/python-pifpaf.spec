#
# spec file for package python-pifpaf
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
%bcond_without libalternatives
Name:           python-pifpaf
Version:        3.4.0
Release:        0
Summary:        Suite of tools and fixtures to manage daemons for testing
License:        Apache-2.0
URL:            https://github.com/jd/pifpaf
Source:         https://files.pythonhosted.org/packages/source/p/pifpaf/pifpaf-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%endif
Requires:       python-Jinja2
Requires:       python-click
Requires:       python-daiquiri
Requires:       python-fixtures
Requires:       python-psutil
Requires:       python-requests
Requires:       python-testrepository
Requires:       python-testtools
Requires:       python-xattr
BuildArch:      noarch
%python_subpackages

%description
Pifpaf is a suite of `fixtures`_ and a command-line tool that allows to start
and stop daemons for a quick throw-away usage. This is typically useful when
needing these daemons to run `integration testing`_. It originaly evolved from
its precussor `overtest`_.

%prep
%setup -q -n pifpaf-%{version}

%build
export LC_ALL=en_US.utf8
%pyproject_wheel

%install
export LC_ALL=en_US.utf8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pifpaf
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative pifpaf

%check
# rather integration tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pifpaf
%{python_sitelib}/pifpaf-%{version}*-info
%python_alternative %{_bindir}/pifpaf

%changelog
