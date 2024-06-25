#
# spec file for package python-onnx
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
# python-nbval needed for test isn't available python39
%define         skip_python39 1


# Tumbleweed does not have a python36-numpy anymore: NEP 29 dropped Python 3.6 for NumPy 1.20
Name:           python-onnx
Version:        1.16.0
Release:        0
Summary:        Open Neural Network eXchange
License:        MIT
URL:            https://onnx.ai/
Source0:        https://github.com/onnx/onnx/archive/v%{version}.tar.gz#/onnx-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module fb-re2}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module protobuf}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module pybind11}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  protobuf21-devel
BuildRequires:  python-rpm-macros
Requires:       libonnx == %version
Requires:       libonnx_proto == %version
Requires:       python-numpy
Requires:       python-protobuf
Requires:       python-typing_extensions >= 3.6.2.1
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-onnx-devel = %{version}-%{release}
Obsoletes:      python-onnx-devel < %{version}-%{release}
%python_subpackages

%description
Open format to represent deep learning models. With ONNX, AI developers can
more easily move models between state-of-the-art tools and choose the
combination that is best for them. ONNX is developed and supported by a
community of partners.

%package -n onnx-devel
Summary:        Header files of onnx
Requires:       libonnx == %version
Requires:       libonnx_proto == %version

%description  -n onnx-devel
Header files of ONNX.

%package -n libonnx
Summary:        Shared library for onnx

%description  -n  libonnx
This package exists to create libonnx_proto, so you do no want
to install this package.

%package -n libonnx_proto
Summary:        Shared library for onnx protocul bufer

%description  -n  libonnx_proto
Shared library for the protocol buffer library, packaged separately to be
used by external project.

%package -n onnx-backend-test
Summary:        Test data

%description -n onnx-backend-test
This packages includes the data for testing the backend.

%prep
%setup -q -n onnx-%{version}

# avoid bundles
rm -rf third_party
%autopatch -p1

# fix shebang
sed -i "s|^#!\s*%{_bindir}/env python|#!%{_bindir}/python3|" tools/protoc-gen-mypy.py

# build inside python_expand shuffled build dir also used by the cmake macro instead of upstream's custom dirname
sed -i "/^CMAKE_BUILD_DIR = / s/TOP_DIR, '.setuptools-cmake-build'/TOP_DIR, 'build'/" setup.py
# do not require extra pytest modules
#sed -i -e '/addopts/d' setup.cfg
# do not pull in pytest-runner as it is deprecated
sed -i -e '/pytest-runner/d' setup.py

%build
%{python_expand # Generate the build system using the distro macro, configuring everything to taste for every python flavor.
%cmake -DONNX_USE_PROTOBUF_SHARED_LIBS:BOOL=ON \
       -DONNX_WERROR:BOOL=OFF
# the macro stays in build/
cd ..
}
# let setup.py do the cmake build call (for every flavor)
%python_build

%install
%python_install
%cmake_install
%python_clone -a %{buildroot}%{_bindir}/backend-test-tools
%python_clone -a %{buildroot}%{_bindir}/check-node
%python_clone -a %{buildroot}%{_bindir}/check-model
%{python_expand # fix shebang
shebang_files="%{$python_sitearch}/onnx/backend/test/stat_coverage.py %{$python_sitearch}/onnx/defs/gen_doc.py %{$python_sitearch}/onnx/gen_proto.py"
for file in $shebang_files ; do
  sed -i 's|%{_bindir}/env python.*$|%{_bindir}/$python|' %{buildroot}/$file
  chmod 755 %{buildroot}/$file
done
}
%{?python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

#Disable tests for s390x based on IBM support without working tests boo#1215337
%ifnarch s390x
%check
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}"
# copy tests into clean subdir and test the installed lib in sitearch
mkdir cleantestdir
cp -r onnx/test onnx/examples cleantestdir/
pushd cleantestdir
# skip online tests
donttest="   test_bvlc_alexnet_cpu \
          or test_shufflenet_cpu \
          or test_densenet121_cpu \
          or test_squeezenet_cpu \
          or test_inception_v1_cpu \
          or test_vgg19_cpu \
          or test_inception_v2_cpu \
          or test_zfnet512_cpu \
          or test_resnet50_cpu \
          or reference_evaluator_backend_test"
# do not run in parallel yet - https://github.com/onnx/onnx/issues/3946#issuecomment-1015634235
%pytest_arch -n 1 -k "not ($donttest)" -ra
popd
%endif

%post
%python_install_alternative backend-test-tools
%python_install_alternative check-node
%python_install_alternative check-model

%postun
%python_uninstall_alternative backend-test-tools
%python_uninstall_alternative check-node
%python_uninstall_alternative check-model

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/check-model
%python_alternative %{_bindir}/check-node
%python_alternative %{_bindir}/backend-test-tools
%{python_sitearch}/onnx*

%files -n onnx-devel
%{_includedir}/onnx
%{_libdir}/cmake/*
%exclude %{_includedir}/onnx/backend

%files -n onnx-backend-test
%{_includedir}/onnx/backend

%files -n libonnx
%{_libdir}/libonnx.so

%files -n libonnx_proto
%{_libdir}/libonnx_proto.so

%changelog
