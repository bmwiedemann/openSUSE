#
# spec file for package python-pudb
#
# Copyright (c) 2022 SUSE LLC
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


%define upstream_name pudb
%define module_name pudb
%define py_maj_ver %(c=%{python})
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-pudb
Version:        2022.1.3
Release:        0
Summary:        A full-screen, console-based Python debugger
License:        MIT
Group:          Development/Tools/Debuggers
URL:            https://mathema.tician.de/software/pudb
Source0:        https://files.pythonhosted.org/packages/source/p/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urwid}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments
Requires:       python-urwid
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
PuDB is a full-screen, console-based visual debugger for Python.
Control is by keyboard. The UI is reminiscient of the DOS versions
of Turbo Pascal.

%prep
%setup -q -n %{upstream_name}-%{version}

sed -i '1{\@^#! %{_bindir}/env python@d}' pudb/debugger.py

%build
%python_build

%install
%python_install
mv -v %{buildroot}%{_bindir}/pudb{*,} || /bin/true
%python_clone -a %{buildroot}%{_bindir}/pudb
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
# Since /usr/bin/pudb became ghosted to be used with
# update-alternatives, we have to get rid of the old binary resulting
# from the non-update-alternatives-ified package:
[ -h %{_bindir}/pudb ] || rm -vf %{_bindir}/pudb

%post
%python_install_alternative pudb

%postun
%python_uninstall_alternative pudb

%check
export LC_ALL=en_US.utf8
# https://github.com/inducer/pudb/issues/304
%pytest -k 'not test_get_lines'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{module_name}
%{python_sitelib}/%{module_name}*.egg-info
%python_alternative %{_bindir}/pudb

%changelog
