#
# spec file for package python-os-api-ref
#
# Copyright (c) 2020 SUSE LLC
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


Name:           python-os-api-ref
Version:        2.1.0
Release:        0
Summary:        Sphinx Extensions to support API reference sites in OpenStack
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/o/os-api-ref/os-api-ref-2.1.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-Sphinx
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-openstackdocstheme >= 2.2.1
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-sphinx-testing
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
This project is a collection of sphinx stanzas that assist in building an API
Reference site for an OpenStack project in RST. RST is great for
unstructured English, but displaying semi structured (and repetitive) data
in tables is not it's strength. This provides tooling to insert semi-structured
data describing request and response parameters, and turn those into nice
tables.
The project also includes a set of styling (and javascript) that is expected
to layer on top of an openstackdocstheme theme base. This provides a nice set
of collapsing sections for REST methods and javascript controls to
expand / collapse all sections.

%package -n python3-os-api-ref
Summary:        Sphinx Extensions to support API reference sites in OpenStack
Group:          Development/Languages/Python
Requires:       python3-PyYAML >= 3.12
Requires:       python3-Sphinx
Requires:       python3-openstackdocstheme >= 2.2.1
Requires:       python3-pbr >= 2.0.0
Requires:       python3-six >= 1.10.0

%description -n python3-os-api-ref
This project is a collection of sphinx stanzas that assist in building an API
Reference site for an OpenStack project in RST. RST is great for
unstructured English, but displaying semi structured (and repetitive) data
in tables is not it's strength. This provides tooling to insert semi-structured
data describing request and response parameters, and turn those into nice
tables.
The project also includes a set of styling (and javascript) that is expected
to layer on top of an openstackdocstheme theme base. This provides a nice set
of collapsing sections for REST methods and javascript controls to
expand / collapse all sections.

This package contains the Python 3.x module.

%prep
%autosetup -p1 -n os-api-ref-2.1.0
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-os-api-ref
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/os_api_ref
%{python3_sitelib}/*.egg-info

%changelog
