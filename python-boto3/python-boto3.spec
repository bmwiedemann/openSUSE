#
# spec file for package python-boto3
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
Name:           python-boto3
Version:        1.9.213
Release:        0
Summary:        Amazon Web Services Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/boto/boto3
Source:         https://github.com/boto/boto3/archive/%{version}.tar.gz
# Related test dependencies
BuildRequires:  %{python_module botocore < 1.13.0}
BuildRequires:  %{python_module botocore >= 1.12.213}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module s3transfer < 0.3.0}
BuildRequires:  %{python_module s3transfer >= 0.2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-botocore < 1.13.0
Requires:       python-botocore >= 1.12.213
Requires:       python-jmespath < 1.0.0
Requires:       python-jmespath >= 0.7.1
Requires:       python-s3transfer < 0.3.0
Requires:       python-s3transfer >= 0.2.0
Requires:       python-six
BuildArch:      noarch
%if 0%{?suse_version} <= 1315
# We need the ssl module, which is delivers by python and not python-base
BuildRequires:  python
%endif
%ifpython2
BuildRequires:  python2-futures
Requires:       python2-futures
%endif
%python_subpackages

%description
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use of
services like Amazon S3 and Amazon EC2.

For documentation consult the online documentation at
http://boto3.readthedocs.org/en/latest/

# Note to maintainers also familia with python-boto:
# The documentation generation requires access to AWS, thus it is not
# possible to generate the documentation in OBS

%prep
%setup -q -n boto3-%{version}
sed -i 's/from botocore.vendored //' boto3/compat.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix} -v tests/unit

%files %{python_files}
%license LICENSE
%doc CONTRIBUTING.rst README.rst
%{python_sitelib}/*

%changelog
