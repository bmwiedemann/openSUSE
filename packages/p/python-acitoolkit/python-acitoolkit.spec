#
# spec file for package python-acitoolkit
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
Name:           python-acitoolkit
Version:        0.4
Release:        0
Summary:        Python library for programming ACI
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/datacenter/acitoolkit
Source:         https://github.com/datacenter/acitoolkit/archive/v%{version}.tar.gz
Patch0:         remove-app-dependency.patch
# https://github.com/datacenter/acitoolkit/commit/629b84887dd0f0183b81efc8adb16817f985541a
Patch1:         python-acitoolkit-python-310.patch
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module websocket-client > 0.33.0}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-graphviz
Requires:       python-jsonschema
Requires:       python-requests
Requires:       python-tabulate
Requires:       python-websocket-client > 0.33.0
BuildArch:      noarch
%python_subpackages

%description
Python Library for configuring the Cisco Application Policy
Infrastructure Controller.

%package -n %{name}-doc
Summary:        Documentation for the Python acitoolkit library
Group:          Documentation/Other

%description -n %{name}-doc
Documentation for %{name}.

%package -n %{name}-doc-applications
Summary:        Applications for the Python acitoolkit library
Group:          Development/Languages/Python
Requires:       python-acitoolkit-doc
Requires:       python3-Flask
Requires:       python3-Flask-Admin
Requires:       python3-Flask-Bootstrap
Requires:       python3-Flask-Cors
Requires:       python3-Flask-HTTPAuth
Requires:       python3-Flask-SQLAlchemy
Requires:       python3-Flask-WTF
Requires:       python3-GitPython
Requires:       python3-py-radix

%description -n %{name}-doc-applications
Python applications using acitoolkit for programming ACI.

%package -n %{name}-doc-samples
Summary:        Sample code for the Python acitoolkit library
Group:          Development/Languages/Python
Requires:       %{name}-doc
Requires:       python3-PyMySQL

%description -n %{name}-doc-samples
Python samples for using acitoolkit for programming ACI.

%prep
%setup -q -n acitoolkit-%{version}
# Remove dependencies of applications/ and samples/ from the library
%patch0 -p1
%patch1 -p1

chmod -x LICENSE NOTICE

sed -i '1{/^#!.*env python/d}' acitoolkit/*.py samples/*.py samples/switch-commands/*.py

rm applications/cableplan/.coverage applications/eventfeeds/.gitignore

dos2unix \
  samples/aci-add-static-binding-leaves.py \
  applications/configpush/json_schema.json \
  applications/search/static/*.css applications/search/static/*.js \
  applications/connection_search/static/*.js \
  applications/reports/static/*.css applications/reports/static/*.js

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Install docs, samples and applications into a common doc area
install -d %{buildroot}%{_defaultdocdir}/%{name}
cp -rp docs/source/*.rst docs/source/*.png docs/source/stats/ samples/ applications/ %{buildroot}%{_defaultdocdir}/%{name}/
find %{buildroot}%{_defaultdocdir}/%{name}/ -type f -exec chmod a-x \{\} \;

%fdupes %{buildroot}%{_defaultdocdir}/%{name}/

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python tests/acitoolkit_test.py offline

%files -n %{name}-doc
%license LICENSE NOTICE
%dir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}/*.rst
%{_defaultdocdir}/%{name}/*.png
%{_defaultdocdir}/%{name}/stats/

%files -n %{name}-doc-samples
%{_defaultdocdir}/%{name}/samples/

%files -n %{name}-doc-applications
%{_defaultdocdir}/%{name}/applications/

%files %{python_files}
%doc README.md
%license LICENSE NOTICE
%{python_sitelib}/acitoolkit
%{python_sitelib}/acitoolkit-*.egg-info

%changelog
