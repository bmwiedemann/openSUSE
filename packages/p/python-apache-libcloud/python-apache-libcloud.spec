#
# spec file for package python-apache-libcloud
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


# No longer build for python2
%define skip_python2 1
Name:           python-apache-libcloud
Version:        3.7.0
Release:        0
Summary:        Abstraction over multiple cloud provider APIs
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://libcloud.apache.org
Source0:        https://downloads.apache.org/libcloud/apache-libcloud-%{version}.tar.bz2
Source1:        https://downloads.apache.org/libcloud/apache-libcloud-%{version}.tar.bz2.asc
# https://libcloud.apache.org/downloads.html#package-verification-guide
Source2:        https://www.apache.org/dist/libcloud/KEYS#/%{name}.keyring
Patch1:         gce_image_projects.patch
Patch2:         ec2_create_node.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module libvirt-python}
BuildRequires:  %{python_module lockfile}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       python-requests
Requires:       python-typing
Suggests:       python-libvirt-python
Suggests:       python-lockfile
Suggests:       python-paramiko
Suggests:       python-pysphere
BuildArch:      noarch
%python_subpackages

%description
Apache Libcloud is a standard Python library that abstracts away
differences among multiple cloud provider APIs.

%prep
%setup -q -n apache-libcloud-%{version}
%autopatch -p1
sed -i '/^#!/d' demos/gce_demo.py
chmod a-x demos/gce_demo.py
# Setup tests
cp libcloud/test/secrets.py-dist libcloud/test/secrets.py

%build
%python_build

%install
%python_install
find %{buildroot} -name '*.DS_Store' -delete
find %{buildroot} -name '*.json' -size 0 -delete
find %{buildroot} -name '*.pem' -size 0 -delete
%python_expand rm -r %{buildroot}%{$python_sitelib}/libcloud/test
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip OvhTests::test_list_nodes_invalid_region which tries to reach OVH servers
donttest="test_consume_stderr_chunk_contains_part_of_multi_byte_utf8_character"
donttest+=" or test_consume_stdout_chunk_contains_part_of_multi_byte_utf8_character"
donttest+=" or test_consume_stdout_chunk_contains_non_utf8_character"
donttest+=" or test_consume_stderr_chunk_contains_non_utf8_character"
# Skip test_key_file_non_pem_format_error since OpenSSH support is backported for SLE python-paramiko < 2.7.0
donttest+=" or test_key_file_non_pem_format_error"
# Skip ShellOutSSHClientTests tests which attempt to ssh to localhost
donttest+=" or ShellOutSSHClientTests"
# Note these four extra py3 failures are undesirable and should be fixed: fail in s390 and ppc64
donttest+=" or ElasticContainerDriverTestCase"
donttest+=" or test_list_nodes_invalid_region"
donttest+=" or test_connection_timeout_raised"
donttest+=" or test_retry_on_all_default_retry_exception_classes"

# Skip tests broken because requests-mock incompatibility with urllib3 >= 2.0.0
# gh#jamielennox/requests-mock#228
donttest+=" or test_openstack.py"
donttest+=" or test_rackspace.py"
donttest+=" or test_scaleway.py"
donttest+=" or test_vcloud.py"
donttest+=" or test_vultr_v2.py"
donttest+=" or test_aurora.py"
donttest+=" or test_azure_blobs.py"
donttest+=" or test_cloudfiles.py"
donttest+=" or test_google_storage.py"
donttest+=" or test_oss.py"
donttest+=" or test_ovh.py"
donttest+=" or test_s3.py"

%pytest -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst demos/ example_*.py
%{python_sitelib}/*

%changelog
