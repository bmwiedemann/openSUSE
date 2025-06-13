#
# spec file for package python-launchpadlib
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


%{?sle15_python_module_pythons}
Name:           python-launchpadlib
Version:        2.1.0
Release:        0
Summary:        Python client library for Launchpad's web service
License:        LGPL-3.0-only
URL:            https://help.launchpad.net/API/launchpadlib
Source:         https://files.pythonhosted.org/packages/source/l/launchpadlib/launchpadlib-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module httplib2}
BuildRequires:  %{python_module lazr.restfulclient}
BuildRequires:  %{python_module lazr.uri}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testresources}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-httplib2
Requires:       python-lazr.restfulclient
Requires:       python-lazr.uri
BuildArch:      noarch
%python_subpackages

%description
launchpadlib is an open-source Python library that lets you treat the HTTP resources published by
Launchpad's web service as Python objects responding to a standard set of commands. With launchpadlib
you can integrate your applications into Launchpad without knowing a lot about HTTP client programming.

%prep
%autosetup -p1 -n launchpadlib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/launchpadlib/docs
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pyunittest discover -v src/launchpadlib/tests/

%files %{python_files}
%license COPYING.txt
%doc README.rst src/launchpadlib/docs/
%{python_sitelib}/launchpadlib
%{python_sitelib}/launchpadlib-%{version}*-info

%changelog
