#
# spec file for package python-webruntime
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


%define         skip_python2 1
Name:           python-webruntime
Version:        0.5.8
Release:        0
Summary:        A python package to launch HTML5 apps in the browser or a desktop-like runtime
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/flexxui/webruntime
Source:         https://files.pythonhosted.org/packages/source/w/webruntime/webruntime-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dialite
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dialite}
BuildRequires:  %{python_module pytest}
BuildRequires:  MozillaFirefox
# /SECTION
%python_subpackages

%description
The webruntime module can be used to launch applications based on
HTML/JS/CSS. This can be a browser or a runtime that looks like a
desktop app, such as XUL (based on Firefox) or NW.js.

%prep
%setup -q -n webruntime-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/webruntime
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative webruntime

%postun
%python_uninstall_alternative webruntime

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/webruntime
%{python_sitelib}/webruntime
%{python_sitelib}/webruntime-%{version}.dist-info

%changelog
