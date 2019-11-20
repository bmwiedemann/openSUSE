#
# spec file for package python-mpi4py
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
%if 0%{?sle_version} && 0%{?sle_version} < 150000
  %define mpiver  openmpi
%else
  %define mpiver  openmpi2
%endif
Name:           python-mpi4py
Version:        3.0.3
Release:        0
Summary:        MPI for Python
License:        BSD-2-Clause
URL:            https://bitbucket.org/mpi4py/mpi4py
Source:         https://files.pythonhosted.org/packages/source/m/mpi4py/mpi4py-%{version}.tar.gz
BuildRequires:  %{mpiver}
BuildRequires:  %{mpiver}-config
BuildRequires:  %{mpiver}-devel
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{mpiver}
Requires:       %{mpiver}-config
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
Requires:       %{mpiver}-devel
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
%setup -q -n mpi4py-%{version}
rm demo/*/runtests.bat docs/source/usrman/make.bat
sed -i 's/\r$//' docs/usrman/objects.inv

%build
source %{_libdir}/mpi/gcc/%{mpiver}/bin/mpivars.sh

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
mpi4py_mpi_ver %{mpiver}
EOL

%check
export PYTHONDONTWRITEBYTECODE=1
export LANG=en_US.UTF-8
export OMPI_MCA_rmaps_base_oversubscribe=yes
rm -rf build _build.*
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
rm -rf build _build.*
%{_libdir}/mpi/gcc/%{mpiver}/bin/mpiexec --use-hwthread-cpus --mca btl tcp,self -n 1  $python -B test/runtests.py -v --exclude="test_msgspec"
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
