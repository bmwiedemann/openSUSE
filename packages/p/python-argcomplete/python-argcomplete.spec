#
# spec file for package python-argcomplete
#
# Copyright (c) 2023 SUSE LLC
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


%global skip_python2 1
Name:           python-argcomplete
Version:        2.0.0
Release:        0
Summary:        Bash tab completion for argparse
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/kislyuk/argcomplete
Source:         https://files.pythonhosted.org/packages/source/a/argcomplete/argcomplete-%{version}.tar.gz
Patch0:         skip_tcsh_tests.patch
Patch1:         trim-test-deps.patch
# PATCH-FIX-UPSTREAM without_fish.patch gh#kislyuk/argcomplete!410 mcepl@suse.com
# Don't fail the test suite when fish is not available
Patch2:         without_fish.patch
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/register-python-argcomplete
%python_clone -a %{buildroot}%{_bindir}/python-argcomplete-check-easy-install-script
rm -rf %{buildroot}%{python_sitelib}/test
rm %{buildroot}%{_bindir}/activate-global-python-argcomplete
# tcsh support is broken
rm %{buildroot}%{_bindir}/python-argcomplete-tcsh
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%{python_expand \
  # https://github.com/kislyuk/argcomplete/issues/255
  # https://github.com/kislyuk/argcomplete/issues/256
  # https://github.com/kislyuk/argcomplete/issues/299
  sed -i -e "1s|#!.*python.*|#!%{_bindir}/$python|" test/prog scripts/*
  sed -i -e "s|python3 |$python |g" test/test.py
  PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -v
}

%post
%python_install_alternative register-python-argcomplete
%python_install_alternative python-argcomplete-check-easy-install-script

%postun
%python_uninstall_alternative register-python-argcomplete
%python_uninstall_alternative python-argcomplete-check-easy-install-script

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/argcomplete-%{version}*-info
%{python_sitelib}/argcomplete
%python_alternative %{_bindir}/python-argcomplete-check-easy-install-script
%python_alternative %{_bindir}/register-python-argcomplete

%changelog
