#
# spec file for package python-scandir
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
Name:           python-scandir
Version:        1.10.0
Release:        0
Summary:        Scandir, a better directory iterator and faster oswalk
License:        BSD-3-Clause
URL:            https://github.com/benhoyt/scandir
Source:         https://files.pythonhosted.org/packages/source/s/scandir/scandir-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
``scandir()`` is a directory iteration function like ``os.listdir()``,
except that instead of returning a list of bare filenames, it yields
``DirEntry`` objects that include file type and stat information along
with the name. Using ``scandir()`` increases the speed of ``os.walk()``
by 2-20 times (depending on the platform and file system) by avoiding
unnecessary calls to ``os.stat()`` in most cases.

``scandir`` has been included in the Python 3.5 standard library as
``os.scandir()``, and the related performance improvements to
``os.walk()`` have also been included. So if you're lucky enough to be
using Python 3.5 (release date September 13, 2015) you get the benefit
immediately, otherwise just
`download this module from PyPI <https://pypi.python.org/pypi/scandir>`_,
install it with ``pip install scandir``, and then do something like
this in your code::

    # Use the built-in version of scandir/walk if possible, otherwise
    # use the scandir module version
    try:
        from os import scandir, walk
    except ImportError:
        from scandir import scandir, walk

`PEP 471 <https://www.python.org/dev/peps/pep-0471/>`_, which is the
PEP that proposes including ``scandir`` in the Python standard library,
was `accepted <https://mail.python.org/pipermail/python-dev/2014-July/135561.html>`_
in July 2014 by Victor Stinner, the BDFL-delegate for the PEP.

This ``scandir`` module is intended to work on Python 2.6+ and Python
3.2+ (and it has been tested on those versions).

%prep
%setup -q -n scandir-%{version}
rm -rf scandir.egg-info
dos2unix LICENSE.txt README.rst

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LANG=en_US.UTF-8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python test/run_tests.py

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitearch}/*

%changelog
