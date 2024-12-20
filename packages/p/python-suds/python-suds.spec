#
# spec file for package python-suds
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15allpythons}
Name:           python-suds
Version:        1.2.0
Release:        0
Summary:        Lightweight SOAP client
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/suds-community/suds
Source:         https://files.pythonhosted.org/packages/source/s/suds/suds-%{version}.tar.gz
BuildRequires:  %{python_module devel}
# Test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-suds-jurko = %{version}
Obsoletes:      python-suds-jurko < %{version}
Provides:       python-suds-community = %{version}
Obsoletes:      python-suds-community < %{version}
BuildArch:      noarch
%python_subpackages

%description
Suds is a lightweight SOAP-based web service client for Python.

Although the original suds package stopped releasing versions after
0.4, many (but not all) other open source projects moved to a
maintained fork known as "suds-jurko". This is a community fork of
that fork that is releasing packages under the main suds package name
(and suds-community for consistency until version 2.x of this
package).

%prep
%autosetup -p1 -n suds-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/suds*

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/suds
%{python_sitelib}/suds_community-%{version}-py%{python_version}.egg-info

%changelog
