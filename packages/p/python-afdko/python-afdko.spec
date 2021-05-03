#
# spec file for package python-afdko-test
#
# Copyright (c) 2021 SUSE LLC
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-afdko%{psuffix}
Version:        3.6.2
Release:        0
Summary:        Adobe Font Development Kit for OpenType
License:        Apache-2.0
URL:            https://github.com/adobe-type-tools/afdko
Source:         https://files.pythonhosted.org/packages/source/a/afdko/afdko-%{version}.tar.gz
Patch0:         skip-tests-failing-on-i586.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Brotli >= 1.0.1
Requires:       python-FontTools >= 4.21.1
Requires:       python-booleanOperations >= 0.9.0
Requires:       python-defcon >= 0.7.2
Requires:       python-fontMath >= 0.6.0
Requires:       python-fontPens >= 0.1.0
Requires:       python-fs >= 2.2.0
Requires:       python-lxml >= 4.6.2
Requires:       python-mutatorMath >= 3.0.1
Requires:       python-psautohint >= 2.3.0
Requires:       python-tqdm >= 4.58.0
Requires:       python-ufoProcessor >= 1.9.0
Requires:       python-ufonormalizer >= 0.5.3
Requires:       python-zopfli >= 0.1.4
%if %{python_version_nodots} < 39
Requires:       python-unicodedata2 >= 13.0.0
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       adobe-afdko
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
%setup -q -n afdko-%{version}
%patch0 -p1

%build
%if ! %{with test}
%python_build
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
%pytest_arch
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
