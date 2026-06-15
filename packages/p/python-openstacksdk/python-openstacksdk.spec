#
# spec file for package python-openstacksdk
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        4.15.0
Release:        0
Summary:        An SDK for building applications to work with OpenStack
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/openstacksdk
Source0:        https://files.pythonhosted.org/packages/source/o/openstacksdk/openstacksdk-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.13}
BuildRequires:  %{python_module cryptography >= 2.7}
BuildRequires:  %{python_module ddt >= 1.0.1}
BuildRequires:  %{python_module decorator >= 4.4.1}
BuildRequires:  %{python_module deprecation}
BuildRequires:  %{python_module dogpile.cache >= 0.6.5}
BuildRequires:  %{python_module fixtures >= 3.0.0}
BuildRequires:  %{python_module iso8601 >= 0.1.11}
BuildRequires:  %{python_module jmespath >= 0.9.0}
BuildRequires:  %{python_module jsonpatch >= 1.16}
BuildRequires:  %{python_module jsonschema >= 3.2.0}
BuildRequires:  %{python_module keyring >= 24.0.0}
BuildRequires:  %{python_module keystoneauth1 >= 5.12.0}
BuildRequires:  %{python_module os-service-types >= 1.8.1}
BuildRequires:  %{python_module oslo.config >= 6.1.0}
BuildRequires:  %{python_module oslotest >= 3.2.0}
BuildRequires:  %{python_module pbr >= 6.1.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs >= 3}
BuildRequires:  %{python_module prometheus_client >= 0.4.2}
BuildRequires:  %{python_module psutil >= 3.2.2}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module requests-mock >= 1.2.0}
BuildRequires:  %{python_module statsd >= 3.3.0}
BuildRequires:  %{python_module stestr >= 1.0.0}
BuildRequires:  %{python_module stevedore}
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  %{python_module testtools >= 2.2.0}
BuildRequires:  %{python_module typing-extensions >= 4.12.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PyYAML >= 3.13
Requires:       python-cryptography >= 2.7
Requires:       python-decorator >= 4.4.1
Requires:       python-dogpile.cache >= 0.6.5
Requires:       python-iso8601 >= 0.1.11
Requires:       python-jmespath >= 0.9.0
Requires:       python-jsonpatch >= 1.16
Requires:       python-keystoneauth1 >= 5.10.0
Requires:       python-os-service-types >= 1.8.1
Requires:       python-platformdirs >= 3
Requires:       python-psutil >= 3.2.2
Requires:       python-typing-extensions >= 4.12.0
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-openstacksdk < %{version}
%else
Conflicts:      python3-openstacksdk < %{version}
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
%autosetup -p1 -n openstacksdk-%{version}

%build
%pyproject_wheel
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/openstack-inventory

%pre
%python_libalternatives_reset_alternative openstack-inventory

%post
%python_install_alternative openstack-inventory

%postun
%python_uninstall_alternative openstack-inventory

%check
export OS_LOG_CAPTURE=true
export OS_TEST_TIMEOUT=30
rm -v openstack/tests/unit/test_hacking.py
rm -v openstack/tests/unit/test_utils.py
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/openstack-inventory
%{python_sitelib}/openstack
%{python_sitelib}/openstacksdk-%{version}.dist-info

%files -n python-openstacksdk-doc
%license LICENSE
%doc doc/build/html

%changelog
