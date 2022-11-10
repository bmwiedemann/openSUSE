#
# spec file for package python-mpi4py
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


%define skip_python2 1
%define skip_python36 1

Name:           python-mpi4py
Version:        3.1.4
Release:        0
Summary:        MPI for Python
License:        BSD-2-Clause
URL:            https://github.com/mpi4py/mpi4py
Source:         https://files.pythonhosted.org/packages/source/m/mpi4py/mpi4py-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  openmpi-macros-devel
BuildRequires:  python-rpm-macros
# Test dependencies
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module PyYAML}
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

%description    devel
Development libraries and headers needed to build packages using %{name}.

%package     -n %{name}-common-devel
Summary:        Shared development files for %{name}
%openmpi_devel_requires
Provides:       %{python_module mpi4py-common-devel = %{version}}

%description -n %{name}-common-devel
Development libraries and headers needed to build packages using %{name}
for both python2 and python3.

You normally do not need to install this directly, it will be pulled in by
the python-specific devel package.

%package     -n %{name}-doc
Summary:        Documentation for %{name}
Provides:       %{python_module mpi4py-doc = %{version}}

%description -n %{name}-doc
Documentation files and demos for %{name}.

%prep
%autosetup -p1 -n mpi4py-%{version}
rm demo/*/runtests.bat docs/source/usrman/make.bat docs/source/usrman/.gitignore
sed -i 's/\r$//' docs/usrman/objects.inv
sed -i '1!b;/^#!\/usr\/bin\/env python/d' demo/python-config
chmod a-x demo/python-config

# Remove this file to fix tests
# https://github.com/mpi4py/mpi4py/issues/279
rm test/dlpackimpl.py

%build
%setup_openmpi

export CFLAGS="%{optflags} -fno-strict-aliasing"
export LANG=en_US.UTF-8
%{python_build --force}

%install
export LANG=en_US.UTF-8
%python_install

# De-duplicate includes and also put them in a more generally-accessible location.
mkdir -p %{buildroot}/%{_includedir}
%python_expand cp -r %{buildroot}%{$python_sitearch}/mpi4py/include/mpi4py %{buildroot}/%{_includedir}/
%python_expand rm -r %{buildroot}%{$python_sitearch}/mpi4py/include/mpi4py
%python_expand ln -s %{_includedir}/mpi4py %{buildroot}%{$python_sitearch}/mpi4py/include/mpi4py

%python_expand %fdupes %{buildroot}%{$python_sitearch}

mkdir -p %{buildroot}%{_docdir}%{name}
cp -r docs %{buildroot}%{_docdir}%{name}/
cp -r demo %{buildroot}%{_docdir}%{name}/
%fdupes %{buildroot}%{_docdir}%{name}

mkdir -p %{buildroot}%{_rpmmacrodir}
cat >> %{buildroot}%{_rpmmacrodir}/macros.mpi4py <<EOL
mpi4py_mpi_ver openmpi
EOL

%check
export PYTHONDONTWRITEBYTECODE=1
export LANG=en_US.UTF-8
export OMPI_MCA_rmaps_base_oversubscribe=yes
donttest="test_spawn"
%ifarch %ix86
# https://github.com/mpi4py/mpi4py/issues/105
donttest+="|test_io"

# There are more broken tests in i586
# https://github.com/mpi4py/mpi4py/issues/279
donttest+="|test_file|test_subclass|test_errhandler|test_threads"
%endif
rm -rf build _build.*
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
rm -rf build _build.*
%setup_openmpi
%{openmpi_prefix}/bin/mpiexec --use-hwthread-cpus --mca btl tcp,self -n 1  $python -B test/runtests.py -v --exclude="$donttest"
}

%files %{python_files}
%doc CHANGES.rst DESCRIPTION.rst README.rst
%license LICENSE.rst
%{python_sitearch}/mpi4py
%{python_sitearch}/mpi4py-%{version}-py*.egg-info
%exclude %{python_sitearch}/mpi4py/include/

%files %{python_files devel}
%license LICENSE.rst
%{python_sitearch}/mpi4py/include/

%files -n %{name}-common-devel
%license LICENSE.rst
%{_includedir}/mpi4py/
%{_rpmmacrodir}/macros.mpi4py

%files -n %{name}-doc
%license LICENSE.rst
%dir %{_docdir}%{name}
%{_docdir}%{name}/docs/
%{_docdir}%{name}/demo/

%changelog
