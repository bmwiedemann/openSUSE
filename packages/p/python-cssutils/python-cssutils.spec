#
# spec file for package python-cssutils
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cssutils
Version:        2.7.0
Release:        0
Summary:        A CSS Cascading Style Sheets library for Python
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/cssutils
Source0:        https://files.pythonhosted.org/packages/source/c/cssutils/cssutils-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not any rendering facilities!

%prep
%setup -q -n cssutils-%{version}

# SECTION Generate a basic setup.py as upstream only supplies setup.cfg
cat << EOF > setup.py
import setuptools

if __name__ == "__main__":
    setuptools.setup()

EOF
# /SECTION

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/csscapture
%python_clone -a %{buildroot}%{_bindir}/csscombine
%python_clone -a %{buildroot}%{_bindir}/cssparse

%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%post
%{python_install_alternative csscapture csscombine cssparse}

%postun
%python_uninstall_alternative csscapture

%files %{python_files}
%license COPYING COPYING.LESSER
%doc README.rst examples
%python_alternative %{_bindir}/csscapture
%python_alternative %{_bindir}/csscombine
%python_alternative %{_bindir}/cssparse
%{python_sitelib}/cssutils-%{version}-py%{python_version}.egg-info/
%{python_sitelib}/cssutils/
%{python_sitelib}/encutils/

%changelog
