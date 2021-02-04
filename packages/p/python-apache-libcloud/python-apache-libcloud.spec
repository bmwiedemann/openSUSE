#
# spec file for package python-apache-libcloud
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


# No longer build for python2
%define skip_python2 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-apache-libcloud
Version:        3.3.1
Release:        0
Summary:        Abstraction over multiple cloud provider APIs
License:        Apache-2.0
Group:          Development/Languages/Python 
URL:            https://libcloud.apache.org
Source0:        https://files.pythonhosted.org/packages/source/a/apache-libcloud/apache-libcloud-%{version}.tar.gz
Patch1:         gce_image_projects.patch
Patch2:         ec2_create_node.patch
Patch3:         skip-some-tests-for-older-paramiko-versions.patch

BuildRequires:  %{python_module libvirt-python}
BuildRequires:  %{python_module lockfile}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest-runner}
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
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
# Skip ShellOutSSHClientTests tests which attempt to ssh to localhost
# Skip test_key_file_non_pem_format_error since OpenSSH support is backported for SLE python-paramiko < 2.7.0
# Note these four extra py3 failures are undesirable and should be fixed: fail in s390 and ppc64
%pytest -k '(not test_consume_stderr_chunk_contains_part_of_multi_byte_utf8_character and not test_consume_stdout_chunk_contains_part_of_multi_byte_utf8_character and not test_consume_stdout_chunk_contains_non_utf8_character and not test_consume_stderr_chunk_contains_non_utf8_character and not test_key_file_non_pem_format_error and not ShellOutSSHClientTests and not ElasticContainerDriverTestCase and not test_list_nodes_invalid_region)'

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst demos/ example_*.py
%{python_sitelib}/*

%changelog
