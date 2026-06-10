#
# spec file for package wafw00f
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


%bcond_without  libalternatives

Name:           wafw00f
Version:        2.4.2
Release:        0
Summary:        The Web Application Firewall Detection and Fingerprinting Toolkit
License:        BSD-3-Clause
URL:            https://github.com/enablesecurity/wafw00f
#Source0:        https://files.pythonhosted.org/packages/source/w/wafw00f/wafw00f-%%{version}.tar.gz
# use source from github to get complete tests
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-request-path.patch -- based on commit af3eca1
Patch0:         fix-request-path.patch
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module responses}
# /SECTION
Requires:       alts
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
The Web Application Firewall Detection and Fingerprinting Toolkit.

%prep
%autosetup -p1
# fix non-executable-script
find . -iname "*.py" -exec sed -i '1{/^#!/ d}' {} \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/wafw00f
%python_expand %python3_fix_shebang_path %{buildroot}%{$python_sitelib}/wafw00f/bin/wafw00f
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative wafw00f

%post
%python_install_alternative wafw00f

%postun
%python_uninstall_alternative wafw00f

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/wafw00f
%{python_sitelib}/wafw00f
%{python_sitelib}/wafw00f-%{version}.dist-info

%changelog
