#
# spec file for package wafw00f
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           wafw00f
Version:        2.2.0
Release:        0
Summary:        The Web Application Firewall Detection and Fingerprinting Toolkit
License:        BSD-3-Clause
URL:            https://github.com/enablesecurity/wafw00f
Source:         https://files.pythonhosted.org/packages/source/w/wafw00f/wafw00f-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pluginbase}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module requests}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pluginbase
Requires:       python-requests
Requires:       python-requests
Suggests:       python-prospector
Suggests:       python-Sphinx
BuildArch:      noarch
%python_subpackages

%description
The Web Application Firewall Detection and Fingerprinting Toolkit.

%prep
%setup -q -n wafw00f-%{version}
find . -iname "*.py" -exec sed -i '1{/^#!/ d}' {} \;

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/wafw00f
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative wafw00f

%postun
%python_uninstall_alternative wafw00f

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/wafw00f
%{python_sitelib}/*

%changelog
