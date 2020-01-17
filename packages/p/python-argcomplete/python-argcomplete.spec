#
# spec file for package python-argcomplete
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-argcomplete
Version:        1.11.1
Release:        0
Summary:        Bash tab completion for argparse
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/kislyuk/argcomplete
Source:         https://files.pythonhosted.org/packages/source/a/argcomplete/argcomplete-%{version}.tar.gz
Patch0:         skip_tcsh_tests.patch
Patch1:         trim-test-deps.patch
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  fish
BuildRequires:  python-rpm-macros
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
%setup -q -n argcomplete-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
rm -rf %{buildroot}%{python_sitelib}/test
rm %{buildroot}%{_bindir}/activate-global-python-argcomplete
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# tcsh support is broken
rm %{buildroot}%{_bindir}/python-argcomplete-tcsh

%check
export LANG=en_US.UTF-8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/argcomplete-%{version}-py%{python_version}.egg-info
%{python_sitelib}/argcomplete
%python3_only %{_bindir}/python-argcomplete-check-easy-install-script
%python3_only %{_bindir}/register-python-argcomplete

%changelog
