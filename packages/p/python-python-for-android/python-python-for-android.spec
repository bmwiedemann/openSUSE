#
# spec file for package python-python-for-android
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


%define version_with_zeros 2024.01.21
Name:           python-python-for-android
Version:        2024.1.21
Release:        0
Summary:        Android APK packager for Python scripts and apps
License:        MIT
URL:            https://github.com/kivy/python-for-android
Source:         https://github.com/kivy/python-for-android/archive/refs/tags/v%{version_with_zeros}.tar.gz#/python-for-android-%{version}.tar.gz
Source1:        python-python-for-android-rpmlintrc
# PATCH-FIX-OPENSUSE We don't need or want isolation when determining metadata
Patch0:         no-isolation-for-metadata-build.patch
# PATCH-FIX-UPSTREAM gh#kivy/python-for-android#3003
Patch1:         fix-mock-assertion.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-appdirs
Requires:       python-build
Requires:       python-colorama >= 0.3.3
Requires:       python-packaging
Requires:       python-setuptools
Requires:       python-sh >= 2
Requires:       python-toml
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     cmake
Recommends:     python-pip
Recommends:     python-wheel
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module colorama >= 0.3.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sh >= 1.10}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ccache
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  lld
BuildRequires:  unzip
# /SECTION
%python_subpackages

%description
Android APK packager for Python scripts and apps

%prep
%autosetup -p1 -n python-for-android-%{version_with_zeros}

sed -i "1{s:#!.*$:#!%{_bindir}/bash:}" pythonforandroid/bootstraps/common/build/gradlew

find pythonforandroid/bootstraps/common/build/src/ -type f | xargs dos2unix
find pythonforandroid/bootstraps/common/build/src/ -type f | xargs chmod a-x

chmod a+x pythonforandroid/bootstraps/common/build/build.py

touch tests/__init__.py tests/recipes/__init__.py

sed -i 's/from backports import tempfile/import tempfile/' tests/test_recipe.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/python-for-android
%python_clone -a %{buildroot}%{_bindir}/p4a
%{python_expand rm -r %{buildroot}%{$python_sitelib}/ci/ %{buildroot}%{$python_sitelib}/tests/

sed -i "1{s:#!.*$:#!%{_bindir}/python%{$python_bin_suffix}:}" \
  %{buildroot}%{$python_sitelib}/pythonforandroid/tools/*link \
  %{buildroot}%{$python_sitelib}/pythonforandroid/bootstraps/common/build/build.py \
  %{buildroot}%{$python_sitelib}/pythonforandroid/toolchain.py

chmod a+x %{buildroot}%{$python_sitelib}/pythonforandroid/toolchain.py

%fdupes %{buildroot}%{$python_sitelib}
}

%check
export PYTHONPATH=${PWD}:${PWD}/tests/
# Five failures due to venv attempting download of pip, wheel, setuptools
skip_tests="test_get_dep_names_of_package or test_get_package_dependencies or test_venv or test_get_package_as_folder or test_extract_metainfo_files_from_package"
# Unable to download NDK
skip_tests="$skip_tests or (TestToolchainCL and test_create) or test_create_python_bundle"
# build_dir is somehow None
skip_tests="$skip_tests or (TestSDL2MixerRecipe and test_get_include_dirs)"

%pytest -rs tests -k "not ($skip_tests)"

%post
%python_install_alternative python-for-android p4a

%postun
%python_uninstall_alternative python-for-android

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/python-for-android
%python_alternative %{_bindir}/p4a
%{python_sitelib}/pythonforandroid
%{python_sitelib}/python_for_android-%{version}.dist-info

%changelog
