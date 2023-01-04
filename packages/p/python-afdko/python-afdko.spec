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
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%define binaries makeotf detype1 makeotfexe mergefonts rotatefont sfntdiff sfntedit \
                 spot afdko-tx type1 buildcff2vf buildmasterotfs \
                 comparefamily checkoutlinesufo makeinstancesufo \
                 otc2otf otf2otc otf2ttf ttfcomponentizer \
                 ttfdecomponentizer ttxn charplot digiplot fontplot \
                 fontplot2 fontsetplot hintplot waterfallplot

# Antlr4 needs to be built and statically linked from in-tree repository.
# See https://github.com/adobe-type-tools/afdko/issues/1407
# Check CMakeLists.txt for correct version
%define antlr4version 4.9.3

%define skip_python2 1
Name:           python-afdko%{psuffix}
Version:        3.9.1
Release:        0
Summary:        Adobe Font Development Kit for OpenType
License:        Apache-2.0 AND MIT
URL:            https://github.com/adobe-type-tools/afdko
Source0:        https://files.pythonhosted.org/packages/source/a/afdko/afdko-%{version}.tar.gz
# License1: MIT
Source1:        https://www.antlr.org/download/antlr4-cpp-runtime-%{antlr4version}-source.zip
# PATCH-FIX-OPENSUSE afdko-opensuse-custom-build.patch -- make sure we can build offline, code@bnavigator.de
Patch0:         afdko-opensuse-custom-build.patch
# PATCH-FIX-OPENSUSE use-system-libxml2.patch -- make sure we can build offline
Patch1:         use-system-libxml2.patch
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module scikit-build}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
BuildRequires:  utfcpp-devel
Requires:       python-Brotli >= 1.0.1
Requires:       python-FontTools >= 4.33.3
Requires:       python-booleanOperations >= 0.9.0
Requires:       python-defcon >= 0.10.1
Requires:       python-fontMath >= 0.9.2
Requires:       python-fontPens >= 0.1.0
Requires:       python-fs >= 2.2.0
Requires:       python-lxml >= 4.9.0
Requires:       python-mutatorMath >= 3.0.1
Requires:       python-psautohint >= 2.4.0
Requires:       python-tqdm >= 4.64.0
Requires:       python-ufoProcessor >= 1.9.0
Requires:       python-ufonormalizer >= 0.6.1
Requires:       python-zopfli >= 0.1.4
%if %{python_version_nodots} < 39
Requires:       python-unicodedata2 >= 13.0.0
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       adobe-afdko = %{version}-%{release}
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module afdko = %{version}}
BuildRequires:  %{python_module pytest}
# /SECTION
%endif
%python_subpackages

%description
Adobe Font Development Kit for OpenType

%prep
%autosetup -p1 -n afdko-%{version}

%build
%if ! %{with test}
%{python_expand # work around python_build parameter restriction: scikit-build calls cmake
%{$python_build} \
  --build-type=RelWithDebInfo \
  -j %{jobs} \
  -DANTLR4_ZIP_REPOSITORY=%{SOURCE1}
}
%endif

%install
%if ! %{with test}
%python_install
mv %{buildroot}%{_bindir}/tx  %{buildroot}%{_bindir}/afdko-tx

for binary in %{shrink:%binaries}; do
   %python_clone -a %{buildroot}%{_bindir}/$binary
done

ln -s -f %{_sysconfdir}/alternatives/tx %{buildroot}%{_bindir}/tx

%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
%{python_expand # use the u-a scripts of our flavor
mkdir -p build/bin
for b in %{shrink:%binaries}; do
  ln -s %{_bindir}/$b-%{$python_bin_suffix} build/bin/$b
done
ln -s afdko-tx build/bin/tx
}
export PATH=$PWD/build/bin:$PATH
mkdir tmp
export TMPDIR=tmp

# broken tests in latest build
donttest+=" or test_cjk_vf or test_sparse_cjk_vf or test_ufo_fontinfo_parsing[empty-key-name-fdarray--0] or test_ufo_fontinfo_parsing[bluesarray-string--0] or test_ufo_fontinfo_parsing[switched-string-and-array--0]"
%ifarch %{ix86}
# Precision issues
# https://github.com/adobe-type-tools/afdko/issues/1163
donttest+=" or test_type1mm_inputs or test_dump_option"
%endif
%ifarch %{power64} %{arm} aarch64
# command does not return error on these platforms
# https://github.com/adobe-type-tools/afdko/issues/1425
donttest+=" or (test_spec and bad.fea)"
%endif
# https://github.com/adobe-type-tools/afdko/issues/1589
donttest+=" or test_ufo_fontinfo_parsing"
%pytest_arch -k "not (dummyprefix $donttest)"
%endif

%if ! %{with test}
%post
%python_install_alternative %{binaries}
%{_sbindir}/update-alternatives --install %{_bindir}/tx tx %{_bindir}/afdko-tx-%{python_bin_suffix} %{python_version_nodots}

%postun
%python_uninstall_alternative makeotf
if [ ! -e %{_bindir}/afdko-tx-%{python_bin_suffix} ] ; then
  %{_sbindir}/update-alternatives --quiet --remove tx %{_bindir}/afdko-tx-%{python_bin_suffix}
fi

%files %{python_files}
%doc NEWS.md README.md
%license LICENSE.md
%ghost %{_sysconfdir}/alternatives/tx
%{_bindir}/tx
%{lua: for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/" .. b .. "\n"))
end}
%{python_sitearch}/afdko
%{python_sitearch}/afdko-%{version}*-info
%endif

%changelog
