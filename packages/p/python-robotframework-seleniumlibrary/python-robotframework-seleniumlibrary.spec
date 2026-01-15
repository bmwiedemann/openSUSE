#
# spec file for package python-robotframework-seleniumlibrary
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
Name:           python-robotframework-seleniumlibrary
Version:        6.8.0
Release:        0
Summary:        Web testing library for Robot Framework
License:        Apache-2.0
URL:            https://github.com/robotframework/SeleniumLibrary
Source:         https://files.pythonhosted.org/packages/source/r/robotframework-seleniumlibrary/robotframework_seleniumlibrary-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module click >= 8.0}
BuildRequires:  %{python_module robotframework >= 4.1.3}
BuildRequires:  %{python_module robotframework-pythonlibcore >= 4.4.1}
BuildRequires:  %{python_module selenium >= 4.3.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click >= 8.0
Requires:       python-robotframework >= 4.1.3
Requires:       python-robotframework-pythonlibcore >= 4.4.1
Requires:       python-selenium >= 4.3.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Web testing library for Robot Framework

%prep
%autosetup -p1 -n robotframework_seleniumlibrary-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/selib
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative selib

%postun
%python_uninstall_alternative selib

%files %{python_files}
%python_alternative %{_bindir}/selib
%{python_sitelib}/SeleniumLibrary
%{python_sitelib}/robotframework_seleniumlibrary-%{version}.dist-info

%changelog
