#
# spec file for package python-PyChromecast
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


%{?sle15_python_module_pythons}
%global skip_python310 1
Name:           python-PyChromecast
Version:        14.0.5
Release:        0
Summary:        Python module to talk to Google Chromecast
License:        MIT
URL:            https://github.com/balloob/pychromecast
Source:         https://files.pythonhosted.org/packages/source/P/PyChromecast/PyChromecast-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-casttube >= 0.2.0
Requires:       python-protobuf >= 3.19.1
Requires:       python-zeroconf >= 0.25.1
BuildArch:      noarch
%python_subpackages

%description
Library to communicate with the Google Chromecast. It currently supports
Auto discovering connected Chromecasts on the network, start the default
media receiver and play any online media, control playback of current
playing media, implement Google Chromecast api v2, communicate with apps
via channels, easily extendable to add support for unsupported namespaces,
multi-room setups with Audio cast devices.

%prep
%setup -q -n PyChromecast-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no tests even on GitHub https://github.com/balloob/pychromecast/issues/333
# but they will most probably ignore this issue

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pychromecast
%{python_sitelib}/PyChromecast-%{version}.dist-info

%changelog
