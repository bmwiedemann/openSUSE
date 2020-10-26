#
# spec file for package python-openstacksdk
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


# and cause timeouts due to swapping. Disabling for now
%define with_tests 0
Name:           python-openstacksdk
Version:        0.50.0
Release:        0
Summary:        An SDK for building applications to work with OpenStack
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/openstacksdk
Source0:        https://files.pythonhosted.org/packages/source/o/openstacksdk/openstacksdk-0.50.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PyYAML >= 3.13
BuildRequires:  python3-appdirs >= 1.3.0
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-ddt
BuildRequires:  python3-decorator >= 4.4.1
BuildRequires:  python3-deprecation
BuildRequires:  python3-dogpile.cache >= 0.6.5
BuildRequires:  python3-extras
BuildRequires:  python3-fixtures
BuildRequires:  python3-jmespath >= 0.9.0
BuildRequires:  python3-jsonpatch >= 1.16
BuildRequires:  python3-jsonschema
BuildRequires:  python3-keystoneauth1 >= 3.18.0
BuildRequires:  python3-mock
BuildRequires:  python3-munch >= 2.1.0
BuildRequires:  python3-netifaces >= 0.10.4
BuildRequires:  python3-os-service-types >= 1.7.0
BuildRequires:  python3-oslo.config
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-requests-mock
BuildRequires:  python3-requestsexceptions >= 1.2.0
BuildRequires:  python3-six
BuildRequires:  python3-statsd
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch
%if 0%{?suse_version}
# RDO does not package prometheus_client
BuildRequires:  python3-prometheus_client
%endif

%description
The openstacksdk is a library for building applications to work
with OpenStack clouds.
The project aims to provide a consistent and complete set of
interactions with OpenStack's many services, along with complete
documentation, examples, and tools.

%package -n python3-openstacksdk
Summary:        An SDK for building applications to work with OpenStack
Group:          Development/Languages/Python
Requires:       python3-PyYAML >= 3.13
Requires:       python3-appdirs >= 1.3.0
Requires:       python3-cryptography >= 2.7
Requires:       python3-decorator >= 4.4.1
Requires:       python3-dogpile.cache >= 0.6.5
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-jmespath >= 0.9.0
Requires:       python3-jsonpatch >= 1.16
Requires:       python3-keystoneauth1 >= 3.18.0
Requires:       python3-munch >= 2.1.0
Requires:       python3-netifaces >= 0.10.4
Requires:       python3-os-service-types >= 1.7.0
Requires:       python3-requestsexceptions >= 1.2.0
Requires:       python3-six
%if 0%{?suse_version}
Obsoletes:      python2-openstacksdk < 1.0.0
%endif
%if 0%{?suse_version}
%if 0%{?sle_version} >= 150000 || 0%{?suse_version} > 1500
Requires:       mkisofs
%else
Requires:       genisoimage
%endif
%else
Requires:       genisoimage
%endif

%description -n python3-openstacksdk
The openstacksdk is a library for building applications to work
with OpenStack clouds.
The project aims to provide a consistent and complete set of
interactions with OpenStack's many services, along with complete
documentation, examples, and tools.

This package contains the Python 3.x module

%package -n python-openstacksdk-doc
Summary:        %{summary} - Documentation
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-svg2pdfconverter

%description -n python-openstacksdk-doc
The openstacksdk is a library for building applications to work
with OpenStack clouds.
The project aims to provide a consistent and complete set of
interactions with OpenStack's many services, along with complete
documentation, examples, and tools.

The openstacksdk is a collection of libraries for building
applications to work with OpenStack clouds.

%prep
%autosetup -p1 -n openstacksdk-0.50.0
%py_req_cleanup
sed -i -e 's,coverage.*,,' test-requirements.txt || true
sed -i -e "s,'sphinx.ext.intersphinx'\,,," doc/source/conf.py
%if !0%{?suse_version}
# RDO does not package prometheus_client
rm openstack/tests/unit/test_stats.py
%endif

%build
%py3_build
PBR_VERSION=0.50.0 %sphinx_build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%py3_install

%if 0%{?with_tests}
%check
export OS_LOG_CAPTURE=true
export OS_TEST_TIMEOUT=30
python3 -m stestr.cli run
%endif

%files -n python3-openstacksdk
%license LICENSE
%doc ChangeLog README.rst
%{_bindir}/openstack-inventory
%{python3_sitelib}/openstack
%{python3_sitelib}/*.egg-info

%files -n python-openstacksdk-doc
%license LICENSE
%doc doc/build/html

%changelog
