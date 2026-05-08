#
# spec file for package python-Timed-Threads
#
# Copyright (c) 2026 SUSE LLC
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


%define modname timed_threads
Name:           python-Timed-Threads
Version:        2.0.0
Release:        0
Summary:        Absolute time deadlines and thread cancelling for Python asynchronous threads
License:        MIT
URL:            https://github.com/Mathics3/python-timed-threads/
Source:         https://files.pythonhosted.org/packages/source/T/Timed-Threads/timed_threads-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A python module that adds the ability to set relative elapsed time deadlines on
asynchronous threads, and allows one thread to stop another by means of raising
an exception.

The main motivation of this module is to support TimedConstraint in the
open-source implementation of Mathematica, called Mathics3.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}*.*-info/

%changelog
