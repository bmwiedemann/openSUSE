#
# spec file for package aws-cli
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


Name:           aws-cli
Version:        1.32.31
Release:        0
Summary:        Amazon Web Services Command Line Interface
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/aws/aws-cli
Source0:        https://github.com/aws/%{name}/archive/refs/tags/%{version}.tar.gz
Patch0:         ac_update-docutils.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       groff
Provides:       awscli = %{version}
BuildArch:      noarch
BuildRequires:  python311-devel
BuildRequires:  python311-pip
BuildRequires:  python311-setuptools
BuildRequires:  python311-wheel
Requires:       python311
Requires:       python311-botocore >= 1.34.31
Requires:       python311-six
Requires:       (python311-PyYAML >= 3.10 with python311-PyYAML <= 6.1)
Requires:       (python311-colorama >= 0.2.5 with python311-colorama <= 0.5.0)
Requires:       (python311-docutils >= 0.10 with python311-docutils < 0.21)
Requires:       (python311-rsa >= 3.1.2 with python311-rsa < 5.0.0)
Requires:       (python311-s3transfer >= 0.10.0 with python311-s3transfer < 0.11.0)

%description
The AWS Command Line Interface (CLI) is a unified tool to manage AWS
services. With this tool, multiple AWS services can be controlled
from the command line and automated through scripts.

%prep
%setup -q
%patch0 -p1
sed -i 's/from botocore\.vendored //' awscli/customizations/awslambda.py
sed -i 's/botocore\.vendored\.//' awscli/customizations/configure/__init__.py
find . -type f | xargs grep -l '/usr/bin/env' | xargs sed -i 's/env python/python3.11/'

%build
#python3.11 setup.py build
%python311_pyproject_wheel

%install
#python3.11 setup.py install --prefix=%{_prefix} --root=%{buildroot} --install-scripts=%{_bindir}
%python311_pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
find %{buildroot}%{python311_sitelib}/awscli/examples -type f -exec chmod 644 {} \;
# No DOS crap
rm %{buildroot}/%{_bindir}/aws.cmd
# Shell completion
install -DTm644 %{buildroot}%{_bindir}/aws_bash_completer %{buildroot}%{_datadir}/bash-completion/completions/aws
install -DTm644 %{buildroot}%{_bindir}/aws_zsh_completer.sh %{buildroot}%{_sysconfdir}/zsh_completion.d/_aws

%files
%defattr(-, root, root)
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%dir %{python311_sitelib}/awscli
%dir %{python311_sitelib}/awscli-%{version}*-info
%{python311_sitelib}/awscli/*
%{python311_sitelib}/awscli-%{version}*-info/*
%{_bindir}/aws
%{_bindir}/aws_completer
%exclude %{_bindir}/aws_bash_completer
%exclude %{_bindir}/aws_zsh_completer.sh
%{_datadir}/bash-completion/completions/aws
%dir %{_sysconfdir}/zsh_completion.d
%config %attr(644,root,root) %{_sysconfdir}/zsh_completion.d/_aws

%changelog
