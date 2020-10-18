#
# spec file for package python-Fabric
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
Name:           python-Fabric
Version:        2.5.0
Release:        0
Summary:        A Pythonic tool for remote execution and deployment
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://fabfile.org
Source:         https://files.pythonhosted.org/packages/source/f/fabric/fabric-%{version}.tar.gz
# fix executable in tests
Patch0:         fix-executable.patch
BuildRequires:  %{python_module cryptography >= 1.1}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module invoke >= 1.3}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module paramiko >= 2.4}
BuildRequires:  %{python_module pytest-relaxed}
# gh#bitprophet/pytest-relaxed#12
BuildRequires:  %{python_module pytest < 6.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 1.1
Requires:       python-decorator
Requires:       python-invoke >= 1.3
Requires:       python-paramiko >= 2.4
Requires:       python-setuptools
Requires:       python-six
Conflicts:      python-Fabric3
Provides:       python-Fabric2 = %{version}
Provides:       python-Fabric3 = %{version}
Provides:       python-Fabric3 = %{version}
Provides:       python-fabric = %{version}
Provides:       python-fabric2 = %{version}
Provides:       python-fabric2 = %{version}
BuildArch:      noarch
%python_subpackages

%description
Fabric is a Python library and command-line tool for
streamlining the use of SSH for application deployment or systems
administration tasks.

It provides a basic suite of operations for executing local or remote shell
commands (normally or via sudo) and uploading/downloading files, as well as
auxiliary functionality such as prompting the running user for input, or
aborting execution.

In addition to being used via the fab tool, Fabric's components may be imported
into other Python code, providing a Pythonic interface to the SSH protocol
suite at a higher level than that provided by e.g. Paramiko (which
Fabric itself leverages).

%prep
%setup -q -n fabric-%{version}
# fix all imports:
sed -i 's/from invoke.vendor\./from\ /' fabric/connection.py fabric/group.py integration/concurrency.py tests/config.py tests/transfer.py tests/_util.py tests/connection.py tests/runners.py
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/fab

%check
%pytest tests/

%post
%python_install_alternative fab

%postun
%python_uninstall_alternative fab

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/fab
%{python_sitelib}/*

%changelog
