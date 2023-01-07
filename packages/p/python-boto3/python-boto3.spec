#
# spec file for package python-boto3
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-boto3
Version:        1.26.42
Release:        0
Summary:        Amazon Web Services Library
License:        Apache-2.0
URL:            https://github.com/boto/boto3
Source:         https://github.com/boto/boto3/archive/%{version}.tar.gz
# Related test dependencies
BuildRequires:  %{python_module botocore < 1.30.0}
BuildRequires:  %{python_module botocore >= 1.29.41}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module s3transfer < 0.7.0}
BuildRequires:  %{python_module s3transfer >= 0.6.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-botocore < 1.30.0
Requires:       python-botocore >= 1.29.41
Requires:       python-jmespath < 2.0.0
Requires:       python-jmespath >= 0.7.1
Requires:       python-s3transfer < 0.7.0
Requires:       python-s3transfer >= 0.6.0
Requires:       python-six
BuildArch:      noarch
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
%pytest --ignore tests/integration -k "not no_bare_six_imports"

%files %{python_files}
%license LICENSE
%doc CONTRIBUTING.rst README.rst
%{python_sitelib}/*

%changelog
