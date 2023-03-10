#
# spec file for package python-sphinx-autobuild
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-sphinx-autobuild
Version:        2021.3.14
Release:        0
Summary:        Rebuild Sphinx documentation on changes, with live-reload in the browser
License:        MIT
URL:            https://github.com/executablebooks/sphinx-autobuild
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-autobuild/sphinx-autobuild-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module livereload}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-colorama
Requires:       python-livereload
Requires:       python-Sphinx
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Rebuild Sphinx documentation on changes, with live-reload in the browser.

%prep
%setup -q -n sphinx-autobuild-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/sphinx-autobuild
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative sphinx-autobuild

%postun
%python_uninstall_alternative sphinx-autobuild

%files %{python_files}
%doc AUTHORS NEWS.rst README.md
%license LICENSE
%python_alternative %{_bindir}/sphinx-autobuild
%{python_sitelib}/sphinx_autobuild
%{python_sitelib}/sphinx_autobuild-%{version}*-info

%changelog
