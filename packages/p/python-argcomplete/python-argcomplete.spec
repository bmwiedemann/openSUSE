#
# spec file for package python-argcomplete
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013 Darin Perusich.
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


%{?sle15_python_module_pythons}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-argcomplete%{psuffix}
Version:        3.5.2
Release:        0
Summary:        Bash tab completion for argparse
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/kislyuk/argcomplete
Source:         https://files.pythonhosted.org/packages/source/a/argcomplete/argcomplete-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 67.2}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module argcomplete == %{version}}
BuildRequires:  %{python_module pexpect}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  fish
BuildRequires:  zsh
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

* You're using bash as your shell
* You're using argparse to manage your command line arguments/options

Argcomplete is particularly useful if your program has lots of options
or subparsers, and if your program can dynamically suggest completions
for your argument/option values (for example, if the user is browsing
resources over the network).

%prep
%autosetup -p1 -n argcomplete-%{version}

%build
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/activate-global-python-argcomplete
%python_clone -a %{buildroot}%{_bindir}/register-python-argcomplete
%python_clone -a %{buildroot}%{_bindir}/python-argcomplete-check-easy-install-script
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
export TERM=xterm-mono
%{python_expand \
  # https://github.com/kislyuk/argcomplete/issues/255
  # https://github.com/kislyuk/argcomplete/issues/299
  sed -i -e "1s|#!.*python.*|#!%{__$python}|" test/prog test/*.py
  sed -i -e "s|python3 |$python |g" test/test.py
  $python ./test/test.py -v
}
%endif

%if %{without test}
%post
%python_install_alternative activate-global-python-argcomplete
%python_install_alternative register-python-argcomplete
%python_install_alternative python-argcomplete-check-easy-install-script

%postun
%python_uninstall_alternative activate-global-python-argcomplete
%python_uninstall_alternative register-python-argcomplete
%python_uninstall_alternative python-argcomplete-check-easy-install-script

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/argcomplete-%{version}.dist-info
%{python_sitelib}/argcomplete
%python_alternative %{_bindir}/activate-global-python-argcomplete
%python_alternative %{_bindir}/python-argcomplete-check-easy-install-script
%python_alternative %{_bindir}/register-python-argcomplete
%endif

%changelog
