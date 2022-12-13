#
# spec file for package python-pythonfinder
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


Name:           python-pythonfinder
Version:        1.3.1
Release:        0
Summary:        A tool to locate Python on the system
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sarugaku/pythonfinder
Source:         https://github.com/sarugaku/pythonfinder/archive/refs/tags/v%{version}.tar.gz#/pythonfinder-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 36.2.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs
Requires:       python-cached-property
Requires:       python-click
Requires:       python-packaging
Requires:       python-vistir >= 0.2.5
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module crayons}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module vistir >= 0.2.5}
# /SECTION
%python_subpackages

%description
A Python discovery tool to locate Python on the system.

%prep
%setup -q -n pythonfinder-%{version}
rm -r tasks

sed -i '/addopts/d' setup.cfg

# pep514tools is a Windows only dependency which is loosely coupled
# https://travis-ci.org/jayvdb/pythonfinder/builds/505169805
rm -rf src/pythonfinder/_vendor/pep514tools

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyfinder
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Three tests fail with OSError: [Errno 1] Operation not permitted , attempting
# to modify read-only system image files.
%pytest -k 'not (test_python_versions or test_shims_are_kept or test_shims_are_removed)'

%post
%python_install_alternative pyfinder

%postun
%python_uninstall_alternative pyfinder

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/pyfinder
%{python_sitelib}/*

%changelog
