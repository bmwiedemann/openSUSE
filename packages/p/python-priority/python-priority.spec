#
# spec file for package python-priority
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


%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-priority
Version:        2.0.0
Release:        0
Summary:        A pure-Python implementation of the HTTP/2 priority tree
License:        MIT
URL:            https://github.com/python-hyper/priority/
Source:         https://files.pythonhosted.org/packages/source/p/priority/priority-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6.1}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Priority is a pure-Python implementation of the priority logic for HTTP/2, set
out in `RFC 7540 Section 5.3 (Stream Priority)`. This logic allows for clients
to express a preference for how the server allocates its (limited) resources to
the many outstanding HTTP requests that may be running over a single HTTP/2
connection.

%prep
%setup -q -n priority-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/priority
%{python_sitelib}/priority-%{version}*-info

%changelog
