#
# spec file for package python-virtualenv
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-virtualenv%{psuffix}
Version:        16.7.5
Release:        0
Summary:        Virtual Python Environment builder
License:        MIT
Group:          Development/Languages/Python
URL:            http://www.virtualenv.org/
Source:         https://files.pythonhosted.org/packages/source/v/virtualenv/virtualenv-%{version}.tar.gz
%if %{with test}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pypiserver}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module virtualenv >= %{version}}
%endif
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
virtualenv is a tool to create isolated Python environments.
The basic problem being addressed is one of dependencies and versions, and
indirectly permissions. Imagine you have an application that needs version 1
of LibFoo, but another application requires version 2. How can you use both
these applications? If you install everything into
%{_libexecdir}/python2.4/site-packages (or whatever your platforms standard location
is), its easy to end up in a situation where you unintentionally upgrade an
application that shouldnt be upgraded.

Or more generally, what if you want to install an application and leave it be?
If an application works, any change in its libraries or the versions of those
libraries can break the application.

Also, what if you cant install packages into the global site-packages
directory? For instance, on a shared host.

In all these cases, virtualenv can help you. It creates an environment that
has its own installation directories, that doesnt share libraries with other
virtualenv environments (and optionally doesnt use the globally installed
libraries either).

%prep
%setup -q -n virtualenv-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/virtualenv
%endif

%check
%if %{with test}
# test_bootstrap is tied to python2 command calls, skip it
# test_always_copy_option does not handle system install dirs in /usr/lib64
# test_wheel_invocation_dash_p or test_use_from_wheel or test_wheel_contains or test_wheel_basic_invocation; online tests
%pytest -k 'not (test_always_copy_option or test_bootstrap or test_use_from_wheel or test_wheel_contains or test_wheel_basic_invocation or test_wheel_invocation_dash_p)'
%endif

%if !%{with test}
%post
%python_install_alternative virtualenv

%postun
%python_uninstall_alternative virtualenv

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/virtualenv*
%python_alternative %{_bindir}/virtualenv
%pycache_only %{python_sitelib}/__pycache__
%endif

%changelog
