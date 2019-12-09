#
# spec file for package python-distob
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
Name:           python-distob
Version:        0.3.3
Release:        0
Summary:        Distributed computing using remote objects
License:        GPL-3.0-or-later
URL:            https://github.com/mattja/distob/
Source:         https://files.pythonhosted.org/packages/source/d/distob/distob-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dill >= 0.2.1
Requires:       python-ipyparallel >= 4.0
Requires:       python-pyzmq >= 2.1.11
Recommends:     python-numpy >= 1.6
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dill >= 0.2.1}
BuildRequires:  %{python_module ipyparallel >= 4.0}
BuildRequires:  %{python_module numpy >= 1.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq >= 2.1.11}
# /SECTION
%python_subpackages

%description
Distob will take your existing python objects, or a sequence of
objects, and scatter them onto many IPython parallel engines, which
may be running on a single computer or on a cluster.

In place of the original objects, proxy objects are kept on the client
computer that provide the same interface as the original objects. You
can continue to use these as if the objects were still local. All
methods are passed through to the remote objects, where computation is
done.

In particular, sending numpy arrays to the cluster is supported.

A numpy array can also be scattered across the cluster, along a
particular axis. Operations on the array can then be automatically
done in parallel.

%prep
%setup -q -n distob-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
