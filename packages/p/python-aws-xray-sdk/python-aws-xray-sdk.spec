#
# spec file for package python-aws-xray-sdk
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-aws-xray-sdk
Version:        2.6.0
Release:        0
Summary:        The AWS X-Ray SDK for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/aws/aws-xray-sdk-python
Source:         https://files.pythonhosted.org/packages/source/a/aws-xray-sdk/aws-xray-sdk-%{version}.tar.gz
Source9:        %{name}-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-botocore >= 1.11.3
Requires:       python-future
Requires:       python-jsonpickle
Requires:       python-wrapt
%ifpython2
Requires:       python-enum34
%endif
BuildArch:      noarch

%python_subpackages

%description
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

It works through any one of various frameworks, provided by backends. The
following backends are included in the main package:

  * botocore
  * httplib
  * sqlite3
  
Additional backends can be installed by installing %{name}-backend
packages.  The %{name}-all package installs all backends.

%package        all
Summary:        Metapackage to pull in all AWS X-Ray SDK backends
Group:          Metapackages
Requires:       %{name} = %{version}
Recommends:     %{name}-Django = %{version}
Recommends:     %{name}-Flask-SQLAlchemy = %{version}
Recommends:     %{name}-SQLAlchemy = %{version}
Recommends:     %{name}-mysql-connector-python = %{version}
Recommends:     %{name}-pymongo = %{version}
Recommends:     %{name}-pynamodb = %{version}
Recommends:     %{name}-psycopg2 = %{version}
Recommends:     %{name}-requests = %{version}
%ifpython3
Recommends:     %{name}-aiobotocore = %{version}
Recommends:     %{name}-aiohttp = %{version}
%endif

%description    all
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package pulls in all available backends for %{name}.

%package        Django
Summary:        Django backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-Django >= 1.10

%description    Django
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the Django backend for %{name}.

%package        Flask-SQLAlchemy
Summary:        Flask-SQLAlchemy backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       %{name}-SQLAlchemy = %{version}
Requires:       python-Flask-SQLAlchemy
Requires:       python-SQLAlchemy

%description    Flask-SQLAlchemy
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the Flask-SQLAlchemy backend for %{name}.

%package        SQLAlchemy
Summary:        SQLAlchemy backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-SQLAlchemy

%description    SQLAlchemy
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the SQLAlchemy backend for %{name}.

%package        mysql-connector
Summary:        mysql backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-mysql-connector-python

%description    mysql-connector
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the mysql-connector-python backend for %{name}.

%package        pymongo
Summary:        pymongo backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-pymongo

%description    pymongo
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the pymongo backend for %{name}.

%package        pynamodb
Summary:        pynamodb backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-pynamodb

%description    pynamodb
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the pynamodb backend for %{name}.

%package        psycopg2
Summary:        psycopg2 backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-psycopg2

%description    psycopg2
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the psycopg2 backend for %{name}.

%package        requests
Summary:        requests backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-requests

%description    requests
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the requests backend for %{name}.

%package        aiobotocore
Summary:        aiobotocore backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-aiobotocore

%description    aiobotocore
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the aiobotocore backend for %{name}.

%package        aiohttp
Summary:        aiohttp backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-aiohttp >= 2.3

%description    aiohttp
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the aiohttp backend for %{name}.

%prep
%setup -q -n aws-xray-sdk-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/aws_xray_sdk/ext/psycopg2/
%python_expand $python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/aws_xray_sdk/ext/psycopg2/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# python3 only
rm -rf %{buildroot}%{python2_sitelib}/aws_xray_sdk/ext/aiobotocore/
rm -rf %{buildroot}%{python2_sitelib}/aws_xray_sdk/ext/aiohttp/

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*
%exclude %{python_sitelib}/aws_xray_sdk/ext/django/
%exclude %{python_sitelib}/aws_xray_sdk/ext/flask_sqlalchemy/
%exclude %{python_sitelib}/aws_xray_sdk/ext/sqlalchemy/
%exclude %{python_sitelib}/aws_xray_sdk/ext/mysql/
%exclude %{python_sitelib}/aws_xray_sdk/ext/pymongo/
%exclude %{python_sitelib}/aws_xray_sdk/ext/pynamodb/
%exclude %{python_sitelib}/aws_xray_sdk/ext/psycopg2/
%exclude %{python_sitelib}/aws_xray_sdk/ext/requests/
%python3_only %exclude %{python_sitelib}/aws_xray_sdk/ext/aiohttp/
%python3_only %exclude %{python_sitelib}/aws_xray_sdk/ext/aiobotocore/

%files %{python_files all}
%license LICENSE

%files %{python_files Django}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/django/

%files %{python_files Flask-SQLAlchemy}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/flask_sqlalchemy/

%files %{python_files SQLAlchemy}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/sqlalchemy/

%files %{python_files mysql-connector}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/mysql/

%files %{python_files pymongo}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/pymongo/

%files %{python_files pynamodb}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/pynamodb/

%files %{python_files psycopg2}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/psycopg2/

%files %{python_files requests}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/requests/

%ifpython3

%files %{python_files aiobotocore}
%license LICENSE
%{python3_sitelib}/aws_xray_sdk/ext/aiobotocore/

%files %{python_files aiohttp}
%license LICENSE
%{python3_sitelib}/aws_xray_sdk/ext/aiohttp/

%endif

%changelog
