#
# spec file for package python-osc-tiny
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-osc-tiny
Version:        0.3.3
Release:        0
Summary:        Client API for openSUSE BuildService
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/crazyscientist/osc-tiny
Source:         https://files.pythonhosted.org/packages/source/o/osc-tiny/osc-tiny-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-cached-property
Requires:       python-lxml
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
OSC Tiny provides a minimalistic, transparent and class based client for
accessing the OpenBuildService API.

For further details see:

* https://osc-tiny.readthedocs.io/en/latest/
* https://openbuildservice.org/
* https://build.opensuse.org/apidocs/index

%prep
%setup -q -n osc-tiny-%{version}

%build
%python_build

%check
%pytest

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
