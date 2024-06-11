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


%if 0%{?suse_version} >= 1600
%define pythons %{primary_python}
%else
%define pythons python311
%endif
%global _sitelibdir %{%{pythons}_sitelib}

Name:           aws-cli
Version:        1.33.4
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
BuildRequires:  %{pythons}-devel
BuildRequires:  %{pythons}-pip
BuildRequires:  %{pythons}-setuptools
BuildRequires:  %{pythons}-wheel
Requires:       %{pythons}
Requires:       %{pythons}-botocore >= 1.34.122
Requires:       %{pythons}-six
Requires:       (%{pythons}-PyYAML >= 3.10 with %{pythons}-PyYAML <= 6.1)
Requires:       (%{pythons}-colorama >= 0.2.5 with %{pythons}-colorama <= 0.5.0)
Requires:       (%{pythons}-docutils >= 0.10 with %{pythons}-docutils < 0.21)
Requires:       (%{pythons}-rsa >= 3.1.2 with %{pythons}-rsa < 5.0.0)
Requires:       (%{pythons}-s3transfer >= 0.10.0 with %{pythons}-s3transfer < 0.11.0)

%description
The AWS Command Line Interface (CLI) is a unified tool to manage AWS
services. With this tool, multiple AWS services can be controlled
from the command line and automated through scripts.

%prep
%autosetup -p1
sed -i 's/from botocore\.vendored //' awscli/customizations/awslambda.py
sed -i 's/botocore\.vendored\.//' awscli/customizations/configure/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
find %{buildroot}%{_sitelibdir}/awscli/examples -type f -exec chmod 644 {} \;
# No DOS crap
rm %{buildroot}/%{_bindir}/aws.cmd
# Shell completion
install -DTm644 %{buildroot}%{_bindir}/aws_bash_completer %{buildroot}%{_datadir}/bash-completion/completions/aws
install -DTm644 %{buildroot}%{_bindir}/aws_zsh_completer.sh %{buildroot}%{_sysconfdir}/zsh_completion.d/_aws

%files
%defattr(-, root, root)
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%dir %{_sitelibdir}/awscli
%dir %{_sitelibdir}/awscli-%{version}*-info
%{_sitelibdir}/awscli/*
%{_sitelibdir}/awscli-%{version}*-info/*
%{_bindir}/aws
%{_bindir}/aws_completer
%exclude %{_bindir}/aws_bash_completer
%exclude %{_bindir}/aws_zsh_completer.sh
%{_datadir}/bash-completion/completions/aws
%dir %{_sysconfdir}/zsh_completion.d
%config %attr(644,root,root) %{_sysconfdir}/zsh_completion.d/_aws

%changelog
