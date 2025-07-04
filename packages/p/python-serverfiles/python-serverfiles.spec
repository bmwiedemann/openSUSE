#
# spec file for package python-serverfiles
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


Name:           python-serverfiles
Version:        0.3.1
Release:        0
Summary:        A utility to locally store files on a HTTP server
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/biolab/serverfiles
Source:         https://files.pythonhosted.org/packages/source/s/serverfiles/serverfiles-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.11.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module requests >= 2.11.1}
# /SECTION
%python_subpackages

%description
A utility that accesses files on an HTTP server and stores them
locally for reuse.

%prep
%setup -q -n serverfiles-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/serverfiles
%{python_sitelib}/serverfiles-%{version}*-info

%changelog
