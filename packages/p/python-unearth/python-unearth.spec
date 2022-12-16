#
# spec file for package python-unearth
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-unearth
Version:        0.7.0
Release:        0
Summary:        A utility to fetch and download python packages
License:        MIT
URL:            https://unearth.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/u/unearth/unearth-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module cached-property >= 1.5.2 if %python-base < 3.8}
BuildRequires:  %{python_module packaging >= 20}
BuildRequires:  %{python_module pdm-pep517}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.25}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 20
Requires:       python-requests >= 2.25
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if 0%{?python_version_nodots} < 38
Requires:       python-cached-property >= 1.5.2
%endif
# SECTION test
BuildRequires:  %{python_module Flask >= 2.1.2}
BuildRequires:  %{python_module pytest-httpserver >= 1.0.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-wsgi-adapter >= 0.4.1}
BuildRequires:  %{python_module trustme >= 0.9.0}
# /SECTION
%python_subpackages

%description
This project exists as the last piece to complete the puzzle of a package manager. The other pieces are:

- python-resolvelib - Resolves concrete dependencies from a set of (abstract) requirements.
- python-unearth - Finds and downloads the best match(es) for a given requirement.
- python-build - Builds wheels from the source code.
- python-installer - Installs packages from wheels.

They provide all the low-level functionalities that are needed to resolve and install packages.

%prep
%setup -q -n unearth-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/unearth
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative unearth

%postun
%python_uninstall_alternative unearth

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/unearth
%{python_sitelib}/unearth
%{python_sitelib}/unearth-%{version}*-info

%changelog
