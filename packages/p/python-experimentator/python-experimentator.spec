#
# spec file for package python-experimentator
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
%define         skip_python2 1
%bcond_without  test
Name:           python-experimentator
Version:        0.3.1
Release:        0
Summary:        Experiment builder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hsharrison/experimentator
Source:         https://files.pythonhosted.org/packages/source/e/experimentator/experimentator-%{version}.tar.gz
# PATCH-FIX-UPSTREAM support_networkX_2.patch -- Support networkX 2.0
# gh#hsharrison/experimentator#24
Patch0:         support_networkX_2.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-docopt
Requires:       python-networkx >= 2
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-schema
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module schema}
%endif
%python_subpackages

%description
Do you write code to run experiments? If so, you've probably had the
experience of sitting down to code an experiment but getting
side-tracked by all the logistics: crossing your independent
variables to form conditions, repeating your conditions,
randomization, storing intermediate data, etc. It's frustrating to
put all that effort in before even getting to what's really unique
about your experiment. Worse, it encourages bad coding practices
like copy-pasting boilerplate from someone else's experiment code
without understanding it.

The purpose of experimentator is to handle all the boring logistics
of running experiments and allow you to get straight to what really
interests you, whatever that may be. This package was originally
intended for behavioral experiments in which human participants are
interacting with a graphical interface, but there is nothing
domain-specific about it--it should be useful for anyone running
experiments with a computer. You might say that experimentator*is a
library for 'repeatedly calling a function while systematically
varying its inputs and saving the data' (although that doesn't do it
full justice).

%prep
%setup -q -n experimentator-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/exp

%if %{with test}
%check
# gh#hsharrison/experimentator#25
%pytest --disable-warnings -k 'not test_round_trip'
%endif

%post
%python_install_alternative exp

%postun
%python_uninstall_alternative exp

%files %{python_files}
%license LICENSE.rst
%doc README.rst changes.rst
%python_alternative %{_bindir}/exp
%{python_sitelib}/*

%changelog
