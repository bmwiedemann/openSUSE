#
# spec file for package python-os-api-ref
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.6.2
Release:        0
Summary:        Sphinx Extensions to support API reference sites in OpenStack
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/o/os-api-ref/os-api-ref-1.6.2.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-PyYAML >= 3.12
BuildRequires:  python2-Sphinx
BuildRequires:  python2-beautifulsoup4
BuildRequires:  python2-openstackdocstheme >= 1.18.1
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-python-subunit
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-sphinx-testing
BuildRequires:  python2-stestr
BuildRequires:  python2-testtools
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-Sphinx
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-openstackdocstheme >= 1.18.1
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-sphinx-testing
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
Requires:       python-PyYAML >= 3.12
Requires:       python-Sphinx
Requires:       python-openstackdocstheme >= 1.18.1
Requires:       python-pbr >= 2.0.0
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

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

%prep
%autosetup -p1 -n os-api-ref-1.6.2
%py_req_cleanup

%build
%{python_build}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/os_api_ref
%{python_sitelib}/*.egg-info

%changelog
