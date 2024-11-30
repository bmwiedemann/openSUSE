#
# spec file for package python-mpi4py
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


%define plainpython python
Name:           python-mpi4py
Version:        4.0.1
Release:        0
Summary:        MPI for Python
License:        BSD-3-Clause
URL:            https://github.com/mpi4py/mpi4py
Source:         https://files.pythonhosted.org/packages/source/m/mpi4py/mpi4py-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  openmpi-macros-devel
BuildRequires:  python-rpm-macros
# SECTION test dependencies
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module cffi}
# /SECTION
%openmpi_requires
%python_subpackages

%description
This package provides Python bindings for the Message Passing
Interface (MPI) standard. It is implemented on top of the MPI-1/2/3
specification and exposes an API which grounds on the standard MPI-2
C++ bindings.

This package supports:
  + Communication of any picklable Python object
    * Point-to-point: send & receive
    * Collective: broadcast, scatter & gather, reductions
  + Communication of Python object exposing the Python buffer
    interface (NumPy arrays, builtin bytes/string/array objects)
    * Point-to-point: blocking/nonbloking/persistent send & receive
    * Collective: broadcast, block/vector scatter & gather, reductions
  + Process groups and communication domains
    * Creation of new intra/inter communicators
    * Cartesian & graph topologies
  + Parallel input/output:
    * read & write
    * blocking/nonbloking & collective/noncollective
    * individual/shared file pointers & explicit offset
  + Dynamic process management
    * spawn & spawn multiple
    * accept/connect
    * name publishing & lookup
  + One-sided operations
    * remote memory access: put, get, accumulate
    * passive target syncronization: start/complete & post/wait
    * active target syncronization: lock & unlock

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       %{name}-common-devel = %{version}
Requires:       python-devel
Requires:       %plainpython(abi) = %python_version

%description    devel
Development libraries and headers needed to build packages using %{name}.

%package     -n %{name}-common-devel
Summary:        Shared development files for %{name}
%openmpi_devel_requires
Provides:       %{python_module mpi4py-common-devel = %{version}}
BuildArch:      noarch

%description -n %{name}-common-devel
Development libraries and headers needed to build packages using %{name}.

You normally do not need to install this directly, it will be pulled in by
the python-specific devel package.

%package     -n %{name}-doc
Summary:        Documentation for %{name}
Provides:       %{python_module mpi4py-doc = %{version}}
BuildArch:      noarch

%description -n %{name}-doc
Documentation files and demos for %{name}.

%prep
%autosetup -p1 -n mpi4py-%{version}
sed -i '1!b;/^#!\/usr\/bin\/env python/d' demo/python-config
chmod a-x demo/python-config demo/check-mpiexec/run.sh
rm docs/source/make.bat

%build
%setup_openmpi

export CFLAGS="%{optflags} -fno-strict-aliasing"
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install

mkdir -p %{buildroot}/%{_includedir}
%{python_expand # De-duplicate includes and also put them in a more generally-accessible location.
cp -r %{buildroot}%{$python_sitearch}/mpi4py/include/mpi4py %{buildroot}/%{_includedir}/
rm -r %{buildroot}%{$python_sitearch}/mpi4py/include/mpi4py
ln -s %{_includedir}/mpi4py %{buildroot}%{$python_sitearch}/mpi4py/include/mpi4py
%fdupes %{buildroot}%{$python_sitearch}
}
%fdupes %{buildroot}/%{_includedir}

mkdir -p %{buildroot}%{_docdir}%{name}
cp -r docs %{buildroot}%{_docdir}%{name}/
cp -r demo %{buildroot}%{_docdir}%{name}/
%fdupes %{buildroot}%{_docdir}%{name}

# Don't run tests in s390x, mpiexec is not too reliable running in the
# OBS virtual machine environment. bsc#1218604#c1
%ifnarch s390x
%check
export PYTHONDONTWRITEBYTECODE=1
export LANG=en_US.UTF-8
# https://mpi4py.readthedocs.io/en/stable/develop.html#testing
# obs server: no communication between processes?
donttest="-x test_spawn"
donttest+=" -x test_apply"
donttest+=" -x test_async_error_callback"
donttest+=" -x test_empty_iterable"
donttest+=" -x test_imap"
donttest+=" -x test_istarmap"
donttest+=" -x test_map"
donttest+=" -x test_starmap"
donttest+=" -x test_pool_worker_lifetime_early_close"
donttest+=" -x test_terminate"
# osc build local: hangs or takes too long?
donttest+=" -x test_p2p_obj"
donttest+=" -x testGetStatusAll"
donttest+=" -x testIMProbe"
donttest+=" -x testIS"
donttest+=" -x testMProbe"
donttest+=" -x testMessageProbeIProbe"
donttest+=" -x testProbe"
donttest+=" -x testTestAll"
donttest+=" -x testAll"
donttest+=" -x testWaitAll"
%ifarch %ix86
# https://github.com/mpi4py/mpi4py/issues/105
donttest+=" -x test_io"
# There are more broken tests in i586: https://github.com/mpi4py/mpi4py/issues/279
donttest+=" -x test_file -x test_subclass -x test_errhandler -x test_threads"
%endif
%setup_openmpi
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
rm -rf build _build.*
%{openmpi_prefix}/bin/mpiexec -n 1 $python -B test/main.py -v $donttest
}
%endif

%files %{python_files}
%doc CHANGES.rst DESCRIPTION.rst README.rst
%license LICENSE.rst
%{python_sitearch}/mpi4py
%{python_sitearch}/mpi4py-%{version}.dist-info
%exclude %{python_sitearch}/mpi4py/include/
%exclude %{python_sitearch}/mpi4py/*.h

%files %{python_files devel}
%license LICENSE.rst
%{python_sitearch}/mpi4py/include/
%{python_sitearch}/mpi4py/*.h

%files -n %{name}-common-devel
%license LICENSE.rst
%{_includedir}/mpi4py/

%files -n %{name}-doc
%license LICENSE.rst
%dir %{_docdir}%{name}
%{_docdir}%{name}/docs/
%{_docdir}%{name}/demo/

%changelog
