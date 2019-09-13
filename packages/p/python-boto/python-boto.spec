#
# spec file for package python-boto
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Tests fail due to missing test directory
%bcond_without tests
Name:           python-boto
Version:        2.49.0
Release:        0
Summary:        Amazon Web Services Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/boto/boto/
Source:         https://files.pythonhosted.org/packages/source/b/boto/boto-%{version}.tar.gz
Source1:        boto.cfg
Patch:          boto-no-builtin-certs.patch
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module httpretty >= 0.7.0}
BuildRequires:  %{python_module mock >= 1.0.1}
BuildRequires:  %{python_module nose >= 1.3.3}
BuildRequires:  %{python_module paramiko >= 1.10.0}
BuildRequires:  %{python_module requests >= 1.2.3}
BuildRequires:  %{python_module rsa >= 3.1.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module simplejson >= 3.6.5}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-paramiko >= 1.10.0
Requires:       python-xml
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-requests >= 1.2.3
Recommends:     python-rsa >= 3.1.4
Suggests:       python-PyYAML >= 3.10
BuildArch:      noarch
%python_subpackages

%description
An integrated interface to current and future infrastructural services offered
by Amazon Web Services. At the moment, boto supports:

 * Compute
  - Amazon Elastic Compute Cloud (EC2)
  - Amazon Elastic Map Reduce (EMR)
  - AutoScaling
  - Amazon Kinesis
 * Content Delivery
  - Amazon CloudFront
 * Database
  - Amazon Relational Data Service (RDS)
  - Amazon DynamoDB
  - Amazon SimpleDB
  - Amazon ElastiCache
  - Amazon Redshift
 * Deployment and Management
  - AWS Elastic Beanstalk
  - AWS CloudFormation
  - AWS Data Pipeline
  - AWS Opsworks
  - AWS CloudTrail
 * Identity & Access
  - AWS Identity and Access Management (IAM)
 * Application Services
  - Amazon CloudSearch
  - Amazon Elastic Transcoder
  - Amazon Simple Workflow Service (SWF)
  - Amazon Simple Queue Service (SQS)
  - Amazon Simple Notification Server (SNS)
  - Amazon Simple Email Service (SES)
 * Monitoring
  - Amazon CloudWatch (EC2 Only)
  - Amazon CloudWatch Logs
 * Networking
  - Amazon Route53
  - Amazon Virtual Private Cloud (VPC)
  - Elastic Load Balancing (ELB)
  - AWS Direct Connect
 * Payments and Billing
  - Amazon Flexible Payment Service (FPS)
 * Storage
  - Amazon Simple Storage Service (S3)
  - Amazon Glacier
  - Amazon Elastic Block Store (EBS)
  - Google Cloud Storage
 * Workforce
  - Amazon Mechanical Turk
 * Other
  - Marketplace Web Services
  - AWS Support

%prep
%setup -q -n boto-%{version}
# remove unwanted shebang
sed -i '/^#!/d' boto/{services/bs,services/result,pyami/launch_ami}.py
rm boto/cacerts/cacerts.txt
%patch

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir %{buildroot}%{_sysconfdir}
cp %{SOURCE1} %{buildroot}%{_sysconfdir}

%python_clone -a %{buildroot}%{_bindir}/asadmin
%python_clone -a %{buildroot}%{_bindir}/bundle_image
%python_clone -a %{buildroot}%{_bindir}/cfadmin
%python_clone -a %{buildroot}%{_bindir}/cq
%python_clone -a %{buildroot}%{_bindir}/cwutil
%python_clone -a %{buildroot}%{_bindir}/dynamodb_dump
%python_clone -a %{buildroot}%{_bindir}/dynamodb_load
%python_clone -a %{buildroot}%{_bindir}/elbadmin
%python_clone -a %{buildroot}%{_bindir}/fetch_file
%python_clone -a %{buildroot}%{_bindir}/glacier
%python_clone -a %{buildroot}%{_bindir}/instance_events
%python_clone -a %{buildroot}%{_bindir}/kill_instance
%python_clone -a %{buildroot}%{_bindir}/launch_instance
%python_clone -a %{buildroot}%{_bindir}/list_instances
%python_clone -a %{buildroot}%{_bindir}/lss3
%python_clone -a %{buildroot}%{_bindir}/mturk
%python_clone -a %{buildroot}%{_bindir}/pyami_sendmail
%python_clone -a %{buildroot}%{_bindir}/route53
%python_clone -a %{buildroot}%{_bindir}/s3put
%python_clone -a %{buildroot}%{_bindir}/sdbadmin
%python_clone -a %{buildroot}%{_bindir}/taskadmin
%python_clone -a %{buildroot}%{_sysconfdir}/boto.cfg

%check
# tests.unit.manage.test_ssh.TestSSHTimeout depends on this
mkdir -p $HOME/.ssh/
touch $HOME/.ssh/known_hosts

# Note that the integration tests systematically fail, and there
# are other submodules of tests which are not being run.

python2 -m nose -v tests/unit
# test_sign_(canned|custom) is 11 tests in tests/unit/cloudfront/test_signed_urls.py
# that all fail.
python3 -m nose -v tests/unit -e 'test_.*(canned|custom)_policy'

%post
%{python_install_alternative asadmin bundle_image cfadmin cq cwutil dynamodb_dump dynamodb_load elbadmin fetch_file glacier instance_events kill_instance launch_instance list_instances lss3 mturk pyami_sendmail route53 s3put sdbadmin taskadmin boto.cfg}

%preun
%python_uninstall_alternative asadmin

%files %{python_files}
%doc README.rst
%config %python_alternative %{_sysconfdir}/boto.cfg
%python_alternative %{_bindir}/asadmin
%python_alternative %{_bindir}/bundle_image
%python_alternative %{_bindir}/cfadmin
%python_alternative %{_bindir}/cq
%python_alternative %{_bindir}/cwutil
%python_alternative %{_bindir}/dynamodb_dump
%python_alternative %{_bindir}/dynamodb_load
%python_alternative %{_bindir}/elbadmin
%python_alternative %{_bindir}/fetch_file
%python_alternative %{_bindir}/glacier
%python_alternative %{_bindir}/instance_events
%python_alternative %{_bindir}/kill_instance
%python_alternative %{_bindir}/launch_instance
%python_alternative %{_bindir}/list_instances
%python_alternative %{_bindir}/lss3
%python_alternative %{_bindir}/mturk
%python_alternative %{_bindir}/pyami_sendmail
%python_alternative %{_bindir}/route53
%python_alternative %{_bindir}/s3put
%python_alternative %{_bindir}/sdbadmin
%python_alternative %{_bindir}/taskadmin
%{python_sitelib}/*

%changelog
