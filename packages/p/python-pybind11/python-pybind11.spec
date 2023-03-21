#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%define skip_python2 1
%define plainpython python
Name:           python-pybind11%{psuffix}
Version:        2.10.4
Release:        0
Summary:        Module for operability between C++11 and Python
License:        BSD-3-Clause
URL:            https://github.com/pybind/pybind11
Source:         https://github.com/pybind/pybind11/archive/v%{version}.tar.gz#/pybind11-%{version}.tar.gz
Source99:       python-pybind11-rpmlintrc
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake >= 3.18
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros >= 20220912
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
%if %{with test}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pybind11-devel = %{version}}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch
%python_subpackages

%description
pybind11 is a header-only library that exposes C++ types in Python
and vice versa, mainly to create Python bindings of existing C++
code. It can reduce boilerplate code in traditional extension modules
by inferring type information using compile-time introspection.

%package -n %{name}-common-devel
Summary:        Development files for pybind11
Provides:       %{python_module pybind11-common-devel = %{version}}

%description -n %{name}-common-devel
This package contains files for developing applications using pybind11.

%package devel
Summary:        Development files for pybind11
Requires:       %{name}-common-devel = %{version}
Requires:       python-devel
Requires:       python-pybind11 = %{version}
Requires:       %{plainpython}(abi) = %{python_version}

%description devel
This package contains files for developing applications using pybind11.

%prep
%setup -q -n pybind11-%{version}

%build
%if !%{with test}
%pyproject_wheel
# calling cmake to install header to right location and
# generate cmake include files
%{python_expand pushd .
%cmake \
  -DPYBIND11_INSTALL=ON \
  -DPYBIND11_TEST=OFF \
  -DPYTHON_EXECUTABLE:FILEPATH=%{_bindir}/$python
%cmake_build
popd
}
%else
%{python_expand pushd .
%cmake \
  -DPYBIND11_INSTALL=OFF \
  -DPYBIND11_TEST=ON \
  -DPYTHON_EXECUTABLE:FILEPATH=%{_bindir}/$python
%cmake_build
popd
}
%endif

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pybind11-config
%{python_expand #
%cmake_install
# remove duplicated header files from sitelibs but link to common dirs as some
# packages expect them to be in the sitelib where pybind11.get_include() reports them.
rm -r %{buildroot}%{$python_sitelib}/pybind11/include/pybind11
ln -s %{_includedir}/pybind11 %{buildroot}%{$python_sitelib}/pybind11/include/pybind11
# same for cmake files: pybind11.get_cmake_dir()
rm -r %{buildroot}%{$python_sitelib}/pybind11/share/cmake/pybind11
ln -s %{_datadir}/cmake/pybind11 %{buildroot}%{$python_sitelib}/pybind11/share/cmake/pybind11
# same for pkgconfig
rm %{buildroot}%{$python_sitelib}/pybind11/share/pkgconfig/pybind11.pc
ln -s %{_datadir}/pkgconfig/pybind11.pc %{buildroot}%{$python_sitelib}/pybind11/share/pkgconfig/pybind11.pc
%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%if %{with test}
%check
export PYTHONPATH=${PWD}/build/tests/
# tests fail as python3-widget is not in distribuion
ignore_tests="--ignore tests/test_embed/test_interpreter.py --ignore tests/test_embed/test_trampoline.py"
# no isolated build env with builddep wheels available
ignore_tests="$ignore_tests --ignore tests/extra_python_package/test_files.py"
%pytest $ignore_tests
%endif

%pretrans devel -p <lua>
-- https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
-- rh#447156
-- Define the paths to directory being replaced in the below.
-- DO NOT add a trailing slash at the end.
paths = {"%{python_sitelib}/pybind11/share/cmake/pybind11", "%{python_sitelib}/pybind11/include/pybind11"}
for i, path in ipairs(paths) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pybind11-config

%post
%python_install_alternative pybind11-config

%postun
%python_uninstall_alternative pybind11-config

%if !%{with test}
%files %{python_files}
%doc README.rst docs/changelog.rst
%license LICENSE
%python_alternative %{_bindir}/pybind11-config
%{python_sitelib}/pybind11
%exclude %{python_sitelib}/pybind11/share/cmake
%exclude %{python_sitelib}/pybind11/include
%{python_sitelib}/pybind11-%{version}*-info

%files -n %{name}-common-devel
%license LICENSE
%{_includedir}/pybind11
%{_datadir}/cmake/pybind11
%{_datadir}/pkgconfig/pybind11.pc

%files %{python_files devel}
%license LICENSE
%{python_sitelib}/pybind11/share/cmake
%ghost %{python_sitelib}/pybind11/share/cmake/pybind11.rpmmoved
%{python_sitelib}/pybind11/include
%ghost %{python_sitelib}/pybind11/include/pybind11.rpmmoved
%{python_sitelib}/pybind11/share/pkgconfig
%endif

%changelog
