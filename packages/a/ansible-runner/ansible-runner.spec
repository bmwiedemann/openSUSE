#
# spec file for package python-ansible-runner
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/

Name:           ansible-runner
Version:        1.3.4
Release:        0
License:        Apache-2.0 and GPL-3.0-or-later
Summary:        Package for interfacing with Ansible
Url:            https://github.com/ansible/ansible-runner
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/ansible-runner/ansible-runner-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-Use-the-correct-python-executable-for-tests.patch -- https://github.com/ansible/ansible-runner/pull/290
Patch0:         0001-Use-the-correct-python-executable-for-tests.patch
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-pexpect
BuildRequires:  python3-psutil
BuildRequires:  python3-PyYAML
BuildRequires:  python3-python-daemon
BuildRequires:  python3-six
Requires:       python3-pexpect >= 4.5
Requires:       python3-psutil
Requires:       python3-python-daemon
Requires:       python3-PyYAML
Requires:       python3-six >= 1.12
BuildArch:      noarch

%description
Ansible Runner is a tool and python library that helps when interfacing with
Ansible directly or as part of another system whether that be through a
container image interface, as a standalone tool, or as a Python module that
can be imported. The goal is to provide a stable and consistent interface
abstraction to Ansible. This allows Ansible to be embedded into other
systems that don’t want to manage the complexities of the interface on
their own (such as CI/CD platforms, Jenkins, or other automated tooling)

%prep
%setup -q -n ansible-runner-%{version}
%patch0 -p1

%build
%python3_build

%install
%python3_install
# dont polute the namespace with tests
rm -r %{buildroot}%{python3_sitelib}/test/

%check
py.test -v test

%files
%doc README.md
%license LICENSE.md
%{_bindir}/ansible-runner
%{python3_sitelib}/ansible_runner
%{python3_sitelib}/ansible_runner-%{version}-py*.egg-info

%changelog
