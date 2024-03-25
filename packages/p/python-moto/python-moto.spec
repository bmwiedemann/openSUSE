#
# spec file for package python-moto
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


Name:           python-moto
Version:        5.0.3
Release:        0
Summary:        Library to mock out tests based on AWS
License:        Apache-2.0
URL:            https://github.com/getmoto/moto
Source:         https://files.pythonhosted.org/packages/source/m/moto/moto-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.10.1
Requires:       python-Werkzeug >= 0.5
Requires:       python-boto3 >= 1.9.201
Requires:       python-botocore >= 1.14.0
Requires:       python-cryptography >= 3.3.1
Requires:       python-requests >= 2.5
Requires:       python-responses >= 0.15.0
Requires:       python-xmltodict
Requires:       (python-python-dateutil >= 2.1 with python-python-dateutil < 3)
Conflicts:      (python-Werkzeug >= 2.2.0 with python-Werkzeug < 2.2.2)
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-moto-all
Suggests:       python-moto-server
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask without (%python-Flask >= 2.2.0 with %python-Flask < 2.2.2)}
BuildRequires:  %{python_module Flask-Cors}
BuildRequires:  %{python_module Jinja2 >= 2.10.1}
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module aws-xray-sdk >= 0.93}
BuildRequires:  %{python_module boto3 >= 1.9.201}
BuildRequires:  %{python_module botocore >= 1.14.0}
BuildRequires:  %{python_module cfn-lint >= 0.40.0}
BuildRequires:  %{python_module cryptography >= 3.3.1}
BuildRequires:  %{python_module docker >= 3.0.0}
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module graphql-core}
BuildRequires:  %{python_module joserfc}
BuildRequires:  %{python_module jsondiff >= 1.1.2}
BuildRequires:  %{python_module jsonpickle}
BuildRequires:  %{python_module openapi-spec-validator >= 0.5.0}
BuildRequires:  %{python_module py-partiql-parser >= 0.5}
BuildRequires:  %{python_module pyparsing >= 3.0.7}
BuildRequires:  %{python_module pytest-order}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.1 with %python-python-dateutil < 3}
BuildRequires:  %{python_module python-multipart}
BuildRequires:  %{python_module requests >= 2.5}
BuildRequires:  %{python_module responses >= 0.15.0}
BuildRequires:  %{python_module surer}
BuildRequires:  %{python_module xmltodict}
BuildRequires:  %{python_module Werkzeug >= 0.5 without (%python-Werkzeug >= 2.2.0 with %python-Werkzeug < 2.2.2)}
# /SECTION
%python_subpackages

%description
A library that allows your python tests to mock out AWS Services

%package all
Summary:        Library to mock out the boto library -- all extras
Provides:       python-moto-proxy = %{version}-%{release}
Requires:       python-PyYAML >= 5.1
Requires:       python-aws-xray-sdk >= 0.93
Requires:       python-cfn-lint >= 0.40.0
Requires:       python-docker >= 3.0.0
Requires:       python-ecdsa
Requires:       python-graphql-core
Requires:       python-joserfc
Requires:       python-jsondiff >= 1.1.2
Requires:       python-moto = %{version}
Requires:       python-openapi-spec-validator >= 0.5.0
Requires:       python-py-partiql-parser >= 0.5.0
Requires:       python-pyparsing >= 3.0.7
Requires:       python-python-multipart
Requires:       python-setuptools

%description all
A library that allows your python tests to mock out the boto
library. Meta package to install the extras moto[all], and
moto[proxy], which have the same requirement definitions.

%package server
Summary:        Library to mock out the boto library -- moto[server]
Requires:       python-Flask
Requires:       python-Flask-Cors
Requires:       python-moto-all = %{version}
Conflicts:      (python-Flask >= 2.2.0 with python-Flask < 2.2.2)

%description server
A library that allows your python tests to mock out the boto
library. Meta package to install server extra (moto[server])

%prep
%autosetup -p1 -n moto-%{version}
# avoid zero-length modules
for f in athena/utils.py \
         ec2/regions.py \
         medialive/exceptions.py \
         meteringmarketplace/exceptions.py \
         redshift/utils.py \
         support/exceptions.py
do
   [ -f moto/$f ] || (echo "moto/$f does not exist anymore"; exit 1)
   [ ! -s moto/$f ] || (echo "moto/$f is not empty anymore"; exit 1)
   echo '# empty module' > moto/$f
done
# unpin exact version
sed -i '/py-partiql-parser/ s/==/>=/' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/moto_server
%python_clone -a %{buildroot}%{_bindir}/moto_proxy

%check
export BOTO_CONFIG=/dev/null
# no online tests on obs
donttest="network"
donttest+=" or test_passthrough_calls_for_entire_service"
donttest+=" or test_passthrough_calls_for_specific_url"
donttest+=" or test_passthrough_calls_for_wildcard_urls"
# no connection -- no such file -- we don't have the test containers
donttest+=" or test_terminate_job or test_cancel_running_job or test_cancel_pending_job"
donttest+=" or (test_batch_jobs and (test_dependencies or test_container_overrides))"
donttest+=" or (test_cloudformation_custom_resources and test_create_custom_lambda_resource__verify_cfnresponse_failed)"
donttest+=" or (test_cloudformation_stack_integration and test_lambda_function)"
donttest+=" or test_firehose_put"
donttest+=" or test_vpc_peering_connections_cross_region_fail"
donttest+=" or test_events_lambdatriggers_integration"
donttest+=" or (test_s3_lambda_integration and test_objectcreated_put__invokes_lambda and ObjectCreated)"
donttest+=" or (test_server and test_appsync_list_tags_for_resource)"
donttest+=" or (test_server and test_s3_server_post_to_bucket_redirect)"
donttest+=" or (test_multiple_accounts_server and test_with_custom_request_header)"
donttest+=" or test_docker_is_running_and_available"
donttest+=" or test_s3_server_post_cors_multiple_origins"
donttest+=" or test_invoke_function_from_sqs_exception"
donttest+=" or test_invoke_function_from_sqs_fifo_queue"
donttest+=" or test_invoke_function_from_sqs_queue"
donttest+=" or test_invoke_local_lambda_layers"
donttest+=" or test_failed_job or test_failed_dependencies"
donttest+=" or TestResponsesMockWithPassThru"
# (?)
donttest+=" or test_send_raw_email"
# 32-bit platforms can't handle dates beyond 2038
[ $(getconf LONG_BIT) -eq 32 ] && donttest+=" or test_list_pipelines_created_after"
# see Makefile
deselect_for_parallel=" or test_kinesisvideoarchivedmedia or test_awslambda or test_batch or test_ec2 or test_sqs"
parallel_tests="./tests/test_awslambda ./tests/test_batch ./tests/test_ec2 ./tests/test_sqs"
%pytest -k "not ($donttest ${$python_donttest} $deselect_for_parallel)" tests/
export MOTO_CALL_RESET_API=false
%pytest -n auto -k "not ($donttest ${$python_donttest})" $parallel_tests

%post
%python_install_alternative moto_server moto_proxy

%postun
%python_uninstall_alternative moto_server

%files %{python_files}
%doc AUTHORS.md README.md
%license LICENSE
%python_alternative %{_bindir}/moto_server
%python_alternative %{_bindir}/moto_proxy
%{python_sitelib}/moto
%{python_sitelib}/moto-%{version}.dist-info

%files %{python_files all}
%license LICENSE

%files %{python_files server}
%license LICENSE

%changelog
