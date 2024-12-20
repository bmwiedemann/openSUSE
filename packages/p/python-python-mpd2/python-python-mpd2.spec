#
# spec file for package python-python-mpd2
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


%{?sle15_python_module_pythons}
Name:           python-python-mpd2
Version:        3.1.1
Release:        0
Summary:        A Python MPD client library
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/Mic92/python-mpd2
Source:         https://files.pythonhosted.org/packages/source/p/python-mpd2/python-mpd2-%{version}.tar.gz
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-Twisted
BuildArch:      noarch
%python_subpackages

%description
The python-mpd2 package is a Python library which provides
a client interface for the Music Player Daemon.

python-mpd2 is a fork of python-mpd.  While 0.4.x was backwards compatible
with python-mpd, starting with 0.5 provides enhanced features which are *NOT*
backward compatibles with the original python-mpd package.

%prep
%setup -q -n python-mpd2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v mpd.tests

%files %{python_files}
%license LICENSE.txt
%doc README.rst doc
%{python_sitelib}/python_mpd2-%{version}.dist-info
%{python_sitelib}/mpd

%changelog
