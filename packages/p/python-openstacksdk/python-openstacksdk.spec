#
# spec file for package python-openstacksdk
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


Name:           python-openstacksdk
Version:        0.27.0
Release:        0
Summary:        An SDK for building applications to work with OpenStack
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/openstacksdk
Source0:        https://files.pythonhosted.org/packages/source/o/openstacksdk/openstacksdk-0.27.0.tar.gz
# https://review.openstack.org/#/c/651119/
Patch0:         0001-add-python-3.7-unit-test-job.patch
# https://review.openstack.org/#/c/651193/
Patch1:         0001-baremetal-Add-support-for-mkisofs-and-xorrisofs-for-.patch
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-PyYAML >= 3.12
BuildRequires:  python2-appdirs >= 1.3.0
BuildRequires:  python2-beautifulsoup4
BuildRequires:  python2-decorator >= 3.4.0
BuildRequires:  python2-deprecation
BuildRequires:  python2-dogpile.cache >= 0.6.2
BuildRequires:  python2-extras
BuildRequires:  python2-fixtures
BuildRequires:  python2-futures >= 3.0.0
BuildRequires:  python2-ipaddress >= 1.0.17
BuildRequires:  python2-jmespath >= 0.9.0
BuildRequires:  python2-jsonpatch >= 1.16
BuildRequires:  python2-jsonschema
BuildRequires:  python2-keystoneauth1 >= 3.13.0
BuildRequires:  python2-mock
BuildRequires:  python2-munch >= 2.1.0
BuildRequires:  python2-netifaces >= 0.10.4
BuildRequires:  python2-os-service-types >= 1.2.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-python-subunit
BuildRequires:  python2-requests-mock
BuildRequires:  python2-requestsexceptions >= 1.2.0
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python2-stevedore
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-appdirs >= 1.3.0
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-decorator >= 3.4.0
BuildRequires:  python3-deprecation
BuildRequires:  python3-devel
BuildRequires:  python3-dogpile.cache >= 0.6.2
BuildRequires:  python3-extras
BuildRequires:  python3-fixtures
BuildRequires:  python3-jmespath >= 0.9.0
BuildRequires:  python3-jsonpatch >= 1.16
BuildRequires:  python3-jsonschema
BuildRequires:  python3-keystoneauth1 >= 3.13.0
BuildRequires:  python3-mock
BuildRequires:  python3-munch >= 2.1.0
BuildRequires:  python3-netifaces >= 0.10.4
BuildRequires:  python3-os-service-types >= 1.2.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-requests-mock
BuildRequires:  python3-requestsexceptions >= 1.2.0
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-PyYAML >= 3.12
Requires:       python-appdirs >= 1.3.0
Requires:       python-cryptography >= 2.1
Requires:       python-decorator >= 3.4.0
Requires:       python-dogpile.cache >= 0.6.2
Requires:       python-iso8601 >= 0.1.11
Requires:       python-jmespath >= 0.9.0
Requires:       python-jsonpatch >= 1.16
Requires:       python-keystoneauth1 >= 3.13.0
Requires:       python-munch >= 2.1.0
Requires:       python-netifaces >= 0.10.4
Requires:       python-os-service-types >= 1.2.0
Requires:       python-requestsexceptions >= 1.2.0
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%ifpython2
Requires:       python-futures >= 3.0.0
Requires:       python-ipaddress >= 1.0.17
%endif
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
The openstacksdk is a library for building applications to work
with OpenStack clouds.
The project aims to provide a consistent and complete set of
interactions with OpenStack's many services, along with complete
documentation, examples, and tools.

%package -n python-openstacksdk-doc
Summary:        %{summary} - Documentation
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
Requires:       %{name} = %{version}

%description -n python-openstacksdk-doc
The openstacksdk is a library for building applications to work
with OpenStack clouds.
The project aims to provide a consistent and complete set of
interactions with OpenStack's many services, along with complete
documentation, examples, and tools.

The openstacksdk is a collection of libraries for building
applications to work with OpenStack clouds.

%prep
%autosetup -p1 -n openstacksdk-0.27.0
%py_req_cleanup
sed -i -e 's,coverage.*,,' test-requirements.txt || true
sed -i -e "s,'sphinx.ext.intersphinx'\,,," doc/source/conf.py

%build
%python_build
PBR_VERSION=0.27.0 sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/openstack-inventory

%post
%python_install_alternative openstack-inventory

%postun
%python_uninstall_alternative openstack-inventory

%check
export OS_LOG_CAPTURE=true
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/openstack-inventory
%{python_sitelib}/openstack
%{python_sitelib}/*.egg-info

%files -n python-openstacksdk-doc
%license LICENSE
%doc doc/build/html

%changelog
